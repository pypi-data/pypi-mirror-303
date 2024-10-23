try:
    import fsspec
    from flytekit import task as _
except ImportError:
    print("To use workflows, please run 'pip install truefoundry[workflow]'.")

from flytekit import conditional
from flytekit.types.directory import FlyteDirectory

from truefoundry.common.tfy_signed_url_fs import SignedURLFileSystem
from truefoundry.deploy.v2.lib.patched_models import (
    ContainerTaskConfig,
    PythonTaskConfig,
    TaskDockerFileBuild,
    TaskPythonBuild,
)
from truefoundry.workflow.container_task import ContainerTask
from truefoundry.workflow.map_task import map_task
from truefoundry.workflow.python_task import PythonFunctionTask
from truefoundry.workflow.task import task
from truefoundry.workflow.workflow import ExecutionConfig, workflow

__all__ = [
    "task",
    "ContainerTask",
    "PythonFunctionTask",
    "map_task",
    "workflow",
    "conditional",
    "FlyteDirectory",
    "TaskDockerFileBuild",
    "TaskPythonBuild",
    "ContainerTaskConfig",
    "PythonTaskConfig",
    "ExecutionConfig",
]
print("SignedURL FS Spec registered for s3 and gs")
fsspec.register_implementation("s3", SignedURLFileSystem, clobber=True)
fsspec.register_implementation("gs", SignedURLFileSystem, clobber=True)
