import os
import shutil

import nbformat
from e2xcore.utils.nbgrader_cells import new_read_only_cell
from nbformat.v4 import new_notebook

from ..dataclasses import TemplateRecord
from ..utils.notebookvariableextractor import NotebookVariableExtractor


class Template:
    name: str
    path: str

    def __init__(self, name: str, base_path: str):
        self.name = name
        self.path = os.path.join(base_path, name)

    @property
    def notebook_file(self):
        return os.path.join(self.path, f"{self.name}.ipynb")

    @staticmethod
    def create(name: str, base_path: str) -> "Template":
        path = os.path.join(base_path, name)
        assert not os.path.exists(path), f"Template {name} already exists"
        os.makedirs(path, exist_ok=True)
        nb = new_notebook(metadata=dict(nbassignment=dict(type="template")))
        cell = new_read_only_cell(
            grade_id="HeaderA",
            source=(
                "### This is a header cell\n\n"
                "It will always appear at the top of the notebook"
            ),
        )
        cell.metadata["nbassignment"] = dict(type="header")
        nb.cells.append(cell)
        nbformat.write(nb, os.path.join(path, f"{name}.ipynb"))
        return Template(name=name, base_path=base_path)

    def remove(self):
        assert os.path.exists(self.path), f"The template {self.name} does not exist."
        shutil.rmtree(self.path)

    def copy(self, new_name: str):
        new_template_path = os.path.join(os.path.dirname(self.path), new_name)
        assert not os.path.exists(
            new_template_path
        ), f"Template {new_name} already exists"
        shutil.copytree(self.path, new_template_path)
        os.rename(
            os.path.join(new_template_path, f"{self.name}.ipynb"),
            os.path.join(new_template_path, f"{new_name}.ipynb"),
        )
        return Template(name=new_name, base_path=os.path.dirname(self.path))

    def rename(self, new_name: str):
        new_template_path = os.path.join(os.path.dirname(self.path), new_name)
        assert not os.path.exists(
            new_template_path
        ), f"Template {new_name} already exists"
        os.rename(self.path, new_template_path)
        old_notebook_file = self.notebook_file
        new_notebook_file = os.path.join(
            os.path.dirname(old_notebook_file), f"{new_name}.ipynb"
        )
        os.rename(old_notebook_file, new_notebook_file)
        self.name = new_name
        self.path = new_template_path

    def list_variables(self):
        assert os.path.exists(
            self.notebook_file
        ), f"The template {self.name} does not exist."
        return NotebookVariableExtractor().extract(self.notebook_file)

    def to_dataclass(self) -> TemplateRecord:
        return TemplateRecord(name=self.name, variables=self.list_variables())

    def to_json(self):
        return self.to_dataclass().to_json()
