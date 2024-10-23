# file: client.py
from enum import Enum
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode, urljoin

import requests
from requests.exceptions import RequestException

from truefoundry.common.constants import ENV_VARS
from truefoundry.pydantic_v1 import BaseModel, Field

DEFAULT_TTL = ENV_VARS.TFY_INTERNAL_SIGNED_URL_SERVER_DEFAULT_TTL
MAX_TIMEOUT = ENV_VARS.TFY_INTERNAL_SIGNED_URL_SERVER_MAX_TIMEOUT


class SignedURLAPIResponseDto(BaseModel):
    uri: str
    signed_url: str
    headers: Optional[Dict[str, Any]] = None


class SignedURLIsDirectoryAPIResponseDto(BaseModel):
    is_directory: bool = Field(..., alias="isDirectory")


class SignedURLExistsAPIResponseDto(BaseModel):
    exists: bool


class FileInfo(BaseModel):
    path: str
    is_directoy: bool = Field(..., alias="isDirectory")
    bytes: Optional[int] = None
    signedUrl: Optional[str] = None


class PagedList(BaseModel):
    items: List[FileInfo]
    token: Optional[str] = None


class SignedURLServerEndpoint(str, Enum):
    """Enumeration for Signed URL Server endpoints."""

    READ = "/v1/signed-uri/read"
    WRITE = "/v1/signed-uri/write"
    EXISTS = "/v1/exists"
    IS_DIRECTORY = "/v1/is-dir"
    LIST_FILES = "/v1/list-files"


