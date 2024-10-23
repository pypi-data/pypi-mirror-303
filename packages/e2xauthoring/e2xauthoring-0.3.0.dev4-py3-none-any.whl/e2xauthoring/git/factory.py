import os
from typing import Dict

from ..utils.pathutils import is_parent_path
from .gitrepo import GitRepo


class GitRepoFactory:
    _instances: Dict[str, GitRepo] = dict()

    @staticmethod
    def get_instance(path: str) -> GitRepo:
        path = os.path.abspath(path)
        if path in GitRepoFactory._instances:
            return GitRepoFactory._instances[path]
        for existing_path in GitRepoFactory._instances.keys():
            if is_parent_path(existing_path, path):
                return GitRepoFactory._instances[existing_path]
        instance = GitRepo(path)
        if instance.is_version_controlled:
            GitRepoFactory._instances[instance.repo.working_tree_dir] = instance
        else:
            GitRepoFactory._instances[path] = instance
        return instance

    @staticmethod
    def remove_instance(path: str) -> None:
        path = os.path.abspath(path)
        if path in GitRepoFactory._instances:
            del GitRepoFactory._instances[path]

    @staticmethod
    def remove_all_instances() -> None:
        GitRepoFactory._instances = dict()
