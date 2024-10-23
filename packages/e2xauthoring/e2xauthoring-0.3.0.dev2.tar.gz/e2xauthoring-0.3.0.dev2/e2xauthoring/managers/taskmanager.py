import os

from ..models import PoolCollection
from .base import BaseManager


class TaskManager(BaseManager):
    pools: PoolCollection

    def __init__(self, coursedir):
        self.pools = PoolCollection(coursedir)

    def commit(self, pool, task, message):
        assert pool in self.pools, f"No pool with the name {pool} exists."
        commit_okay = self.pools[pool].commit_task(task, message)
        assert commit_okay, "There was an error during the commit process."

    def git_diff(self, pool, task, file):
        assert pool in self.pools, f"No pool with the name {pool} exists."
        assert (
            task in self.pools[pool]
        ), f"No task with the name {task} exists in pool {pool}."
        file_path = os.path.join(self.pools[pool][task].path, file)
        repo = self.pools[pool].repo
        assert repo.is_version_controlled, "The pool is not version controlled."
        return repo.diff(file_path)

    def get(self, pool: str, name: str):
        assert pool in self.pools, f"No pool with the name {pool} exists."
        taskpool = self.pools[pool]
        assert name in taskpool, f"No task with the name {name} exists in pool {pool}."
        return taskpool[name].to_json(include_git_status=True)

    def create(self, pool: str, name: str, kernel_name: str = None):
        self.pools.add_task(pool, name, kernel_name=kernel_name)

    def remove(self, pool, name):
        self.pools.remove_task(pool, name)

    def list(self, pool):
        assert pool in self.pools, f"No pool with the name {pool} exists."
        return self.pools[pool].to_json(include_git_status=True)["tasks"]

    def list_all(self):
        pools = self.pools.to_json(include_git_status=False)
        tasks = []
        for pool in pools["pools"]:
            tasks.extend(pool["tasks"])
        return tasks

    def copy(self, old_name: str, new_name: str, pool: str = ""):
        self.pools.copy_task(pool, old_name, new_name)

    def rename(self, old_name: str, new_name: str, pool: str = ""):
        self.pools.rename_task(pool, old_name, new_name)
