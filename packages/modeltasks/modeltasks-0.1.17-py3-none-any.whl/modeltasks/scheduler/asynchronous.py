import asyncio
from modeltasks.util.task import ExecutionTimer
from modeltasks.scheduler.abstract import AbstractScheduler


class AsynchronousScheduler(AbstractScheduler):
    """
    A scheduler using async coroutines for the simultaneous execution of jobs.
    """

    def run(self):
        """
        Execute the scheduled tasks (blocking until all tasks are done)
        """
