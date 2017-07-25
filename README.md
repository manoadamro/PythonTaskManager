# PythonTaskManager

      from taskmanager import TaskManager, Module
      
      
      class SomeModule(Module):
        def __init__(self, **kwargs)
          super(SomeModule, self).__init__(**kwargs)
      
        def some_event(self, some_string):
          print(some_string)
          
        def some_other_event(self, some_string):
          return some_string
          
        def some_callback(self, data):
          print(data)
          
      
      task_manager = TaskManager()
      task_manager.start_thread()
      
      something = SomeModule(task_manager=task_manager, max_workers=5)
      
      
      # will create a task to be run asap
      # some_event prints "hello"
      something.add_task(something.some_event, args=("hello",), kwargs=None, callback=None)
      
      # will create a task to be run asap
      # some_callback prints "hello"
      something.add_task(something.some_other_event, args=("hello",), kwargs=None, callback=something.some_callback)
      
      # will create a task to be run in one second
      # some_event prints "hello" after 1 second
      schedule_task(something.some_event, 1, args=None, kwargs=None, callback=None, reoccurring=False, run_now=False)
      
      # will create a task to be run every one second
      # some_event prints "hello" every 1 second, starting in 1 second
      schedule_task(something.some_event, 1, args=None, kwargs=None, callback=None, reoccurring=True, run_now=False)
      
      # will create a task to be run every one second
      # some_event prints "hello" every 1 second, runs it now too
      schedule_task(something.some_event, 1, args=None, kwargs=None, callback=None, reoccurring=True, run_now=True)
