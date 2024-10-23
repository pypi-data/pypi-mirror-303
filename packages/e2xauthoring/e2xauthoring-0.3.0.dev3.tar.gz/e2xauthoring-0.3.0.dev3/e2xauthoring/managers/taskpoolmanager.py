from ..models import PoolCollection
from .base import BaseManager


class TaskPoolManager(BaseManager):
    pools: PoolCollection

    def __init__(self, coursedir):
        self.pools = PoolCollection(coursedir)

    def assert_pool_exists(self, name):
        assert name in self.pools, f"The pool {name} does not exist."

    def turn_into_repository(self, pool):
        self.assert_pool_exists(pool)
        self.pools[pool].turn_into_repository()

    def get(self, name: str):
        self.assert_pool_exists(name)
        return self.pools[name].to_json(include_git_status=True)

    def copy(self, name: str, new_name: str):
        self.pools.copy_pool(name, new_name)
        return self.pools[new_name].to_json(include_git_status=True)

    def rename(self, name: str, new_name: str):
        self.pools.rename_pool(name, new_name)
        return self.pools[new_name].to_json(include_git_status=True)

    def create(self, name: str, init_repository: bool = False):
        self.pools.add_pool(name, init_repo=init_repository)
        return self.pools[name].to_json(include_git_status=True)

    def remove(self, name):
        self.pools.remove_pool(name)

    def list(self):
        return self.pools.to_json(include_git_status=True)["pools"]
