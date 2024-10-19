# SPDX-FileCopyrightText: 2024 CERN
#
# SPDX-License-Identifier: BSD-4-Clause

import os
import pathlib
import re
from typing import Mapping

from requests_toolbelt import sessions

from pymbse.commons.schemas import (
    ExecEnvironment,
    ExecutionJob,
    Model,
    ModelExecution,
    ModelExecutionReference,
    ModelReference,
    ModelSource,
    System,
)


class PymbseExec:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.session = sessions.BaseUrlSession(base_url)

    def execute_model(
        self,
        execution_reference: ModelExecutionReference,
        execution_env: ExecEnvironment,
        model_source: ModelSource | None = None,
    ) -> ExecutionJob:
        json = {
            "execution_reference": execution_reference.model_dump(),
            "execution_env": execution_env.model_dump(),
        }
        if model_source:
            json["mod_source"] = model_source.model_dump()
        response = self.session.post(
            "/executions/start",
            json=json,
        )
        response.raise_for_status()
        return ExecutionJob(**response.json())

    def get_status(self, job: ExecutionJob) -> ExecutionJob:
        response = self.session.get(f"executions/status/{job.id}")
        response.raise_for_status()
        return ExecutionJob(**response.json())


class PymbseCache:
    re_file_content_dis = re.compile(
        r"([^;]+); filename=\"([^\"]+)\"; content-type=\"([^\"]+)\""
    )

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.session = sessions.BaseUrlSession(base_url)

    def _modelref_path(self, model_reference: ModelReference) -> str:
        return f"/systems/{model_reference.system}/models/{model_reference.model}"

    def _executionref_path(self, execution_reference: ModelExecutionReference) -> str:
        return f"{self._modelref_path(execution_reference)}/executions/{execution_reference.execution}"

    def _execution_path(self, model_execution: ModelExecution) -> str:
        return self._executionref_path(model_execution.get_reference())

    def create_model(self, model: Model) -> None:
        response = self.session.post(
            f"/systems/{model.system}/models",
            json=model.model_dump(),
        )
        response.raise_for_status()

    def update_models(self, models: list[Model]) -> None:
        response = self.session.patch(
            "/systems/update_models", json=[m.model_dump() for m in models]
        )
        response.raise_for_status()

    def delete_model(self, model_reference: ModelReference) -> None:
        response = self.session.delete(self._modelref_path(model_reference))
        response.raise_for_status()

    def get_systems(self) -> list[System]:
        response = self.session.get("/systems")
        response.raise_for_status()
        return [System(**x) for x in response.json()]

    def get_models(self, system_name: str) -> list[Model]:
        response = self.session.get(f"/systems/{system_name}/models")
        response.raise_for_status()
        return [Model(**x) for x in response.json()]

    def find_model(self, model_reference: ModelReference) -> Model | None:
        response = self.session.get(self._modelref_path(model_reference))
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return Model(**response.json())

    def clear_all(self):
        """Clear cache"""
        for system in self.get_systems():
            self.clear_system(system.name)

    def clear_system(self, system_name: str):
        response = self.session.delete(f"/systems/{system_name}")
        response.raise_for_status()
        """Clear system cache"""

    def clear_model(self, model: ModelReference):
        """Clear model cache"""
        response = self.session.delete(f"/systems/{model.system}/models/{model.model}")
        response.raise_for_status()

    def clear_exectuions(self, model: ModelReference):
        response = self.session.delete(f"{self._modelref_path(model)}/executions")
        response.raise_for_status()

    def clear_all_executions(self):
        for system in self.get_systems():
            for model in self.get_models(system.name):
                self.clear_exectuions(model.get_reference())

    def get_execution(
        self, execution_reference: ModelExecutionReference
    ) -> ModelExecution:
        response = self.session.get(self._executionref_path(execution_reference))
        response.raise_for_status()
        return ModelExecution(**response.json())

    def get_uploaded_inputs(
        self, execution_reference: ModelExecutionReference
    ) -> list[str]:
        response = self.session.get(
            f"{self._executionref_path(execution_reference)}/inputs"
        )
        response.raise_for_status()
        return response.json()

    def get_uploaded_outputs(
        self, execution_reference: ModelExecutionReference
    ) -> list[str]:
        response = self.session.get(
            f"{self._executionref_path(execution_reference)}/outputs"
        )
        response.raise_for_status()
        return response.json()

    def _download_file(
        self,
        execution_reference: ModelExecutionReference,
        i_o: str,
        name: str,
        output_dir: str | os.PathLike,
        fname: str | os.PathLike | None = None,
    ):
        response = self.session.get(
            f"{self._executionref_path(execution_reference)}/{i_o}/{name}"
        )
        response.raise_for_status()

        if fname is None:
            if d := response.headers.get("content-disposition", None):
                if match := self.re_file_content_dis.match(d):
                    rel_path_file = pathlib.Path(
                        match[2]
                    )  # [attachment,<filename>,<content-type>]
                else:
                    raise ValueError(
                        f"Cannot parse content-disposition: {d}. Format changed?"
                    )
            else:
                rel_path_file = pathlib.Path(name)
        else:
            rel_path_file = pathlib.Path(fname)

        filepath = pathlib.Path(output_dir) / rel_path_file
        with open(filepath, "wb") as f:
            f.write(response.content)
        return filepath

    def download_input(
        self,
        execution_reference: ModelExecutionReference,
        name: str,
        output_dir: str | os.PathLike,
        fname: str | os.PathLike | None = None,
    ) -> pathlib.Path:
        return self._download_file(
            execution_reference, "inputs", name, output_dir, fname
        )

    def download_output(
        self,
        execution_reference: ModelExecutionReference,
        name: str,
        output_dir: str | os.PathLike,
        fname: str | os.PathLike | None = None,
    ) -> pathlib.Path:
        return self._download_file(
            execution_reference, "outputs", name, output_dir, fname
        )

    def download_inputs(
        self, model_execution: ModelExecution, output_dir: os.PathLike
    ) -> dict[str, pathlib.Path]:
        inputs = {}
        alternative_filenames = model_execution.model.get_alternative_filenames()
        for input in model_execution.inputs:
            inputs[input] = self.download_input(
                model_execution.get_reference(),
                input,
                output_dir,
                alternative_filenames.get(input, None),
            )
        return inputs

    def download_outputs(
        self,
        execution_reference: ModelExecutionReference,
        output_dir: str | os.PathLike,
    ) -> dict[str, pathlib.Path]:
        outputs = {}
        for output in self.get_uploaded_outputs(execution_reference):
            outputs[output] = self.download_output(
                execution_reference,
                output,
                output_dir,
                None,
            )
        return outputs

    def upload_outputs(
        self,
        execution_reference: ModelExecutionReference,
        outputs: Mapping[str, str | os.PathLike],
        lock: bool = True,
        allow_unfinished: bool = False,
    ) -> None:
        for name, out_path in outputs.items():
            self.upload_output(execution_reference, name, out_path)
        if lock:
            self.lock_outputs(execution_reference, allow_unfinished=allow_unfinished)

    def upload_inputs(
        self,
        execution_reference: ModelExecutionReference,
        inputs: Mapping[str, str | os.PathLike],
    ) -> None:
        for name, in_path in inputs.items():
            self.upload_input(execution_reference, name, in_path)

    def upload_input(
        self,
        execution_ref: ModelExecutionReference,
        name: str,
        filepath: str | os.PathLike,
    ) -> None:
        response = self.session.post(
            f"{self._executionref_path(execution_ref)}/inputs/{name}",
            files={"file": open(filepath, "rb")},
        )
        response.raise_for_status()

    def upload_output(
        self,
        execution_ref: ModelExecutionReference,
        name: str,
        filepath: str | os.PathLike,
    ):
        response = self.session.post(
            f"{self._executionref_path(execution_ref)}/outputs/{name}",
            files={"file": open(filepath, "rb")},
        )
        response.raise_for_status()

    def lock_outputs(
        self,
        execution_reference: ModelExecutionReference,
        forward_outputs: bool = True,
        allow_unfinished: bool = False,
    ) -> None:
        response = self.session.post(
            f"{self._executionref_path(execution_reference)}/lock_outputs?allow_unfinished={allow_unfinished}&forward_outputs={forward_outputs}",
        )
        response.raise_for_status()

    def forward_outputs(
        self,
        execution_reference: ModelExecutionReference,
        additional_execution_ids: list[str] | None = None,
        additional_references: list[ModelExecutionReference] | None = None,
    ) -> None:
        json_dict = {}
        if additional_execution_ids:
            json_dict["additional_execution_ids"] = additional_execution_ids
        if additional_references:
            json_dict["additional_references"] = [
                ref.model_dump() for ref in additional_references
            ]
        response = self.session.post(
            f"{self._executionref_path(execution_reference)}/create_output_refs",
            json=json_dict,
        )
        response.raise_for_status()

    def lock_inputs(
        self,
        execution_reference: ModelExecutionReference,
        ignore_missing: bool = False,
        ignore_locked: bool = False,
    ) -> str:
        response = self.session.post(
            f"{self._executionref_path(execution_reference)}/lock_inputs?ignore_missing={ignore_missing}&ignore_locked={ignore_locked}",
        )
        response.raise_for_status()
        return response.json()

    def link_from_existing_exec(
        self, execution_reference: ModelExecutionReference
    ) -> ModelExecutionReference | None:
        response = self.session.post(
            f"{self._executionref_path(execution_reference)}/link_from_past_executions"
        )
        response.raise_for_status()
        json = response.json()
        if json:
            return ModelExecutionReference(**json)
        return None

    def create_execution(
        self, model: ModelReference, exec_id: str | None = None
    ) -> ModelExecution:
        if exec_id:
            add_exec_id = f"?existing_exec_id={exec_id}"
        else:
            add_exec_id = ""
        response = self.session.post(
            f"{self._modelref_path(model)}/executions{add_exec_id}",
        )
        response.raise_for_status()
        return ModelExecution(**response.json())

    def create_executions(
        self, models: list[ModelReference]
    ) -> list[ModelExecutionReference]:
        response = self.session.post(
            "/executions/create",
            json={"filter_models": [m.model_dump() for m in models]},
        )
        response.raise_for_status()
        executions = [ModelExecutionReference(**x) for x in response.json()]
        return executions
