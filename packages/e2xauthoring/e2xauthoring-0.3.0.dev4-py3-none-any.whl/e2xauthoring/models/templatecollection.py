import glob
import os
from typing import Dict

from nbgrader.coursedir import CourseDirectory
from traitlets import Unicode
from traitlets.config import LoggingConfigurable

from ..dataclasses import TemplateCollectionRecord
from .template import Template


class TemplateCollection(LoggingConfigurable):
    directory = Unicode("templates", help="Directory where templates are stored").tag(
        config=True
    )

    templates: Dict[str, Template]
    coursedir: CourseDirectory
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(TemplateCollection, cls).__new__(cls)
        return cls._instance

    def __init__(self, coursedir: CourseDirectory):
        self.coursedir = coursedir
        self.templates = dict()
        self.init_templates()

    @property
    def template_path(self):
        return self.coursedir.format_path(self.directory, ".", ".")

    def __getitem__(self, key):
        return self.templates[key]

    def __contains__(self, key):
        return key in self.templates

    def get_template_paths(self):
        paths = glob.glob(os.path.join(self.template_path, "*"))
        return [os.path.basename(path) for path in paths if os.path.isdir(path)]

    def init_template(self, template_name: str):
        if template_name not in self.templates:
            self.templates[template_name] = Template(
                name=template_name, base_path=self.template_path
            )

    def init_templates(self):
        template_names = self.get_template_paths()
        for template_name in template_names:
            self.init_template(template_name)

    def update_templates(self):
        template_names = self.get_template_paths()
        deleted_templates = set(self.templates.keys()) - set(template_names)
        for template_name in deleted_templates:
            self.templates.pop(template_name)
        added_templates = set(template_names) - set(self.templates.keys())
        for template_name in added_templates:
            self.init_template(template_name)

    def add_template(self, name: str):
        template_path = os.path.join(self.template_path, name)
        assert not os.path.exists(
            template_path
        ), f"Template {name} already exists in templates"
        template = Template.create(name=name, base_path=self.template_path)
        self.templates[name] = template

    def remove_template(self, name: str):
        assert name in self.templates, f"Template {name} does not exist in templates"
        template = self.templates.get(name)
        template.remove()
        del self.templates[name]

    def copy_template(self, name: str, new_name: str):
        assert name in self.templates, f"Template {name} does not exist in templates"
        template = self.templates.get(name)
        new_template = template.copy(new_name)
        self.templates[new_name] = new_template

    def to_dataclass(self) -> TemplateCollectionRecord:
        self.update_templates()
        return TemplateCollectionRecord(
            templates=[template.to_dataclass() for template in self.templates.values()]
        )

    def to_json(self):
        return self.to_dataclass().to_json()
