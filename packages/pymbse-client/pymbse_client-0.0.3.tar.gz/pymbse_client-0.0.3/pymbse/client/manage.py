# SPDX-FileCopyrightText: 2024 CERN
#
# SPDX-License-Identifier: BSD-4-Clause

import os
import pathlib
import time
import typing
from graphlib import TopologicalSorter

from tqdm.auto import tqdm

from pymbse.client.cache import PymbseCache, PymbseExec
from pymbse.client.config import (
    FileConfig,
    ModelConfig,
    ModelSourceConfig,
    ModelSourceType,
    ModelStructure,
    PymbseConfig,
    SubmodelSourceConfig,
    SystemConfig,
)
from pymbse.commons.schemas import (
    ExecutionJob,
    ModelExecutionReference,
    ModelReference,
)


class ExecutionError(RuntimeError):
    def __init__(self, *args, job: ExecutionJob, ref: ModelExecutionReference) -> None:
        super().__init__(*args)
        self.job = job
        self.ref = ref


class ModelSourceHandler:
    def __init__(self, source: ModelSourceConfig) -> None:
        self.source = source
        pass

    @staticmethod
    def create(source: ModelSourceConfig) -> "ModelSourceHandler":
        return ModelSourceHandler(source)


class ProgressTracker:
    def __init__(self) -> None:
        self.models_to_run: list[ModelReference] = []
        self.models_running: list[ModelReference] = []
        self.models_finished: list[ModelReference] = []
        self.models_skipped: list[ModelReference] = []

    def setup(self, models_to_run: list[ModelReference]) -> None:
        self.models_to_run = models_to_run
        self.models_running = []
        self.models_finished = []
        self.models_skipped = []

    def job_update(self, model: ModelReference, job: ExecutionJob) -> None:
        pass

    def close(self) -> None:
        pass

    def start(self, models: list[ModelReference]) -> None:
        pass

    def skip(self, models: list[ModelReference]) -> None:
        pass

    def success(self, models: list[ModelReference]) -> None:
        pass

    def fail(self, models: list[ModelReference]) -> None:
        pass


class TQDMProgressTracker(ProgressTracker):
    def __init__(self) -> None:
        super().__init__()
        self.pbar = None

    def setup(self, models_to_run: list[ModelReference]) -> None:
        super().setup(models_to_run)
        self.pbar = tqdm(total=len(self.models_to_run))

    def close(self) -> None:
        super().close()
        if self.pbar is not None:
            self.pbar.close()

    def start(self, models: list[ModelReference]) -> None:
        super().start(models)
        if self.pbar is not None:
            active_jobs = ", ".join([f"{job.system}.{job.model}" for job in models])
            self.pbar.set_description(f"Running models: {active_jobs}")

    def skip(self, models: list[ModelReference]) -> None:
        super().skip(models)
        for node in models:
            tqdm.write(f"Using existing exection for Model {node.system}.{node.model}")
        if self.pbar is not None:
            self.pbar.update(len(models))

    def success(self, models: list[ModelReference]) -> None:
        super().success(models)
        for job in models:
            tqdm.write(
                f"Execution of Model {job.system}.{job.model} finished successfully"
            )
        if self.pbar is not None:
            self.pbar.update(len(models))

    def fail(self, models: list[ModelReference]) -> None:
        super().fail(models)
        for job in models:
            tqdm.write(f"Execution of Model {job.system}.{job.model} failed.")
        if self.pbar is not None:
            self.pbar.update(len(models))