class SignedURLClient:
    """Client to interact with the Signed URL Server for file operations."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        token: Optional[str] = None,
        ttl: int = DEFAULT_TTL,
    ):
        """
        Initialize the SignedURLClient.

        Args:
            base_url (str): Base URL of the signed URL server (optional).
            token (str): Token for authentication (optional).
            ttl (int): Default time-to-live for signed URLs in seconds.
        """
        self.base_url = base_url or ENV_VARS.TFY_INTERNAL_SIGNED_URL_SERVER_HOST
        self.token = token or ENV_VARS.TFY_INTERNAL_SIGNED_URL_SERVER_TOKEN
        self.ttl = ttl

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def _make_request(
        self, endpoint: str, method: str = "GET", payload: Optional[Dict] = None
    ) -> Dict:
        """
        Internal method to handle requests to the signed URL server.

        Args:
            endpoint (str): The endpoint for the request.
            method (str): HTTP method (GET, POST, etc.).
            payload (Dict, optional): JSON payload for the request.

        Returns:
            Dict: JSON response from the server.

        Raises:
            RuntimeError: For network errors or invalid responses.
        """
        url = urljoin(self.base_url, endpoint)
        try:
            response = requests.request(
                method, url, headers=self.headers, json=payload, timeout=MAX_TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise RuntimeError(f"Error during request to {url}: {e}") from e

    def _make_server_api_call(
        self, endpoint: SignedURLServerEndpoint, params: Optional[Dict] = None
    ) -> Dict:
        """Get a signed URL for the specified operation and URI."""
        query_string = urlencode(params or {})
        endpoint_with_params = f"{endpoint.value}?{query_string}"
        return self._make_request(endpoint_with_params)

    def _upload_data(self, signed_url: str, data: Any) -> None:
        """Helper method to upload data to the signed URL."""
        try:
            # TODO: Add TIMEOUT to this request
            response = requests.put(
                signed_url,
                headers={"Content-Type": "application/octet-stream"},
                data=data,
            )
            response.raise_for_status()
        except Exception as e:
            raise RuntimeError(f"Failed to upload data: {e}") from e

    def upload_from_bytes(self, data: bytes, storage_uri: str) -> str:
        """Upload bytes to the specified storage path using a signed URL."""
        signed_object = self._make_server_api_call(
            endpoint=SignedURLServerEndpoint.WRITE,
            params={"uri": storage_uri, "expiryInSeconds": self.ttl},
        )
        pre_signed_object_dto = SignedURLAPIResponseDto.parse_obj(signed_object)
        self._upload_data(pre_signed_object_dto.signed_url, data)
        return storage_uri

    def upload(self, file_path: str, storage_uri: str) -> str:
        """Upload a file to the specified storage path using a signed URL."""
        print(f"Uploading {file_path} to {storage_uri}")
        response = self._make_server_api_call(
            endpoint=SignedURLServerEndpoint.WRITE,
            params={"uri": storage_uri, "expiryInSeconds": self.ttl},
        )
        pre_signed_object_dto = SignedURLAPIResponseDto.parse_obj(response)
        with open(file_path, "rb") as file:
            self._upload_data(pre_signed_object_dto.signed_url, file)
        return storage_uri

    def _download_file(
        self, signed_url: str, local_path: Optional[str] = None
    ) -> Optional[bytes]:
        """Common method to download a file using a signed URL.

        Args:
            signed_url (str): The signed URL to download from.
            local_path (Optional[str]): The local path to save the file. If None, the file will not be saved.

        Returns:
            Optional[bytes]: The content of the downloaded file if local_path is None; otherwise, None.
        """
        try:
            # TODO: Add TIMEOUT to this request
            response = requests.get(
                signed_url,
                stream=True,
                headers=self.headers,
            )
            response.raise_for_status()

            if local_path:
                with open(local_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                return None  # File saved successfully; no need to return content.

            return response.content  # Return the content if not saving to a local path.

        except requests.RequestException as e:
            raise RuntimeError(f"Failed to download file from {signed_url}: {e}") from e

    def download(self, storage_uri: str, local_path: str) -> Optional[str]:
        """Download a file from the specified storage path to a local path using a signed URL.

        Args:
            storage_uri (str): The storage URI to download the file from.
            local_path (str): The local path to save the downloaded file.

        Returns:
            Optional[str]: The local path if successful; None if the file is saved.
        """
        print(f"Dowloading {storage_uri} to {local_path}")
        response = self._make_server_api_call(
            endpoint=SignedURLServerEndpoint.READ,
            params={"uri": storage_uri, "expiryInSeconds": self.ttl},
        )
        presigned_object = SignedURLAPIResponseDto.parse_obj(response)
        self._download_file(presigned_object.signed_url, local_path)
        return local_path  # Indicate successful download.

    def download_to_bytes(self, storage_uri: str) -> bytes:
        """Download a file from the specified storage path and return it as bytes.

        Args:
            storage_uri (str): The storage URI to download the file from.

        Returns:
            bytes: The content of the downloaded file.
        """
        response = self._make_server_api_call(
            endpoint=SignedURLServerEndpoint.READ,
            params={"uri": storage_uri, "expiryInSeconds": self.ttl},
        )
        presigned_object = SignedURLAPIResponseDto.parse_obj(response)
        return self._download_file(presigned_object.signed_url)

    def exists(self, uri: str) -> bool:
        """Check if a file exists at the specified path."""
        response = self._make_server_api_call(
            endpoint=SignedURLServerEndpoint.EXISTS, params={"uri": uri}
        )
        response_obj = SignedURLExistsAPIResponseDto.parse_obj(response)
        return response_obj.exists

    def is_directory(self, uri: str) -> bool:
        """Check if the specified URI is a directory."""
        response = self._make_server_api_call(
            endpoint=SignedURLServerEndpoint.IS_DIRECTORY, params={"path": uri}
        )
        response_obj = SignedURLIsDirectoryAPIResponseDto.parse_obj(response)
        print(f"Path {uri} is_directory: {response_obj.is_directory}")
        return response_obj.is_directory

    def list_files(self, path: str, detail: bool = False, max_results: int = 1000):
        """List files in the specified directory."""
        token = ""
        items: List[FileInfo] = []
        # Fetch all files in the specified path, in pages of max_results
        while True:
            response = self._make_server_api_call(
                endpoint=SignedURLServerEndpoint.LIST_FILES,
                params={"path": path, "maxResults": max_results, "pageToken": token},
            )
            response_obj = PagedList.parse_obj(response)
            items.extend(response_obj.items)
            token = response_obj.token
            if not token:
                break

        # Return the items or paths based on the detail flag
        if detail:
            return items
        return [item.path for item in items]
