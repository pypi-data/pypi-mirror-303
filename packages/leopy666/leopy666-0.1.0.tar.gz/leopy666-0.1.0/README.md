# leopy
Python tools developed by Leo.

## Decorators

- `timeout`: This decorator can be used to set a timeout for a function. It takes a parameter `seconds`, which represents the maximum allowed execution time of the function in seconds. If the function execution time exceeds the specified timeout, the decorator raises a `TimeoutError` exception.

- `rate_limiter`: This decorator can be used to limit the call frequency of a function. It takes two parameters: `limit`, which represents the maximum number of allowed calls within a specified time interval, and `interval`, which represents the length of the time interval in seconds. If the function is called too frequently, the decorator automatically introduces a delay to meet the rate limiting requirement.

- `stoppable`: This decorator can convert a function into a stoppable background thread. It takes an optional parameter `sleep_time`, which specifies the sleep time between each function execution, defaulting to 1 second. The decorator internally creates a thread event object `stop_event` to control the stopping of the thread. In a separate thread, the original function is continuously executed in a loop, sleeping according to `sleep_time` after each execution. By calling the `stop` function returned by the decorator, the thread execution can be stopped at any time. This decorator is very useful in situations where long-running tasks or dynamic control of task execution is needed.

- `timer`: This decorator can be used to measure the execution time of a function. It records the start time of the function execution and then calculates and prints the execution time after the function completes.

- `cache`: This decorator can be used to cache the results of a function. If the function has been called with the same arguments before, the decorator directly returns the cached result instead of re-executing the function. This can improve the performance of functions, especially for computationally expensive functions that are frequently called with the same arguments.

- `retry_decorator`: This decorator can be used to handle exceptions that may occur during function execution. If the function raises an exception, the decorator automatically retries the function execution until the specified maximum number of retries is reached. There is a certain delay time between each retry.

- `logger`: This decorator can be used to log the call information and return value of a function. It prints the function name, arguments, and other information before the function executes, and prints the return value of the function after it executes. This is very helpful for debugging and tracing the function execution process.

## Utils





