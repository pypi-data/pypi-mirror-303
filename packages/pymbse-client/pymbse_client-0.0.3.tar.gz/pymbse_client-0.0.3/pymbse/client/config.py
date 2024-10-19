# SPDX-FileCopyrightText: 2024 CERN
#
# SPDX-License-Identifier: BSD-4-Clause

import graphlib
import os
import pathlib
import re
import typing
from dataclasses import dataclass
from enum import Enum
from pathlib import Path, PurePosixPath
from typing import Sequence

import yaml
from pydantic import BaseModel, ConfigDict, SerializeAsAny

from pymbse.commons.schemas import (
    ArtefactResource,
    ArtefactResourceRef,
    ExecEnvironment,
    Model,
    ModelExecution,
    ModelReference,
    ResourceType,
)


def extract_system_model_input(input_str: str) -> tuple[str, str, str]:
    """Extract system, model and input name from a reference string"""
    input_regex = r"([^.]+)\.([^.]+)\.([^.]+)"
    matcher = re.compile(input_regex)
    if match := matcher.match(input_str):
        return match[1], match[2], match[3]
    else:
        raise ValueError(f"Invalid reference: {input_str}")


class SettingsConfig(BaseModel):
    cache_uri: str
    exec_uri: str


class ModelSourceType(str, Enum):
    LOCAL = "local"
    SUBMODEL = "submodel"
    CACHE = "cache"
    MMBSE = "mmbse"


class ModelSourceConfig(BaseModel):
    data_source: ModelSourceType
    source_url: str
    source_reference: str | None = None
    model_config = ConfigDict(use_enum_values=True)


class SubmodelSourceConfig(ModelSourceConfig):
    submodel_data: typing.Mapping[
        ModelReference, typing.Mapping[str, str | os.PathLike]
    ] = {}


class FileConfig(BaseModel):
    filename: Path | None = None
    reference: str | None = None

    def extract_system_model_input(self) -> tuple[str, str, str]:
        """Extract system, model and input name from a reference string"""
        if self.reference is None:
            return "", "", ""
        return extract_system_model_input(self.reference)

    model_config = ConfigDict(from_attributes=True, json_encoders={PurePosixPath: str})


class ModelConfig(BaseModel):
    exec_env: str
    source: str | None = None
    inputs: dict[str, FileConfig] = {}
    outputs: dict[str, FileConfig] = {}


class SystemConfig(BaseModel):
    source: str | None = None
    models: dict[str, ModelConfig]


@dataclass
class ModelStructure:
    models: dict[ModelReference, ModelConfig]
    inputs: dict[ModelReference, dict[str, pathlib.Path]]
    dependency_graph: dict[ModelReference, set[ModelReference]]
    execution_order: list[ModelReference]

    def get_model_dependencies(
        self,
        model_reference: ModelReference | Sequence[ModelReference],
        include_model=True,
    ) -> "ModelStructure":
        """Return a filtered ModelStructure with only dependencies on system and model"""
        # get dependencie list
        dep_list = []
        if isinstance(model_reference, ModelReference):
            model_reference = [model_reference]
        if include_model:
            work = [mr for mr in model_reference]
        else:
            work = []
            for mr in model_reference:
                work.extend(list(self.dependency_graph.get(mr, set())))
        while work:
            ref = work.pop()
            dep_list.append(ref)
            if ref in self.dependency_graph:
                work.extend(self.dependency_graph[ref])
        models = {k: v for k, v in self.models.items() if k in dep_list}
        inputs = {k: v for k, v in self.inputs.items() if k in dep_list}
        dependency_graph = {
            k: v for k, v in self.dependency_graph.items() if k in dep_list
        }
        execution_order = [k for k in self.execution_order if k in dep_list]

        return ModelStructure(
            models=models,
            inputs=inputs,
            dependency_graph=dependency_graph,
            execution_order=execution_order,
        )


