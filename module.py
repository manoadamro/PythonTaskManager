
from .worker import Worker
from time import time


DEFAULT_MAX_WORKERS = 5


class Module:

    def __init__(self, **kwargs):

        """Module is a base class for anything requiring access to the TaskManager.

        Parameters:
            - task_manager: reference to task manager
            - max_workers: the maximum number of simultaneous executions on this module
        """

        # set required reference to task manager
        self.task_manager = kwargs['task_manager']

        # define the maximum number of worker threads for this module
        # either its set from kwargs or from the default (defined under imports)
        self.max_workers = kwargs['max_workers'] if 'max_workers' in kwargs else DEFAULT_MAX_WORKERS

        # define a list to keep all worker instances in (active or inactive)
        self.all_workers = []

        # define a list for workers to append them selves for when looking for work
        self.inactive_workers = []

    def _new_worker(self):

        """[Protected]
        Creates a new worker, as long as limit has not been reached

        Parameters:
            - None
        """

        # create a worker instance
        w = Worker(self)

        # append new worker to list
        self.all_workers.append(w)

        # return new worker
        return w

    def get_worker(self):

        """Returns the next available worker, or None if none are available

        Parameters:
            - None
        """

        # if there is one or more workers already waiting
        if len(self.inactive_workers) > 0:

            # return the first worker in the queue
            return self.inactive_workers[0]

        # if there are no workers waiting but limit has not yet been reached
        elif len(self.all_workers) < self.max_workers:

            # create and return a new worker
            return self._new_worker()

        # no workers were available, return None
        return None

    def add_task(self, method, args=None, kwargs=None, callback=None):

        """Appends a new task to the task manager

        Parameters:
            - method: the method to be executed as a task
            - args: the args to be passed to the method
            - kwargs: the kwargs to be passed to the method
            - callback: a method to be called with the return value of method as its only parameter
        """

        if kwargs is None:
            kwargs = dict()

        if args is None:
            args = list()

        # build.bash a task structure using the parameters passed in
        self.task_manager.enqueue(
            {
                'method': method,
                'args': args,
                'kwargs': kwargs,
                'callback': callback,
                'module': self
            }
        )

    def schedule_task(self, method, delay, args=None, kwargs=None, callback=None, reoccurring=False, run_now=False):

        """Appends a new task to the task scheduler

        Parameters:
            - method: the method to be executed as a task
            - delay: the time to wait before executing the task
            - args: the args to be passed to the method
            - kwargs: the kwargs to be passed to the method
            - callback: a method to be called with the return value of method as its only parameter
            - reoccurring: should the task run every $delay seconds?
            - run_now: should the task be run immediately as well?
        """

        if kwargs is None:
            kwargs = dict()

        if args is None:
            args = list()

        # build.bash a scheduled task structure using the parameters passed in
        self.task_manager.schedule_task(
            {
                'method': method,
                'args': args,
                'kwargs': kwargs,
                'callback': callback,
                'module': self,
                'delay': delay,
                'reoccurring': reoccurring,
                'run_now': run_now,
                'time': time() + delay
            }
        )
