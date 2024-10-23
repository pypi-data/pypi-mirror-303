from typing import List
from modeltasks.task import ModelTask


class JobPipeline:
    """
    A job pipeline is a sub entity of the scheduler responsible for keeping track of
    a sequence of certain jobs (queue). A pipeline needs to implement the following methods.
    """

    _locked = False
    _jobs = None
    _paused = False
    _concurrent_jobs = 0

    @property
    def concurrent_jobs(self):
        return self._concurrent_jobs

    @property
    def paused(self):
        return self._paused

    def __init__(self):
        self._jobs = []

    def add(self, jobs: List):
        """
        Add job(s) to the pipeline.
        """
        self._concurrent_jobs = max([self._concurrent_jobs, len(jobs)])
        self._add_jobs(jobs)

    def _add_jobs(self, jobs: List):
        """
        Template method to enlist a job (step) in the pipeline.
        Should be overwritten by any subclass by its own method
        """
        self._jobs.append(jobs)

    def get(self) -> List:
        """
        Remove and return an item from the job pipeline
        """
        if self._paused:
            return []
        else:
            return self._get_jobs()

    def _get_jobs(self) -> List:
        """
        Template method to retrieve a job (step) from the pipeline.
        Should be overwritten by any subclass by its own method
        """
        return self._jobs.pop(0)

    def list(self) -> List[ModelTask]:
        """
        List all current jobs in the pipeline
        """
        return self._jobs

    def cancel(self):
        """
        Should cancel all pending jobs of the pipeline
        """
        self._jobs = []

    def pause(self):
        """
        Should pause the pipeline and set all pending jobs as idle
        """
        self._paused = True

    def resume(self):
        """
        Should resume the paused pipeline
        """
        self._paused = False

    def __len__(self):
        return len(self._jobs)
