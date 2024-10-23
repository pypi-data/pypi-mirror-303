import multiprocessing
from time import sleep
from queue import Queue
from modeltasks.util.task import ExecutionTimer
from modeltasks.scheduler import AbstractScheduler


class MultiprocessingScheduler(AbstractScheduler):
    """
    A scheduler using multiple processes for the simultaneous execution of jobs.
    """

    def run(self):
        """
        Execute the scheduled tasks (blocking until all tasks are done)
        """
