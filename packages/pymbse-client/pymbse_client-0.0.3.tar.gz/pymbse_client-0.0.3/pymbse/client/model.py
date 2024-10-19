# SPDX-FileCopyrightText: 2024 CERN
#
# SPDX-License-Identifier: BSD-4-Clause

import os
import pathlib
import tempfile
import typing
from abc import ABC, abstractmethod
from typing import Any

import yaml

from pymbse.client.cache import PymbseCache
from pymbse.client.config import (
    ModelConfig,
    ModelSourceConfig,
    ModelSourceType,
    PymbseConfig,
    extract_system_model_input,
)
from pymbse.client.manage import PymbseManage
from pymbse.commons.schemas import ModelExecutionReference, ModelReference


class PymbseSubmodel:
    """Pymbse submodel actions

    Class functions to extract results from a submodel run
    """

    def __init__(
        self, cache_uri: str, model_execution: ModelExecutionReference
    ) -> None:
        self.model_execution_reference = model_execution
        self.cache = PymbseCache(cache_uri)

    def list_outputs(self) -> list[str]:
        return self.cache.get_uploaded_outputs(self.model_execution_reference)

    def download_output(
        self, name: str, outpuput_dir: str | os.PathLike
    ) -> pathlib.Path:
        return self.cache.download_output(
            self.model_execution_reference, name, outpuput_dir
        )

    def download_all_outputs(
        self, output_dir: str | os.PathLike
    ) -> dict[str, pathlib.Path]:
        return self.cache.download_outputs(self.model_execution_reference, output_dir)


