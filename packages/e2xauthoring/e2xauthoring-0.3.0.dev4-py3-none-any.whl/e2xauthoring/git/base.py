import os
import time

from git import Actor, GitCommandError, InvalidGitRepositoryError, Repo

from ..dataclasses import GitStatus
from ..patterns.observer import Subject


class BaseRepo(Subject):
    def __init__(self, path, min_update_interval=5):
        """
        Initializes the BaseRepo object.

        Args:
            path (str): The path of the repository.
            min_update_interval (int, optional): The minimum update interval in seconds.
                Defaults to 5.
        """
        super().__init__()
        self.path = path
        self.repo = self.get_repo()
        self.status = GitStatus(
            untracked=[],
            unstaged=[],
            staged=[],
        )
        self.min_update_interval = min_update_interval
        self.last_modified = 0
        self.last_full_update = 0
        self.update_status()

    @property
    def is_version_controlled(self):
        """
        Checks if the path is a Git repository.

        Returns:
            bool: True if the path is a Git repository, False otherwise.
        """
        return self.repo is not None

    @property
    def repo_root(self):
        """
        Retrieves the root directory of the Git repository.

        Returns:
            str or None: The root directory of the Git repository if found, None otherwise.
        """
        if self.repo is not None:
            return self.repo.working_tree_dir
        return None

    def get_status(self, absolute_paths=False):
        """
        Retrieves the status of the repository.

        Args:
            absolute_paths (bool, optional): Whether to return absolute paths. Defaults to False.

        Returns:
            GitStatus: The status of the repository.
        """
        if absolute_paths:
            return GitStatus(
                untracked=[
                    os.path.join(self.repo_root, f) for f in self.status.untracked
                ],
                unstaged=[
                    os.path.join(self.repo_root, f) for f in self.status.unstaged
                ],
                staged=[os.path.join(self.repo_root, f) for f in self.status.staged],
            )
        return self.status

    def get_repo_modification_time(self):
        """
        Retrieves the last modification time of the Git repository.

        Returns:
            float: The last modification time of the Git repository.
        """
        if not self.is_version_controlled:
            return 0
        index_path = os.path.join(self.repo_root, ".git", "index")
        head_path = os.path.join(self.repo_root, ".git", "HEAD")
        timestamp = 0
        if os.path.exists(index_path):
            timestamp = max(timestamp, os.path.getmtime(index_path))
        if os.path.exists(head_path):
            timestamp = max(timestamp, os.path.getmtime(head_path))
        return timestamp

    def get_repo(self):
        """
        Retrieves the Git repository object.

        Returns:
            Repo or None: The Git repository object if found, None otherwise.
        """
        try:
            return Repo(self.path, search_parent_directories=True)
        except InvalidGitRepositoryError:
            return None

    def refresh_repo(self):
        """
        Refreshes the Git repository object.
        """
        if time.time() - self.last_full_update < self.min_update_interval:
            return
        old_path = self.repo.working_tree_dir if self.repo else None
        self.repo = self.get_repo()

        if self.repo is None or self.repo.working_tree_dir != old_path:
            self.last_modified = 0
        self.update_status()

    def update_status(self):
        """
        Updates the status of the repository.
        """
        if time.time() - self.last_full_update < self.min_update_interval:
            return
        self.update_untracked()
        self.update_staged_and_unstaged()
        self.last_full_update = time.time()
        self.notify()

    def update_untracked(self):
        """
        Updates the list of untracked files in the repository.
        """
        if self.is_version_controlled:
            self.status.untracked = self.repo.untracked_files
        else:
            self.status.untracked = []

    def update_staged_and_unstaged(self):
        """
        Updates the lists of staged and unstaged files in the repository.
        """
        if not self.is_version_controlled:
            self.status.staged = []
            self.status.unstaged = []
            return
        # Update only if the HEAD or index has been modified
        mtime = self.get_repo_modification_time()
        if mtime > self.last_modified:
            self.status.unstaged = [item.a_path for item in self.repo.index.diff(None)]
            if self.repo.head.is_valid():
                self.status.staged = [
                    item.a_path for item in self.repo.index.diff("HEAD")
                ]
            else:
                self.status.staged = [key[0] for key in self.repo.index.entries.keys()]
            self.last_modified = mtime

    def initialize_repo(self):
        """
        Initializes a Git repository.
        """
        if self.is_version_controlled:
            return
        self.repo = Repo.init(self.path)
        self.last_modified = 0
        self.last_full_update = 0
        self.update_status()

    def add(self, path: str) -> bool:
        """
        Adds a file to the repository.

        Args:
            path (str): The path of the file to be added.

        Returns:
            bool: True if the file was added, False otherwise.
        """
        if not self.is_version_controlled:
            return False
        path = os.path.relpath(os.path.abspath(path), start=self.repo_root)
        self.repo.git.add(path)
        return True

    def commit(
        self,
        path: str,
        add_if_untracked=False,
        message: str = None,
        author: Actor = None,
    ) -> bool:
        """
        Commits changes to the repository.

        Args:
            path (str): The path of the file to be committed.
            add_if_untracked (bool, optional): Whether to add the file if it is untracked.
                Defaults to False.
            message (str, optional): The commit message. If not provided, a default message will be
                used. Defaults to None.
            author (Actor, optional): The author of the commit. Defaults to None.

        Returns:
            bool: True if the commit was successful, False otherwise.
        """
        if not self.is_version_controlled:
            return False
        relpath = os.path.relpath(os.path.abspath(path), start=self.repo_root)
        author_string = (
            f"{author.name} <{author.email}>" if author is not None else None
        )
        try:
            if add_if_untracked:
                self.add(path)
            if message is None:
                message = f"Update {relpath}"
            self.repo.git.commit(relpath, message=message, author=author_string)
        except GitCommandError:
            return False
        return True

    def diff(self, file_path: str, color: bool = True, html=True) -> str:
        """
        Generate a diff for the specified file.

        Args:
            file_path (str): The path of the file to generate the diff for.
            color (bool, optional): Whether to include color in the diff. Defaults to True.
            html (bool, optional): Whether to format the diff as HTML. Defaults to True.

        Returns:
            str: The generated diff.
        """
        if not self.is_version_controlled:
            return ""
        diff = self.repo.git.diff(
            os.path.relpath(file_path, start=self.repo.working_tree_dir), color=color
        )
        if html:
            diff.replace("\n", "<br/>")
        return diff
