from __future__ import annotations

from digitalhub.entities._base.runtime_entity.builder import RuntimeEntityBuilder


class RuntimeEntityBuilderContainer(RuntimeEntityBuilder):
    EXECUTABLE_KIND = "container"
    TASKS_KINDS = [
        {
            "kind": "container+job",
            "action": "job",
        },
        {
            "kind": "container+build",
            "action": "build",
        },
        {
            "kind": "container+serve",
            "action": "serve",
        },
        {
            "kind": "container+deploy",
            "action": "deploy",
        },
    ]
    RUN_KIND = "container+run"
