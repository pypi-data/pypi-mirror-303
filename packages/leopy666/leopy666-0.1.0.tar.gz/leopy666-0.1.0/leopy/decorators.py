import threading
import time
import signal

def timeout(seconds):
    '''
    这个装饰器可以为函数设置超时时间。它接受一个参数seconds,表示函数允许执行的最长时间(以秒为单位)。如果函数执行时间超过了指定的超时时间,装饰器会抛出一个TimeoutError异常。
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutError(f"Function '{func.__name__}' timed out after {seconds} seconds")
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wrapper
    return decorator



def rate_limiter(limit, interval):
    '''
    这个装饰器可以限制函数的调用频率。它接受两个参数:limit表示在指定的时间间隔内允许的最大调用次数,interval表示时间间隔的长度(以秒为单位)。如果函数调用过于频繁,装饰器会自动引入延迟以满足限速要求。
    '''
    def decorator(func):
        last_called = 0
        def wrapper(*args, **kwargs):
            nonlocal last_called
            elapsed = time.time() - last_called
            if elapsed < interval:
                time.sleep(interval - elapsed)
            last_called = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def stoppable(sleep_time=1):
    '''
    这个装饰器可以将一个函数转换为可停止的后台线程。它接受一个可选的参数sleep_time,用于指定每次函数执行完毕后的休眠时间,默认为1秒。装饰器内部创建了一个线程事件对象stop_event,用于控制线程的停止。在一个独立的线程中,原始函数在一个循环内不断执行,并在每次执行完毕后根据sleep_time进行休眠。通过调用装饰器返回的stop函数,可以随时停止线程的执行。这个装饰器在需要长时间运行的任务或需要动态控制任务执行的情况下非常有用。
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            stop_event = threading.Event()

            def inner():
                while not stop_event.is_set():
                    func(*args, **kwargs)
                    time.sleep(sleep_time)

            thread = threading.Thread(target=inner)
            thread.start()

            def stop():
                stop_event.set()
                thread.join()

            return stop

        return wrapper

    return decorator



def timer(func):
    '''
    这个装饰器可以用来测量函数的执行时间。它记录函数开始执行的时间,然后在函数执行完毕后计算并打印执行时间。
    '''
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.5f} seconds")
        return result
    return wrapper

def cache(func):
    '''
    这个装饰器可以用来缓存函数的结果。如果函数曾经使用相同的参数被调用过,装饰器会直接返回缓存的结果,而不是重新执行函数。这可以提高函数的性能,特别是对于计算量大且经常使用相同参数调用的函数。
    '''
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper


def retry_decorator(max_retries, delay):
    '''
    这个装饰器可以用来处理函数执行过程中可能出现的异常。如果函数抛出异常,装饰器会自动重试执行函数,直到达到指定的最大重试次数。每次重试之间会有一定的延迟时间。
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            retry_count = 0
            while retry_count < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    retry_count += 1
                    print(f"Retry {retry_count}/{max_retries} due to: {str(e)}")
                    time.sleep(delay)
            raise Exception("Max retries exceeded")
        return wrapper
    return decorator


def logger(func):
    '''
    这个装饰器可以用来记录函数的调用信息和返回值。它在函数执行前打印函数名称、参数等信息,在函数执行后打印函数的返回值。这对于调试和跟踪函数执行过程非常有帮助。
    '''
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper




