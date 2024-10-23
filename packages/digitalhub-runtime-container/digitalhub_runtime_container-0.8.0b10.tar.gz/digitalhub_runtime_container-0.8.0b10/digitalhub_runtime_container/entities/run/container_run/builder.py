from __future__ import annotations

from digitalhub_runtime_container.entities._base.runtime_entity.builder import RuntimeEntityBuilderContainer
from digitalhub_runtime_container.entities.run.container_run.entity import RunContainerRun
from digitalhub_runtime_container.entities.run.container_run.spec import RunSpecContainerRun, RunValidatorContainerRun
from digitalhub_runtime_container.entities.run.container_run.status import RunStatusContainerRun

from digitalhub.entities.run._base.builder import RunBuilder


class RunContainerRunBuilder(RunBuilder, RuntimeEntityBuilderContainer):
    """
    RunContainerRunBuilder runer.
    """

    ENTITY_CLASS = RunContainerRun
    ENTITY_SPEC_CLASS = RunSpecContainerRun
    ENTITY_SPEC_VALIDATOR = RunValidatorContainerRun
    ENTITY_STATUS_CLASS = RunStatusContainerRun
    ENTITY_KIND = "container+run"
