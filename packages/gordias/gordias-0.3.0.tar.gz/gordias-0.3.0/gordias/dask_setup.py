"""Module for setting up dask scheduler."""

from __future__ import annotations

import argparse
import glob
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any

import dask
import psutil
from dask.distributed import Client, LocalCluster, system, wait
from dask.distributed import progress as distributed_progress

logger = logging.getLogger(__name__)


def progress(fs: Any) -> Any:
    """
    Perform outstanding calculations similar to :func:`distributed.diagnostics.progressbar.progress`.

    Detects whether we are in an interactive environment or not. In an
    interactive environment we use :func:`distributed.diagnostics.progressbar.progress`
    to output a dynamic progress bar during the calculations. In a non-interactive
    setting, we don't output anything and just :func:`distributed.wait` for the
    end of the calculations. This is useful to keep log files clean for HPC
    jobs.

    Parameters
    ----------
    fs : `distributed.Future`
        A list of futures or keys to track.
    """  # noqa
    if sys.stdout.isatty():
        return distributed_progress(fs)
    else:
        wait(fs)
        return fs


def cpu_count_physical() -> int | None:
    # Adapted from psutil
    """
    Return the number of physical cores in the system.

    Used to detect hyperthreading.

    Returns
    -------
    int or None
        Number of physical cores or `None` if not detectable.
    """
    ids = ["physical_package_id", "die_id", "core_id", "book_id", "drawer_id"]
    core_ids = set()
    for path in glob.glob("/sys/devices/system/cpu/cpu[0-9]*/topology"):
        core_id = []
        for id in ids:
            id_path = os.path.join(path, id)
            if os.path.exists(id_path):
                with open(id_path) as f:
                    core_id.append(int(f.read()))
        core_ids.add(tuple(core_id))
    result = len(core_ids)
    if result != 0:
        return result
    else:
        return None


def hyperthreading_info() -> tuple[bool | None, int, int]:
    """
    Detect presence of hyperthreading.

    If there are more logical cpus than physical ones, hyperthreading is
    active.

    Returns
    -------
    hyperthreading : bool or None
        If `True`, hyperthreading is active.
    no_logical_cpus : int
        Number of logical cpus.
    no_physical_cpus : int
        Number of physical cpus.
    """
    no_logical_cpus = psutil.cpu_count(logical=True)
    no_physical_cpus = cpu_count_physical()
    if no_logical_cpus is None or no_physical_cpus is None:
        return (None, 0, 0)
    else:
        hyperthreading = no_logical_cpus > no_physical_cpus
    return (hyperthreading, no_logical_cpus, no_physical_cpus)


def restart_cluster(client: Client) -> None:
    """
    Restarts cluster.

    Parameters
    ----------
    client : Scheduler
        `Client` to restart Cluster.
    """
    info = client.scheduler_info()

    def total_executing() -> Any:
        return sum(sum(w) for w in client.processing().values())

    expected_nr_workers = len(info["workers"])
    retries = 5
    while (nr_executing := total_executing()) > 0:
        logger.info(f"Waiting for {nr_executing} tasks to finish")
        time.sleep(60)
        if retries > 0:
            logger.info(f"Retrying with {retries} retries left.")
            retries -= 1
        else:
            logger.info("Retries exhausted. Hoping for the best.")
            break
    client.restart()
    client.wait_for_workers(expected_nr_workers, 120)


class DummyClient:
    """Dummy class mimicking :obj:`distributed.Client` without `distributed`."""

    def persist(self, x: Any) -> Any:
        """Dummy method mimicking persist."""  # noqa
        return x


class DistributedLocalClusterScheduler:
    """
    Scheduler using :obj:`distributed.LocalCluster` for local parallelism.

    Recommended way to use on a single machine.

    Parameters
    ----------
    threads_per_worker : int, optional
        Number of threads per each worker.

    Attributes
    ----------
    cluster : `dask.LocalCluster`
        A `cluster` of a scheduler and workers running on the local machine.
    client : `dask.Client`
        A `client` that connect to and submit computation to a Dask cluster.
    """

    def __init__(self, threads_per_worker: int = 2, **kwargs: Any) -> None:  # noqa ARG002
        (hyperthreading, no_logical_cpus, no_physical_cpus) = hyperthreading_info()
        if hyperthreading:
            factor = no_logical_cpus // no_physical_cpus
            no_available_physical_cpus = dask.system.CPU_COUNT // factor
            n_workers = no_available_physical_cpus // threads_per_worker
            # leave one core for scheduler and client
            n_workers -= 1
            # but make sure to have at least one worker
            n_workers = max(1, n_workers)
            # use 90% of available memory for workers,
            # rest for scheduler, client, and system
            memory_limit = (system.MEMORY_LIMIT * 0.9) / n_workers
        else:
            # let dask figure it out
            n_workers = None
            memory_limit = None
        self.cluster = LocalCluster(
            n_workers=n_workers,
            threads_per_worker=threads_per_worker,
            memory_limit=memory_limit,
        )
        self.client = Client(self.cluster)

    def __enter__(self) -> DistributedLocalClusterScheduler:
        """Magic method following PEP 343."""
        self.cluster.__enter__()
        self.client.__enter__()
        return self

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None:
        """Magic method following PEP 343."""
        self.client.__exit__(type, value, traceback)
        self.cluster.__exit__(type, value, traceback)