class PymbseManage:
    """Class to handle global actions with Pymbse
    - Storing and loading models from external sources
    - Creation of models
    - Synchorization with cache
    """

    def __init__(
        self,
        config: PymbseConfig,
    ) -> None:
        self.config = config
        self.cache = PymbseCache(config.config.cache_uri)
        self.exec = PymbseExec(config.config.exec_uri)
        self.progress_tracker: ProgressTracker = TQDMProgressTracker()

    @staticmethod
    def create(config_path: str | os.PathLike) -> "PymbseManage":
        return PymbseManage(PymbseConfig.load_from_file(config_path))

    def set_progress_tracker(self, value: ProgressTracker) -> None:
        self.progress_tracker = value

    def setup_cache_models(self, model_structure: ModelStructure | None = None) -> None:
        if model_structure is None:
            model_structure = self.config.get_model_structure()
        update_list = [
            self.config.to_cache_model(model)
            for model in model_structure.execution_order
        ]
        self.cache.update_models(update_list)

    def clear_cache(self) -> None:
        self.cache.clear_all()

    def run_model_dependencies(
        self,
        model_reference: ModelReference,
        include_model: bool = False,
        force_all: bool = False,
    ) -> str:
        """Run all models for given dependency

        Create a ExecutionJob for all models in the structure which depend on the given model_reference,
        schedule models by dependencies and execute them.

        :param model_reference: model reference
        :type model_reference: ModelReference
        :param include_model: Also run (system,model) itself
        :type include_model: bool
        :param force_all: Force all executions (even if no input changed)
        :type force_all: bool
        :return: Execution reference
        :rtype: str
        """
        structure = self.config.get_model_structure().get_model_dependencies(
            model_reference, include_model
        )
        self.setup_cache_models(structure)

        return self.run_models(structure, force_all)

    def run_in_environment(
        self,
        base_model: ModelReference,
        files: typing.Mapping[str, str | os.PathLike],
        exec_environment: str,
        force_execution: bool = False,
    ) -> ModelExecutionReference:
        generic_model_name = f"{base_model.system}_{base_model.model}_{exec_environment}_{'_'.join(files.keys())}"
        generic_system_name = "Generic_executions"
        if generic_system_name not in self.config.systems:
            self.config.systems[generic_system_name] = SystemConfig(models={})
        self.config.systems[generic_system_name].models[generic_model_name] = (
            ModelConfig(
                exec_env=exec_environment,
                inputs={
                    name: FileConfig(filename=pathlib.Path())
                    for name, filename in files.items()
                },
            )
        )
        subref = ModelReference(system=generic_system_name, model=generic_model_name)

        exec_refs = self.run_submodels(
            base_model, [subref], {subref: files}, force_execution
        )
        return exec_refs[0]

    def run_submodels(
        self,
        base_model: ModelReference,
        submodels: list[ModelReference],
        files: dict[ModelReference, typing.Mapping[str, str | os.PathLike]],
        force_execution: bool = False,
    ) -> list[ModelExecutionReference]:
        structure = self.config.get_model_structure().get_model_dependencies(
            submodels, True
        )
        submod_conf_name = f"submodel_{base_model.system}_{base_model.model}"
        self.config.sources[submod_conf_name] = SubmodelSourceConfig(
            data_source=ModelSourceType.SUBMODEL,
            source_url="",
            source_reference=f"{base_model.system}_{base_model.model}",
            submodel_data=files,
        )
        for _ref, mod in structure.models.items():
            mod.source = submod_conf_name
        # Store the files
        self.setup_cache_models(structure)
        execution_ref = self.run_models(structure, force_execution)

        return [
            ModelExecutionReference(
                execution=execution_ref, model=ref.model, system=ref.system
            )
            for ref in submodels
        ]

    def run_models(self, structure: ModelStructure, force_all: bool = False) -> str:
        """Run all models for the given modelStructure

        Create a ExecutionJob for all models in the structure, schedule models by
        dependencies and execute them.

        :param structure: model structure
        :type structure: ModelStructure
        :param force_all: Force all executions (even if no input changed)
        :type force_all: bool
        :return: Execution reference
        :rtype: str
        """
        executions = self.cache.create_executions(structure.execution_order)
        execution_ref = executions[0].execution  # All have the same reference

        exec_dict = {
            modref: exec_ref
            for modref, exec_ref in zip(structure.execution_order, executions)
        }
        jobs = {}

        ts = TopologicalSorter(structure.dependency_graph)
        ts.prepare()
        active_jobs: list[ModelReference] = []
        self.progress_tracker.setup(structure.execution_order)
        try:
            while ts.is_active():
                for node in ts.get_ready():
                    _exec, output = self.init_upload_run(exec_dict[node], force_all)
                    if output.status == "SKIPPED":
                        self.progress_tracker.skip([node])
                        ts.done(node)
                    else:
                        jobs[node] = output
                active_jobs_new = list(jobs.keys())
                if active_jobs_new != active_jobs:
                    active_jobs = active_jobs_new
                    self.progress_tracker.start([node for node in jobs])

                wait_on_job = False
                finished_jobs = []
                for job in jobs:
                    if jobs[job].status == "SUCCESS":
                        self.cache.forward_outputs(exec_dict[job])
                        ts.done(job)
                        self.progress_tracker.success([job])
                        finished_jobs.append(job)
                    elif jobs[job].status == "FAILURE":
                        self.progress_tracker.fail([job])
                        self.on_execution_error(jobs[job], exec_dict[job])
                    else:
                        jobs[job] = self.exec.get_status(jobs[job])
                        self.progress_tracker.job_update(job, jobs[job])
                        wait_on_job = True
                for job in finished_jobs:
                    del jobs[job]
                if wait_on_job:
                    time.sleep(1)
        finally:
            self.progress_tracker.close()

        return execution_ref

    def on_execution_error(self, job: ExecutionJob, reference: ModelExecutionReference):
        # Todo, print nice exception handling
        raise ExecutionError(f"Execution of {reference} failed", job=job, ref=reference)

    def init_upload_run(
        self, reference: ModelReference, force_execution: bool = False
    ) -> tuple[ModelExecutionReference, ExecutionJob]:
        if isinstance(reference, ModelExecutionReference):
            model_execution = reference
        else:
            model_execution = self.cache.create_execution(reference).get_reference()

        model_conf = self.config.get_model(reference)
        source = self.config.get_source(reference)
        if source.data_source == ModelSourceType.LOCAL:
            # upload from local file system
            source_top_path = pathlib.Path(source.source_url)
            model_path = source_top_path / reference.system / reference.model
            for inp_name, inp in model_conf.inputs.items():
                # References are pushed via cache automatically
                if not inp.reference:
                    if not inp.filename:
                        raise ValueError(
                            f"Input {inp_name} has neither reference nor filename"
                        )
                    file_path = model_path / inp.filename

                    self.cache.upload_input(model_execution, inp_name, file_path)

        elif source.data_source == ModelSourceType.CACHE:
            # All input files should be uploaded already, otherwise we don't know where to retreive them
            pass
        elif source.data_source == ModelSourceType.MMBSE:
            # Synchronize with MMBSE DB, load execution, upload to cache
            pass
        elif source.data_source == ModelSourceType.SUBMODEL:
            submod_source = typing.cast(SubmodelSourceConfig, source)
            model_ref = ModelReference(system=reference.system, model=reference.model)
            for name, filepath in submod_source.submodel_data.get(
                model_ref, {}
            ).items():
                self.cache.upload_input(model_execution, name, filepath)

        self.cache.lock_inputs(model_execution)
        # Check if need to be run
        exec_past = None
        if not force_execution:
            exec_past = self.cache.link_from_existing_exec(model_execution)
        if exec_past:
            return model_execution, ExecutionJob(
                id=exec_past.execution, status="SKIPPED"
            )
        else:
            exec_env = self.config.execution_environments[model_conf.exec_env]
            return model_execution, self.exec.execute_model(model_execution, exec_env)

    def load_external_sources(self):
        pass

    def store_external_sources(self):
        pass
