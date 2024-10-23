import glob
import os
from typing import Dict, List

from nbgrader.coursedir import CourseDirectory
from traitlets import Unicode
from traitlets.config import LoggingConfigurable

from ..dataclasses import PoolCollectionRecord
from .pool import Pool


class PoolCollection(LoggingConfigurable):
    pools: Dict[str, Pool]
    coursedir: CourseDirectory

    directory = Unicode("pools", help="Directory where pools are stored").tag(
        config=True
    )

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PoolCollection, cls).__new__(cls)
        return cls._instance

    def __init__(self, coursedir: CourseDirectory):
        if not self._initialized:
            self.coursedir = coursedir
            self.pools = dict()
            self.init_pools()
            self.__class__._initialized = True

    def __getitem__(self, key):
        return self.pools[key]

    def __contains__(self, key):
        return key in self.pools

    @property
    def pool_path(self):
        return self.coursedir.format_path(self.directory, ".", ".")

    def get_pool_paths(self) -> List[str]:
        paths = glob.glob(os.path.join(self.pool_path, "*"))
        return [os.path.basename(path) for path in paths if os.path.isdir(path)]

    def init_pool(self, pool_name: str):
        if pool_name not in self.pools:
            self.pools[pool_name] = Pool(name=pool_name, base_path=self.pool_path)

    def init_pools(self):
        pool_names = self.get_pool_paths()
        for pool_name in pool_names:
            self.init_pool(pool_name)

    def update_pools(self):
        pool_names = self.get_pool_paths()
        deleted_pools = set(self.pools.keys()) - set(pool_names)
        for pool_name in deleted_pools:
            del self.pools[pool_name]
        added_pools = set(pool_names) - set(self.pools.keys())
        for pool_name in added_pools:
            self.init_pool(pool_name)
        # For each pool that is not a repository, check if it is now a repository
        for pool in self.pools.values():
            if not pool.is_version_controlled():
                pool.repo.get_repo()
                if pool.is_version_controlled():
                    pool.repo.update_status()

    def add_pool(self, pool_name: str, init_repo: bool = False):
        pool_path = os.path.join(self.pool_path, pool_name)
        assert not os.path.exists(pool_path), f"Pool {pool_name} already exists"
        pool = Pool.create(
            name=pool_name,
            base_path=self.pool_path,
            init_repo=init_repo,
        )
        self.pools[pool_name] = pool

    def remove_pool(self, pool_name: str):
        assert pool_name in self.pools, f"Pool {pool_name} does not exist"
        pool = self.pools[pool_name]
        pool.remove()
        del self.pools[pool_name]

    def copy_pool(self, pool_name: str, new_name: str):
        assert pool_name in self.pools, f"Pool {pool_name} does not exist"
        pool = self.pools[pool_name]
        new_pool = pool.copy(new_name)
        self.pools[new_name] = new_pool

    def rename_pool(self, pool_name: str, new_name: str):
        assert pool_name in self.pools, f"Pool {pool_name} does not exist"
        pool = self.pools[pool_name]
        pool.rename(new_name)
        self.pools[new_name] = pool
        del self.pools[pool_name]

    def add_task(self, pool_name: str, task_name: str, kernel_name: str = None):
        assert pool_name in self.pools, f"Pool {pool_name} does not exist"
        pool = self.pools[pool_name]
        pool.add_task(task_name, kernel_name=kernel_name)

    def remove_task(self, pool_name: str, task_name: str):
        assert pool_name in self.pools, f"Pool {pool_name} does not exist"
        pool = self.pools[pool_name]
        pool.remove_task(task_name)

    def copy_task(self, pool_name: str, task_name: str, new_name: str):
        assert pool_name in self.pools, f"Pool {pool_name} does not exist"
        pool = self.pools[pool_name]
        pool.copy_task(task_name, new_name)

    def rename_task(self, pool_name: str, task_name: str, new_name: str):
        assert pool_name in self.pools, f"Pool {pool_name} does not exist"
        pool = self.pools[pool_name]
        pool.rename_task(task_name, new_name)

    def to_dataclass(self, include_git_status=False) -> PoolCollectionRecord:
        self.update_pools()

        return PoolCollectionRecord(
            pools=[
                pool.to_dataclass(include_git_status=include_git_status)
                for pool in self.pools.values()
            ]
        )

    def to_json(self, include_git_status=False):
        return self.to_dataclass(include_git_status=include_git_status).to_json()
