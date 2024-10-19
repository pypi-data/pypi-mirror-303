# SPDX-FileCopyrightText: 2024 CERN
#
# SPDX-License-Identifier: BSD-4-Clause

import os
import pathlib
from abc import ABC, abstractmethod
from typing import Dict, Mapping, Type

from pymbse.commons.schemas import (
    ExecEnvironment,
    ExecutionSource,
    ModelExecutionReference,
    ModelSource,
)
from pymbse.exec.io import ModelSourceAdapter


class ExecutionError(RuntimeError):
    def __init__(self, *args, error_files: dict[str, pathlib.Path]):
        super().__init__(*args)
        self.error_files = error_files


class ToolAdapter(ABC):
    registry: dict[str, dict[str, Type["ToolAdapter"]]] = {}

    def __init_subclass__(cls, tool_name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        if tool_name in cls.registry:
            raise ValueError(
                f"Execution environment for {tool_name} already registered in adapter. Duplicate?"
            )
        cls.registry[tool_name] = {"*": cls}

    @abstractmethod
    def __init__(
        self,
        exec_environment: ExecEnvironment,
        execution_reference: ModelExecutionReference,
        model_source: ModelSource,
        execution_source: ExecutionSource,
    ):
        self.exec_environment = exec_environment
        self.execution_reference = execution_reference
        self.model_source = model_source
        self.execution_source = execution_source

    def load_inputs(
        self, source_adapter: ModelSourceAdapter
    ) -> tuple[pathlib.Path, Dict[str, pathlib.Path]]:
        """Default implementation to load inputs before execution"""
        return source_adapter.load_inputs(self.execution_reference)

    def store_outputs(
        self,
        source_adapter: ModelSourceAdapter,
        outputs: Mapping[str, str | os.PathLike],
        execption_raised: bool,
    ) -> None:
        """Default implementation to store outputs after execution"""
        source_adapter.store_outputs(
            self.execution_reference, outputs, execption_raised
        )

    def load_execute_store(self) -> None:
        source_adapter = ModelSourceAdapter.get_adapter(
            self.model_source, self.execution_source
        )
        exec_dir, inputs = self.load_inputs(source_adapter)
        try:
            outputs = self.execute_tool(self.exec_environment, exec_dir, inputs)
        except ExecutionError as ee:
            self.store_outputs(source_adapter, ee.error_files, True)
            raise ee
        self.store_outputs(source_adapter, outputs, False)

    @abstractmethod
    def execute_tool(
        self,
        exec_environment: ExecEnvironment,
        io_dir: pathlib.Path,
        input_files: Dict[str, pathlib.Path],
    ) -> dict[str, pathlib.Path]:
        """
        Execute tool

        :param exec_environment: The execution environment
        :type exec_environment: ExecEnvironment
        :param io_dir: The input/output working directory
        :type io_dir: pathlib.Path
        :param input_files: Dict of input files
        :type input_files: Dict[str,pathlib.Path]

        :return: Dict of output files
        :rtype: Dict[str,pathlib.Path]

        :raises: ExecutionError(message:str,error_files:dict[str,pathlib.Path]) if execution fails.
            The error_files dict contains error information uploaded as result for the user
        """
        raise NotImplementedError()

    @classmethod
    def get_adapter(
        cls,
        execution_env: ExecEnvironment,
        reference: ModelExecutionReference,
        model_source: ModelSource,
        execution_source: ExecutionSource,
    ) -> "ToolAdapter":
        if execution_env.name not in cls.registry:
            raise ValueError(
                f"Execution environment for {execution_env.name} not registered in adapter. Possible values: {','.join(cls.registry.keys())}"
            )
        if execution_env.version in cls.registry[execution_env.name]:
            return cls.registry[execution_env.name][execution_env.version](
                exec_environment=execution_env,
                execution_reference=reference,
                model_source=model_source,
                execution_source=execution_source,
            )

        return cls.registry[execution_env.name]["*"](
            exec_environment=execution_env,
            execution_reference=reference,
            model_source=model_source,
            execution_source=execution_source,
        )
