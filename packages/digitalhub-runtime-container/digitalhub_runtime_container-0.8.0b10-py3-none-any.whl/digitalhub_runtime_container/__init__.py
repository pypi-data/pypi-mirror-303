from __future__ import annotations

from digitalhub_runtime_container.entities.function.container.builder import FunctionContainerBuilder
from digitalhub_runtime_container.entities.run.container_run.builder import RunContainerRunBuilder
from digitalhub_runtime_container.entities.task.container_build.builder import TaskContainerBuildBuilder
from digitalhub_runtime_container.entities.task.container_deploy.builder import TaskContainerDeployBuilder
from digitalhub_runtime_container.entities.task.container_job.builder import TaskContainerJobBuilder
from digitalhub_runtime_container.entities.task.container_serve.builder import TaskContainerServeBuilder

entity_builders = (
    (FunctionContainerBuilder.ENTITY_KIND, FunctionContainerBuilder),
    (TaskContainerBuildBuilder.ENTITY_KIND, TaskContainerBuildBuilder),
    (TaskContainerDeployBuilder.ENTITY_KIND, TaskContainerDeployBuilder),
    (TaskContainerJobBuilder.ENTITY_KIND, TaskContainerJobBuilder),
    (TaskContainerServeBuilder.ENTITY_KIND, TaskContainerServeBuilder),
    (RunContainerRunBuilder.ENTITY_KIND, RunContainerRunBuilder),
)

try:
    from digitalhub_runtime_container.runtimes.builder import RuntimeContainerBuilder

    runtime_builders = ((kind, RuntimeContainerBuilder) for kind in FunctionContainerBuilder().get_all_kinds())
except ImportError:
    runtime_builders = tuple()
