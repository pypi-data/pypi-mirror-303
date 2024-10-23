from __future__ import annotations

import typing

from digitalhub.entities.workflow._base.entity import Workflow

if typing.TYPE_CHECKING:
    from digitalhub_runtime_kfp.entities.workflow.kfp.spec import WorkflowSpecKfp
    from digitalhub_runtime_kfp.entities.workflow.kfp.status import WorkflowStatusKfp

    from digitalhub.entities._base.entity.metadata import Metadata


class WorkflowKfp(Workflow):
    """
    WorkflowKfp class.
    """

    def __init__(
        self,
        project: str,
        name: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: WorkflowSpecKfp,
        status: WorkflowStatusKfp,
        user: str | None = None,
    ) -> None:
        super().__init__(project, name, uuid, kind, metadata, spec, status, user)

        self.spec: WorkflowSpecKfp
        self.status: WorkflowStatusKfp
