# PythonTaskManager

      from taskmanager import TaskManager, Module

## TaskManager:
      
      manager = TaskManager()
      
  TaskManager is responsible for queuing tasks and executing them when required.
  Tasks can be queued in two different ways.
  
  ### Add Task  
  enqueues a task to be executed immediately.  
  Tasks are usually added through a Module class, although they can be added directly via task manager.
  this will require a dictionary with the following keys
  
          {
            'method': method,           # the method to call,
                                        # can NOT be None
                                    
            'args': [list or tuple],    # args to pass to the method
                                        # can be None
              
            'kwargs': {dict},           # keyword args to pass to the method,
                                        # can be None
              
            'callback': method,         # called when method completes, 
                                        # can be method or list/tuple of methods
                                        # takes one arg (the return from method),
                                        # can be None or list                                
          }
           
  
  ### Schedule Task
  enqueues a task to be executed at a given time or interval.
  Tasks are usually scheduled through a Module class as well, although they can too be added directly via task manager.
  this will require a dictionary with the following keys

          {
            'method': method,           # the method to call,
                                        # can NOT be None
                                    
            'args': [list or tuple],    # args to pass to the method
                                        # can be None
              
            'kwargs': {dict},           # keyword args to pass to the method,
                                        # can be None
              
            'callback': method,         # called when method completes, 
                                        # can be method or list/tuple of methods
                                        # takes one arg (the return from method),
                                        # can be None or list 
         
            'delay': number,            # number of seconds to wait before executing
                                        # if reoccurring,
                                        # it will also act as the number of seconds interval between executions
              
            'reoccurring': bool,        # if false, the task will only execute once, then be deleted
                                        # if true, the task will execute every {delay} seconds
                                          
            'run_now': bool,            # should the task also be run immediately?
              
          }

___

## Module:

         my_module = Module( task_manager=, max_workers= )
      
  ### Args & Kwargs
  
        task_manager TaskManager: a reference to a task manager instance
        max_workers int: the maximum number of threads a module is allowed at any one time
  
  ### Add Task:  
  
  enqueues a task to be executed at a given time or interval.
  
  __required args:__
  
        method: method                  # the method to call,
     
  
  __Optional keyword args:__ 
  
        args: [list or tuple]           # args to pass to the method
                                        # default None
              
        kwargs: {dict}                  # keyword args to pass to the method,
                                        # default None
              
        callback': method               # called when method completes,
                                        # can be method or list/tuple of methods
                                        # takes one arg (the return from method),
                                        # can be None or list
                                        # default None
  
  ### Schedule Task:

  enqueues a task to be executed at a given time or interval.

  __required args:__
  
        method: method                  # the method to call,
    
        delay: number                   # number of seconds to wait before executing
                                        # if reoccurring,
                                        # it will also act as the number of seconds interval between executions
  
  __Optional keyword args:__
  
        args: [list or tuple]           # args to pass to the method
                                        # default None
              
        kwargs: {dict}                  # keyword args to pass to the method,
                                        # default None
              
        callback': method               # called when method completes,
                                        # can be method or list/tuple of methods
                                        # takes one arg (the return from method),
                                        # can be None or list
                                        # default None
                                    
        reoccurring: bool               # if false, the task will only execute once, then be deleted
                                        # if true, the task will execute every {delay} seconds
                                        # default False
                                          
        run_now: bool                   # should the task also be run immediately?
                                        # default False

# Example

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
          
      
      manager = TaskManager()
      manager.start_thread()
      
      something = SomeModule(task_manager=manager, max_workers=5)
      
      
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
