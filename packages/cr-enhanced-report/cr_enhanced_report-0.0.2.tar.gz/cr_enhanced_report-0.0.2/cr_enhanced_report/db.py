"""Module to overload the cosmic-ray database."""
import contextlib
from typing import Any

from cosmic_ray.work_db import (MutationSpecStorage, WorkDB, WorkItemStorage,
                                WorkResultStorage, _mutation_spec_from_storage,
                                _work_item_from_storage,
                                _work_result_from_storage)
from cosmic_ray.work_item import TestOutcome
from sqlalchemy import func


class DB(WorkDB):
    """Database handler adding new functionality to WorkDB."""

    skip_success: bool = False
    _kill_count: int | None = None
    _survival_rate: float | None = None

    @property
    def completed_work_items(self) -> tuple[Any, ...]:
        """
        Iterable of all completed work items.

        Returns:
            Tuple of completed work items.
        """
        with self._session_maker.begin() as session:
            results = session.query(
                WorkItemStorage, WorkResultStorage, MutationSpecStorage
            ).where(
                WorkItemStorage.job_id == WorkResultStorage.job_id
            ).where(
                WorkItemStorage.job_id == MutationSpecStorage.job_id
            )
            if self.skip_success:
                results = results.where(
                    WorkResultStorage.test_outcome != TestOutcome.KILLED
                )
            results = results.order_by(MutationSpecStorage.module_path)
            return tuple(
                (
                    _work_item_from_storage(work_item),
                    _work_result_from_storage(result),
                    _mutation_spec_from_storage(mutation_spec)
                ) for work_item, result, mutation_spec in results
            )

    def fetch_status_counts(self):
        """Fetch status counts from the database."""
        with self._session_maker.begin() as session:
            results = session.query(
                WorkResultStorage.test_outcome,
                MutationSpecStorage.module_path,
                func.count(WorkResultStorage.test_outcome)
            ).where(
                WorkResultStorage.job_id == WorkItemStorage.job_id
            ).where(
                WorkResultStorage.job_id == MutationSpecStorage.job_id
            ).group_by(
                MutationSpecStorage.module_path, WorkResultStorage.test_outcome
            ).all()

        return results

    @property
    def kill_count(self) -> int:
        """
        Fetch the number of killed mutants.

        Returns:
            Number of killed mutants.
        """
        if self._kill_count is None:
            self._kill_count = sum(r.is_killed for _, r in self.results)
        return self._kill_count or 0

    @property
    def survival_rate(self) -> float:
        """
        Fetch the survival rate.

        Returns:
            Survival rate as a percentage accurate to 2 decimal places.
        """
        if self._survival_rate is None:
            kills = self.kill_count
            num_results = self.num_results
            self._survival_rate = round((1 - kills / num_results) * 100, 2) if num_results else 0.0

        return self._survival_rate


@contextlib.contextmanager
def use_db(path, mode=DB.Mode.create):
    """
    Open a DB in file `path` in mode `mode` as a context manager.

    On exiting the context the DB will be automatically closed.

    Function is a copy of cosmic-ray.work_db.use_db modified to use our
    extension of WorkDB.

    Args:
      path: The path to the DB file.
      mode: The mode to open the DB with.

    Raises:
      FileNotFoundError: If `mode` is `Mode.open` and `path` does not
        exist.
    """
    database = DB(path, mode)
    try:
        yield database

    finally:
        database.close()
