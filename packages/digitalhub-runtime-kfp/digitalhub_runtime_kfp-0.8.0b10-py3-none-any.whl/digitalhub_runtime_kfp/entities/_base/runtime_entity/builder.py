from __future__ import annotations

from digitalhub.entities._base.runtime_entity.builder import RuntimeEntityBuilder


class RuntimeEntityBuilderKfp(RuntimeEntityBuilder):
    EXECUTABLE_KIND = "kfp"
    TASKS_KINDS = [
        {
            "kind": "kfp+pipeline",
            "action": "pipeline",
        },
    ]
    RUN_KIND = "kfp+run"
