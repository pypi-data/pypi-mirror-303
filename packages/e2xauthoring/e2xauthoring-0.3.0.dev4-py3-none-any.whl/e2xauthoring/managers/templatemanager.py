from ..models import TemplateCollection
from .base import BaseManager


class TemplateManager(BaseManager):
    templates: TemplateCollection

    def __init__(self, coursedir):
        self.templates = TemplateCollection(coursedir)

    def get(self, name: str):
        assert name in self.templates, f"The template {name} does not exist."
        return self.templates[name].to_json()

    def create(self, name: str):
        self.templates.add_template(name)

    def remove(self, name: str):
        self.templates.remove_template(name)

    def list(self):
        return self.templates.to_json()["templates"]

    def list_variables(self, name):
        assert name in self.templates, f"The template {name} does not exist."
        return self.templates[name].list_variables()

    def copy(self, old_name: str, new_name: str):
        self.templates.copy_template(old_name, new_name)
