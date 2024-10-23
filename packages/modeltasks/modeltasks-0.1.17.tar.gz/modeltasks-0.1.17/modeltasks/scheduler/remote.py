from modeltasks.scheduler.abstract import AbstractScheduler


class RemoteScheduler(AbstractScheduler):
    """
    A scheduler using remote processing for the simultaneous execution of jobs.
    """

    def run(self):
        """
        Execute the scheduled tasks (blocking until all tasks are done)
        """
