# SPDX-FileCopyrightText: 2024 CERN
#
# SPDX-License-Identifier: BSD-4-Clause

from typing import Any

from celery import shared_task

from pymbse.commons.schemas import (
    ExecEnvironment,
    ExecutionSource,
    ModelExecutionReference,
    ModelSource,
)
from pymbse.exec.tools import ToolAdapter


@shared_task
def execute_model(
    exec_ref: dict[str, Any],
    exec_env: dict[str, Any],
    mod_source: dict[str, Any],
    exec_source: dict[str, Any],
    **kwargs,
) -> None:
    execution_reference: ModelExecutionReference = (
        ModelExecutionReference.model_validate(exec_ref)
    )
    execution_env: ExecEnvironment = ExecEnvironment.model_validate(exec_env)
    model_source: ModelSource = ModelSource.model_validate(mod_source)
    execution_source: ExecutionSource = ExecutionSource.model_validate(exec_source)

    tool_adapter = ToolAdapter.get_adapter(
        execution_env, execution_reference, model_source, execution_source
    )
    tool_adapter.load_execute_store()
