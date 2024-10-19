# SPDX-FileCopyrightText: 2024 CERN
#
# SPDX-License-Identifier: BSD-4-Clause

import os
import pathlib
import tempfile
from abc import ABC, abstractmethod
from typing import Dict, Mapping, Tuple, Type

from pydantic_yaml import to_yaml_str

from pymbse.client.cache import PymbseCache
from pymbse.client.config import PymbseConfig, SettingsConfig
from pymbse.commons.schemas import (
    ExecutionSource,
    ModelExecutionReference,
    ModelSource,
)


class ModelSourceAdapter(ABC):
    registry: Dict[str, Type["ModelSourceAdapter"]] = {}

    def __init_subclass__(cls, io_name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        if io_name in cls.registry:
            raise ValueError(
                f"ModelSource for {io_name} already registered in adapter. Duplicate?"
            )
        cls.registry[io_name] = cls

    @abstractmethod
    def __init__(self, mod_source: ModelSource, execution_source: ExecutionSource):
        self.mod_source = mod_source
        self.execution_source = execution_source
        self.temp_directory = tempfile.TemporaryDirectory()

    def __del__(self):
        self.temp_directory.cleanup()

    @abstractmethod
    def load_inputs(
        self,
        exection_ref: ModelExecutionReference,
        input_filter: list[str] | None = None,
    ) -> Tuple[pathlib.Path, Dict[str, pathlib.Path]]:
        raise NotImplementedError()

    @abstractmethod
    def store_outputs(
        self,
        execution_reference: ModelExecutionReference,
        outputs: Mapping[str, str | os.PathLike],
        execution_failure: bool,
    ) -> None:
        raise NotImplementedError()

    @classmethod
    def get_adapter(
        cls, mod_source: ModelSource, execution_source: ExecutionSource
    ) -> "ModelSourceAdapter":
        if mod_source.name not in cls.registry:
            raise ValueError(
                f"ModelSource for {mod_source.name} not registered in adapter. Possible values: {','.join(cls.registry.keys())}"
            )

        return cls.registry[mod_source.name](mod_source, execution_source)


class PymbseCacheFileAdapter(ModelSourceAdapter, io_name="pymbse-cache"):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache = PymbseCache(self.mod_source.uri)

    def load_inputs(
        self,
        execution_reference: ModelExecutionReference,
        input_filter: list[str] | None = None,
    ) -> Tuple[pathlib.Path, Dict[str, pathlib.Path]]:
        # load execution
        tmp_base = pathlib.Path(self.temp_directory.name)
        tmp_path = tmp_base / execution_reference.system / execution_reference.model
        tmp_path.mkdir(parents=True, exist_ok=True)

        model_execution = self.cache.get_execution(execution_reference)
        if input_filter:
            inputs = {}
            for inp in input_filter:
                if inp not in model_execution.inputs:
                    raise ValueError(
                        f"Input {inp} not found in model execution {execution_reference}"
                    )
                inputs[inp] = self.cache.download_input(
                    model_execution.get_reference(), inp, tmp_path, None
                )
        else:
            inputs = self.cache.download_inputs(model_execution, tmp_path)

        # create a model config
        config = PymbseConfig.create_from_model_executions(
            [model_execution],
            SettingsConfig(
                cache_uri=self.mod_source.uri, exec_uri=self.execution_source.uri
            ),
        )

        # write model config
        model_config_path = tmp_base / "model_config.yml"
        with open(model_config_path, "w") as f:
            f.write(to_yaml_str(config))

        return (tmp_path, inputs)

    def store_outputs(
        self,
        execution_reference: ModelExecutionReference,
        outputs: Mapping[str, str | os.PathLike],
        execution_failure: bool,
    ) -> None:
        self.cache.upload_outputs(execution_reference, outputs, True, execution_failure)