class PymbseModel(ABC):
    """PymbseModel actions.

    Class providing access to model specific information and actions:
        - Loading of Inputs
        - Dependency resolution
        - Storing of outputs

    Depending of the execution envirnoment (running interactive/local or in evaluation mode), functions will have different behaviour.
    For example, a model in interactive mode will not store any outputs in an execution job (as they are not guaranteed to be
    reproducible). Also, inputs are not loaded from the cache.

    In evaluation mode, input dependencies are already resolved and stored in the cache.
    """

    def __init__(
        self,
        config: PymbseConfig,
        model_reference: ModelReference,
    ) -> None:
        """Create a new Pymbse object.

        If no parameters are given, the objects infers model name, system name and configuration from
        it's local position in the file system. Otherwise the values can be explicitly given.

        :param config: A configuration object, defaults to None
        :type config: PymbseConfig | None, optional
        :param model_name: Name of the model, defaults to None
        :type model_name: str | None, optional
        :param system_name: Name of the system, defaults to None
        :type system_name: str | None, optional
        """
        self.config = config
        self.model_reference = model_reference
        self._manage = PymbseManage(config)
        self.cache = PymbseCache(self.config.config.cache_uri)

    @property
    def modelconfig(self) -> ModelConfig:
        return self.config.get_model(self.model_reference)

    @property
    def sourceconfig(self) -> ModelSourceConfig:
        return self.config.get_source(self.model_reference)

    @property
    def manage(self) -> PymbseManage:
        return self._manage

    def run_execution(
        self,
        execution_environment: str,
        files: typing.Mapping[str, str | os.PathLike],
        force_execution: bool = False,
    ) -> PymbseSubmodel:
        exec_ref = self._manage.run_in_environment(
            self.model_reference, files, execution_environment, force_execution
        )
        return PymbseSubmodel(self.config.config.cache_uri, exec_ref)

    def run_submodels(
        self,
        submodels: list[ModelReference],
        files: dict[ModelReference, typing.Mapping[str, str | os.PathLike]],
        force_execution: bool = False,
    ) -> dict[ModelReference, PymbseSubmodel]:
        refs = self._manage.run_submodels(
            self.model_reference, submodels, files, force_execution
        )
        return {
            ModelReference(system=ref.system, model=ref.model): PymbseSubmodel(
                self.config.config.cache_uri, ref
            )
            for ref in refs
        }

    @staticmethod
    def create(
        config: PymbseConfig | None = None,
        model_reference: ModelReference | None = None,
    ) -> "PymbseModel":
        if not config:
            config = PymbseModel._find_config()
        if not model_reference:
            model_name = PymbseModel._find_model_name()
            system_name = PymbseModel._find_system_name()
            model_reference = ModelReference(system=system_name, model=model_name)

        source = config.get_source(model_reference)

        if source.data_source == ModelSourceType.MMBSE:
            raise NotImplementedError("MMBSE model not yet implemented")
        elif source.data_source == ModelSourceType.CACHE:
            return PymbseModelCache(config, model_reference)
        elif source.data_source == ModelSourceType.LOCAL:
            return PymbseModelLocal(config, model_reference)
        else:
            raise NotImplementedError(
                f"Unknown data source, or not implemented: {source.data_source}"
            )

    @staticmethod
    def _find_config() -> PymbseConfig:
        """Find the config file.

        Checks the following locations:
            - ./inputs/model_config.yml # Relative to model
            - ../../model_config.yml # Main data path

        raises:
            FileNotFoundError: if no config file is found
        """
        local_model = pathlib.Path("./model_config.yaml")
        main_model = pathlib.Path("../../model_config.yaml")

        files = [
            local_model,
            local_model.with_suffix(".yml"),
            main_model,
            main_model.with_suffix(".yml"),
        ]

        for file in files:
            if file.is_file():
                return PymbseConfig.load_from_file(file)

        searched_paths = "\n".join([str(file.absolute()) for file in files])
        raise FileNotFoundError(
            f"No config file found in model input folder or main data folder. Paths searched:\n{searched_paths}"
        )

    @staticmethod
    def _find_model_name() -> str:
        current_path = pathlib.Path.cwd()
        model_name = current_path.name
        return model_name

    @staticmethod
    def _find_system_name() -> str:
        current_path = pathlib.Path.cwd()
        system_name = current_path.parent.name
        return system_name

    def get_input_params(self, name: str) -> dict[str, Any]:
        filepath = self.get_input_file(name)
        return yaml.safe_load(filepath.read_text())

    def store_output_params(self, name: str, values: dict[str, Any]) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            filename = pathlib.Path(tempdir) / f"{name}.yml"
            with open(filename, "w") as f:
                yaml.dump(values, f)
            self.store_file(name, filename)

    @abstractmethod
    def prepare_model(self) -> None:
        """Prepare model before use.

        Verifies all dependencies are resolved.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_input_file(self, name: str) -> pathlib.Path:
        raise NotImplementedError()

    @abstractmethod
    def store_file(self, name: str, path: pathlib.Path) -> None:
        raise NotImplementedError()

    @abstractmethod
    def finalize(self) -> None:
        raise NotImplementedError()


class PymbseModelCache(PymbseModel):
    def __init__(
        self,
        config: PymbseConfig,
        model_reference: ModelReference,
    ) -> None:
        super().__init__(config, model_reference)
        if self.sourceconfig.source_reference is None:
            raise ValueError("No execution reference for source model set")
        self.execution = ModelExecutionReference(
            system=self.model_reference.system,
            model=self.model_reference.model,
            execution=self.sourceconfig.source_reference,
        )
        self.iopath = pathlib.Path(".")
        self.outputs_registered: dict[str, pathlib.Path] = {}

    def prepare_model(self) -> None:
        # All dependencies should be executed in advance, check that all exists
        inputs = set(self.cache.get_uploaded_inputs(self.execution))
        missing_inputs = set(self.modelconfig.inputs) - inputs
        if missing_inputs:
            raise ValueError(
                f"Not all input references are present in model: {missing_inputs}. Cannot execute"
            )

        # Lock model inputs
        self.cache.lock_inputs(self.execution, ignore_locked=True)

    def get_input_file(self, name: str) -> pathlib.Path:
        return self.cache.download_input(self.execution, name, self.iopath, None)

    def store_file(self, name: str, path: pathlib.Path) -> None:
        self.cache.upload_output(self.execution, name, path)
        self.outputs_registered[name] = path

    def finalize(self) -> None:
        # Wait with locking outputs, notebook will be uploaded after script is finished
        missing_outputs = set(self.modelconfig.outputs) - set(self.outputs_registered)
        if missing_outputs:
            raise ValueError(
                f"Outputs {missing_outputs} not regisreted during execution."
            )


class PymbseModelLocal(PymbseModel):
    def __init__(
        self,
        config: PymbseConfig,
        model_reference: ModelReference,
    ) -> None:
        super().__init__(config, model_reference)
        self.dependencies: dict[str, pathlib.Path] = {}
        self.outputs_registered: dict[str, pathlib.Path] = {}
        self.execution_ref: str | None = None
        self.iopath = pathlib.Path(".")

    def prepare_model(self) -> None:
        manage = PymbseManage(self.config)
        execution_ref = manage.run_model_dependencies(
            self.model_reference, include_model=False
        )

        # Load dependencies
        for name, dep in self.modelconfig.inputs.items():
            if dep.reference:
                sys, mod, output = extract_system_model_input(dep.reference)
                out_path = manage.cache.download_output(
                    ModelExecutionReference(
                        system=sys, model=mod, execution=execution_ref
                    ),
                    output,
                    self.iopath,
                    dep.filename,
                )
                self.dependencies[name] = out_path

        self.execution_ref = execution_ref

    def get_input_file(self, name: str) -> pathlib.Path:
        try:
            file = self.modelconfig.inputs[name]
        except KeyError as ke:
            raise ValueError(f"Input {name} not found in model") from ke

        if file.reference:
            return self.dependencies[name]
        elif file.filename:
            return pathlib.Path(file.filename)
        else:
            raise ValueError(f"Input {name} is has neither filename nor reference")

    def store_file(self, name: str, path: pathlib.Path) -> None:
        self.outputs_registered[name] = path

    def finalize(self) -> None:
        missing_outputs = set(self.modelconfig.outputs) - set(self.outputs_registered)
        outputs_not_in_model = set(self.outputs_registered) - set(
            self.modelconfig.outputs
        )
        for onim in outputs_not_in_model:
            print(
                f"Output {onim} (file: {self.outputs_registered[onim]}) not registered as output in model."
            )
        if missing_outputs:
            raise ValueError(
                f"Outputs {missing_outputs} not regisreted during execution."
            )
