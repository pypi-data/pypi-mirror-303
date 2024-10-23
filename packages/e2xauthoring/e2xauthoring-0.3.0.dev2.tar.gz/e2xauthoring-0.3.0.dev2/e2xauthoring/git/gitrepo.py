import os
import shutil

from git import Actor

from ..dataclasses import GitStatus
from ..utils.pathutils import is_parent_path
from .base import BaseRepo

GITIGNORE = ".gitignore"
HERE = os.path.dirname(os.path.abspath(__file__))


class GitRepo(BaseRepo):
    def _copy_gitignore(self):
        here = os.path.dirname(__file__)
        shutil.copy(
            os.path.join(here, "..", "assets", GITIGNORE),
            os.path.join(self.path, GITIGNORE),
        )

    def initialize_repo(self, exist_ok: bool = True, author: Actor = None):
        """
        Initializes a Git repository.
        """
        if not exist_ok and self.is_version_controlled:
            raise ValueError(
                f"A repository already exists at {self.repo.working_tree_dir}"
            )
        self._copy_gitignore()
        super().initialize_repo()
        self.commit(
            path=os.path.join(self.path, GITIGNORE),
            message="Add .gitignore",
            add_if_untracked=True,
            author=author,
        )

    def get_status_of_path(self, path: str) -> GitStatus:
        """
        Returns the GitStatus of the specified path.

        Args:
            path (str): The path to check the status of.

        Returns:
            GitStatus: The GitStatus object containing the status of the path.

        """
        status = self.get_status(absolute_paths=True)
        return GitStatus(
            untracked=[
                os.path.relpath(f, start=path)
                for f in status.untracked
                if is_parent_path(parent_path=path, child_path=f)
            ],
            unstaged=[
                os.path.relpath(f, start=path)
                for f in status.unstaged
                if is_parent_path(parent_path=path, child_path=f)
            ],
            staged=[
                os.path.relpath(f, start=path)
                for f in status.staged
                if is_parent_path(parent_path=path, child_path=f)
            ],
        )