class ExternalScheduler:
    """
    Scheduler using an externally started :obj:`distributed.Cluster`.

    This is useful if the cluster needs to be set up outside of the program,
    for example in a HPC environment or for debugging purposes.

    Parameters
    ----------
    scheduler_file : str or Path
        Path to a file with scheduler information.
    auto_shutdown : bool
        Turn on auto shutdown. By default set to `True`.

    Attributes
    ----------
    scheduler_file:  str or Path
        Path to a file with scheduler information.
    auto_shutdown : bool
        Turn on auto shutdown. By default set to `True`.
    client : `dask.Client`
        A `client` that connect to and submit computation to a Dask cluster.
    """

    def __init__(
        self,
        scheduler_file: str | Path,
        auto_shutdown: bool = True,
        **kwargs: Any,  # noqa ARG002
    ) -> None:
        p = Path(scheduler_file)
        time_to_wait = 10
        while not p.exists():
            time.sleep(1)
            time_to_wait -= 1
            if time_to_wait <= 0:
                raise RuntimeError("Scheduler does not exist")
        self.scheduler_file = scheduler_file
        self.client = Client(scheduler_file=scheduler_file)
        self.auto_shutdown = auto_shutdown

    def __enter__(self) -> ExternalScheduler:
        """Magic method following PEP 343."""
        self.client.__enter__()
        return self

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None:
        """Magic method following PEP 343."""
        if self.auto_shutdown:
            self.client.shutdown()
        self.client.__exit__(type, value, traceback)


class LocalThreadsScheduler:
    """
    Scheduler using `dask` without `distributed`.

    Generally not useful due to the extensive use of :obj:`distributed.Client` in the
    program. May occasionally be used for debugging.

    Attributes
    ----------
    client : None
        A `client` that is set to `None`

    """

    def __init__(self, **kwargs: Any) -> None:  # noqa ARG002
        self.client = None

    def __enter__(self) -> LocalThreadsScheduler:
        """Magic method following PEP 343."""
        dask.config.set(scheduler="threads")
        return self

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None:  # noqa ARG002
        """Magic method following PEP 343."""
        pass


class MPIScheduler:
    """
    Scheduler using dask.mpi for cluster setup.

    Should be avoided since the `Dask-MPI project <http://mpi.dask.org/en/latest>`_
    seems to be out-of-date. For now, prefer :obj:`ExternalScheduler`; might be
    revisited at a later time.

    Attributes
    ----------
    client : `dask.Client`
        A `client` that connect to and submit computation to a Dask cluster.
    """

    def __init__(self, **kwargs: Any) -> None:  # noqa ARG002
        from dask_mpi import initialize

        n_workers = 4  # tasks-per-node from scheduler
        n_threads = 4  # cpus-per-task from scheduler
        memory_limit = (system.MEMORY_LIMIT * 0.9) / n_workers
        initialize(
            "ib0",
            nthreads=n_threads,
            local_directory="/scratch/local",
            memory_limit=memory_limit,
        )
        self.client = Client()

    def __enter__(self) -> MPIScheduler:
        """Magic method following PEP 343."""
        self.client.__enter__()
        return self

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None:
        """Magic method following PEP 343."""
        self.client.__exit__(type, value, traceback)


class SingleThreadedScheduler:
    """
    Scheduler using strictly local, single threaded approach.

    Only for debugging.

    Attributes
    ----------
    client : `DummyClient`
        A dummy class thet mimicks a `client`.
    """

    def __init__(self, **kwargs: Any) -> None:  # noqa ARG002
        self.client = DummyClient()

    def __enter__(self) -> SingleThreadedScheduler:
        """Magic method following PEP 343."""
        dask.config.set(scheduler="single-threaded")
        return self

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None:  # noqa ARG002
        """Magic method following PEP 343."""
        pass


#: Available schedulers. For detailed descriptions see the respective class.
SCHEDULERS = {
    "distributed-local-cluster": DistributedLocalClusterScheduler,
    "external": ExternalScheduler,
    "threaded": LocalThreadsScheduler,
    "mpi": MPIScheduler,
    "single-threaded": SingleThreadedScheduler,
}


def setup_scheduler(
    args: argparse.Namespace,
) -> (
    DistributedLocalClusterScheduler
    | ExternalScheduler
    | LocalThreadsScheduler
    | MPIScheduler
    | SingleThreadedScheduler
    | Any
):
    """
    Start a scheduler for use of parallel environment with :obj:`distributed.Client`.

    Parameters
    ----------
    args : argparse.Namespace
        Arguments to setup the scheduler. Generally, an entry from
        :const:`SCHEDULERS`.

    Returns
    -------
    scheduler
        One of the scheduler objects defined in :ref:`schedulers`,
        suitable as a context manager.
    """
    scheduler_spec = args.dask_scheduler.split("@")
    scheduler_name = scheduler_spec[0]
    scheduler_kwargs = dict(e.split("=") for e in scheduler_spec[1:])
    scheduler = SCHEDULERS[scheduler_name]
    return scheduler(**scheduler_kwargs)
