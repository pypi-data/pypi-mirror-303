Dask Setup
==========

.. currentmodule:: gordias.dask_setup

Scheduler functions
-------------------

.. autosummary::
   :toctree: _autosummary
   :template: custom-base-template.rst
   :recursive:

   progress
   cpu_count_physical
   hyperthreading_info
   restart_cluster
   setup_scheduler


Schedulers
----------

.. autosummary::
   :toctree: _autosummary
   :template: custom-class-template.rst
   :recursive:

   DistributedLocalClusterScheduler
   DummyClient
   ExternalScheduler
   LocalThreadsScheduler
   MPIScheduler
   SingleThreadedScheduler