class PymbseConfig(BaseModel):
    config: SettingsConfig
    sources: dict[str, ModelSourceConfig]
    execution_environments: dict[str, SerializeAsAny[ExecEnvironment]]
    default_model_source: str
    systems: dict[str, SystemConfig]

    @staticmethod
    def load_from_file(filepath: str | os.PathLike) -> "PymbseConfig":
        conf = yaml.load(open(filepath, "r"), Loader=yaml.BaseLoader)
        return PymbseConfig(**conf)

    @staticmethod
    def create_from_model_executions(
        model_executions: list[ModelExecution], settings: SettingsConfig
    ) -> "PymbseConfig":
        sources: dict[str, ModelSourceConfig] = {}
        default_model_source: str = "cache"
        execution_environments: dict[str, SerializeAsAny[ExecEnvironment]] = {}
        systems: dict[str, SystemConfig] = {}
        for me in model_executions:
            if me.exec_id not in sources:
                sources[me.exec_id] = ModelSourceConfig(
                    data_source=ModelSourceType.CACHE,
                    source_url=settings.cache_uri,
                    source_reference=me.exec_id,
                )

            exec_env_name = f"{me.model.env.name}_{me.model.env.version}"
            if exec_env_name not in execution_environments:
                execution_environments[exec_env_name] = me.model.env
            input_configs = {}
            output_configs = {}
            for inp in me.model.inputs:
                if isinstance(inp, ArtefactResource):
                    input_configs[inp.name] = FileConfig(filename=inp.name)
                elif isinstance(inp, ArtefactResourceRef):
                    input_configs[inp.name] = FileConfig(
                        filename=inp.ref_file_name,
                        reference=f"{inp.ref_system}.{inp.ref_model}.{inp.ref_name}",
                    )
            for outp in me.model.outputs:
                output_configs[outp.name] = FileConfig(filename=outp.name)

            config = ModelConfig(
                source=me.exec_id,
                exec_env=exec_env_name,
                inputs=input_configs,
                outputs=output_configs,
            )

            if me.model.system not in systems:
                systems[me.model.system] = SystemConfig(models={})
            systems[me.model.system].models[me.model.name] = config

        return PymbseConfig(
            config=settings,
            sources=sources,
            execution_environments=execution_environments,
            default_model_source=default_model_source,
            systems=systems,
        )

    def get_model(self, model_reference: ModelReference) -> ModelConfig:
        """Short cut to get a model from the config"""
        return self.systems[model_reference.system].models[model_reference.model]

    def get_source(self, model_reference: ModelReference) -> ModelSourceConfig:
        mod = self.get_model(model_reference)
        if mod.source:
            return self.sources[mod.source]
        sys = self.systems[model_reference.system]
        if sys.source:
            return self.sources[sys.source]
        return self.sources[self.default_model_source]

    def get_model_structure(self) -> ModelStructure:
        inputs: dict[ModelReference, dict[str, pathlib.Path]] = {}
        models: dict[ModelReference, ModelConfig] = {}

        graph: dict[ModelReference, set[ModelReference]] = {}

        for system_name, system in self.systems.items():
            for model_name, model in system.models.items():
                ref = ModelReference(system=system_name, model=model_name)
                graph[ref] = set()
                models[ref] = model
                inputs[ref] = {}
                for input_name, input in model.inputs.items() if model.inputs else []:
                    if input.filename:
                        inputs[ref][input_name] = pathlib.Path(input.filename)
                    if input.reference:
                        sys, mod, _ = extract_system_model_input(input.reference)
                        graph[ref].add(ModelReference(system=sys, model=mod))

        ts = graphlib.TopologicalSorter(graph)

        model_order = [*ts.static_order()]

        return ModelStructure(models, inputs, graph, model_order)

    def to_cache_model(self, model_reference: ModelReference) -> Model:
        model = self.get_model(model_reference)
        exec_env = self.execution_environments[model.exec_env]
        inputs = []
        outputs = []
        for name, inp in model.inputs.items():
            if inp.reference:
                sys, mod, inp_name = extract_system_model_input(inp.reference)
                ref_filename = None
                if inp.filename:
                    ref_filename = pathlib.Path(inp.filename).name
                inputs.append(
                    ArtefactResourceRef(
                        name=name,
                        ref_system=sys,
                        ref_model=mod,
                        ref_name=inp_name,
                        ref_file_name=ref_filename,
                    )
                )
            else:
                if not inp.filename:
                    raise ValueError(f"Input {name} has neither reference nor filename")
                fn_path = pathlib.Path(inp.filename)
                suffix = fn_path.suffix
                res_type = ResourceType.infer_type(suffix)
                inputs.append(ArtefactResource(name=name, resource_type=res_type))

        for name, outp in model.outputs.items():
            if not outp.filename:
                raise ValueError(f"Output {name} has no filename")
            fn_path = pathlib.Path(outp.filename)
            suffix = fn_path.suffix
            res_type = ResourceType.infer_type(suffix)
            outputs.append(ArtefactResource(name=name, resource_type=res_type))

        return Model(
            name=model_reference.model,
            system=model_reference.system,
            env=exec_env,
            inputs=inputs,
            outputs=outputs,
        )


if __name__ == "__main__":
    import pprint

    config = PymbseConfig.load_from_file(pathlib.Path("testconfig.yaml"))

    pprint.pprint(config)
