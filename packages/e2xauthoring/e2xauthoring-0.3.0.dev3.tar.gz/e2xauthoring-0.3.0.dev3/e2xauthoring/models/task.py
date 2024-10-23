import os
import shutil
import time
from typing import Dict

import nbformat
from e2xcore.utils.nbgrader_cells import get_points, is_grade, new_read_only_cell
from jupyter_client.kernelspec import KernelSpecManager

from ..dataclasses import GitStatus, TaskRecord
from ..git import GitRepo
from ..patterns import Observer
from ..utils.pathutils import list_files


def new_task_notebook(
    name: str, kernel_name: str = None
) -> nbformat.notebooknode.NotebookNode:
    metadata = dict(nbassignment=dict(type="task"))
    if kernel_name is not None:
        kernel_spec = KernelSpecManager().get_kernel_spec(kernel_name)
        metadata["kernelspec"] = dict(
            name=kernel_name,
            display_name=kernel_spec.display_name,
            language=kernel_spec.language,
        )
    nb = nbformat.v4.new_notebook(metadata=metadata)
    cell = new_read_only_cell(
        grade_id=f"{name}_Header",
        source=(
            f"# {name}\n"
            "Here you should give a brief description of the task.\n"
            "Then add questions via the menu above.\n"
            "A task should be self contained and not rely on other tasks."
        ),
    )
    nb.cells.append(cell)
    return nb


class Task(Observer):
    name: str
    pool: str
    path: str
    n_questions: int
    points: int
    git_status: Dict[str, str]
    last_modified: float
    last_updated: float
    repo: GitRepo

    def __init__(self, name: str, pool: str, base_path: str, repo: GitRepo):
        self.name = name
        self.pool = pool
        self.path = os.path.join(base_path, pool, name)
        self.repo = repo
        self.repo.attach(self)
        self.last_modified = 0
        self.last_updated = self.repo.last_full_update
        self.update_task_info()
        self.full_git_status = self.repo.get_status_of_path(self.path)
        self.file_dict = list_files(self.path)

    def update(self, subject: GitRepo):
        self.last_updated = subject.last_full_update
        self.full_git_status = subject.get_status_of_path(self.path)
        self.file_dict = list_files(self.path)

    @property
    def git_status(self):
        if not self.repo.is_version_controlled:
            return dict(status="not version controlled")
        elif (
            len(
                self.full_git_status.unstaged
                + self.full_git_status.staged
                + self.full_git_status.untracked
            )
            > 0
        ):
            return dict(status="modified")
        else:
            return dict(status="unchanged")

    def check_for_changes(self):
        current_file_dict = list_files(self.path)
        if set(current_file_dict.items()) != set(self.file_dict.items()):
            self.repo.update_status()
        elif self.last_updated < self.repo.last_full_update:
            self.update(self.repo)

    @staticmethod
    def create(
        name: str, pool: str, base_path: str, repo: GitRepo, kernel_name: str = None
    ):
        task_path = os.path.join(base_path, pool, name)
        assert not os.path.exists(
            task_path
        ), f"Task {name} already exists in pool {pool}"
        os.makedirs(os.path.join(task_path, "data"), exist_ok=True)
        os.makedirs(os.path.join(task_path, "img"), exist_ok=True)
        nb = new_task_notebook(name, kernel_name)
        nbformat.write(nb, os.path.join(task_path, f"{name}.ipynb"))
        # Sleep to ensure that the file is written before the repo is updated
        time.sleep(0.5)

        return Task(name, pool, base_path, repo)

    def remove(self):
        task_path = self.path
        assert os.path.exists(
            task_path
        ), f"Task {self.name} does not exist in pool {self.pool}"
        shutil.rmtree(task_path)
        self.repo.detach(self)
        self.repo.update_status()

    def copy(self, new_name: str):
        old_path = self.path
        new_path = os.path.join(os.path.dirname(old_path), new_name)
        assert not os.path.exists(new_path), f"Task {new_name} already exists"
        shutil.copytree(old_path, new_path)
        shutil.move(
            os.path.join(new_path, f"{self.name}.ipynb"),
            os.path.join(new_path, f"{new_name}.ipynb"),
        )
        nb = nbformat.read(
            os.path.join(new_path, f"{new_name}.ipynb"), as_version=nbformat.NO_CONVERT
        )
        for cell in nb.cells:
            if is_grade(cell):
                cell.source = cell.source.replace(self.name, new_name)
                cell.metadata.nbgrader.grade_id = (
                    cell.metadata.nbgrader.grade_id.replace(self.name, new_name)
                )
        nbformat.write(nb, os.path.join(new_path, f"{new_name}.ipynb"))
        self.repo.update_status()
        return Task(new_name, self.pool, os.path.dirname(old_path), self.repo)

    def rename(self, new_name: str):
        old_path = self.path
        new_path = os.path.join(os.path.dirname(old_path), new_name)
        assert not os.path.exists(new_path), f"Task {new_name} already exists"
        shutil.move(old_path, new_path)
        self.path = new_path
        self.name = new_name
        self.repo.update_status()

    @property
    def notebook_file(self):
        return os.path.join(self.path, f"{self.name}.ipynb")

    @property
    def data_path(self):
        return os.path.join(self.path, "data")

    @property
    def image_path(self):
        return os.path.join(self.path, "img")

    @property
    def notebook_file_exists(self):
        return os.path.isfile(self.notebook_file)

    @property
    def is_dirty(self):
        if self.notebook_file_exists:
            return self.last_modified < os.path.getmtime(self.notebook_file)
        return False

    def update_task_info(self):
        if self.is_dirty:
            nb = nbformat.read(self.notebook_file, as_version=nbformat.NO_CONVERT)
            last_modified = os.path.getmtime(self.notebook_file)
            if self.last_modified < last_modified:
                points = [get_points(cell) for cell in nb.cells if is_grade(cell)]
                self.points = sum(points)
                self.n_questions = len(points)
                self.last_modified = last_modified

    def to_dataclass(self, include_git_status=False) -> TaskRecord:
        if self.is_dirty:
            self.update_task_info()
        status = GitStatus(
            status=self.git_status["status"],
        )
        if include_git_status:
            self.check_for_changes()
            status = GitStatus(
                status=self.git_status["status"],
                staged=self.full_git_status.staged,
                unstaged=self.full_git_status.unstaged,
                untracked=self.full_git_status.untracked,
            )
        return TaskRecord(
            name=self.name,
            pool=self.pool,
            points=self.points,
            n_questions=self.n_questions,
            git_status=status,
        )

    def to_json(self, include_git_status=False):
        return self.to_dataclass(include_git_status).to_json()
