from __future__ import annotations

from digitalhub_runtime_kfp.entities.run.kfp_run.builder import RunKfpRunBuilder
from digitalhub_runtime_kfp.entities.task.kfp_pipeline.builder import TaskKfpPipelineBuilder
from digitalhub_runtime_kfp.entities.workflow.kfp.builder import WorkflowKfpBuilder

entity_builders = (
    (RunKfpRunBuilder.ENTITY_KIND, RunKfpRunBuilder),
    (TaskKfpPipelineBuilder.ENTITY_KIND, TaskKfpPipelineBuilder),
    (WorkflowKfpBuilder.ENTITY_KIND, WorkflowKfpBuilder),
)

try:
    from digitalhub_runtime_kfp.runtimes.builder import RuntimeKfpBuilder

    runtime_builders = ((kind, RuntimeKfpBuilder) for kind in WorkflowKfpBuilder().get_all_kinds())
except ImportError:
    runtime_builders = tuple()
