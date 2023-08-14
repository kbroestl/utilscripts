#! /usr/bin/env python

import functools
import time

def do_twice(func):
	@functools.wraps(func)
	def wrapper_do_twice(*args, **kwargs):
		func(*args, **kwargs)
		return func(*args, **kwargs)
	return wrapper_do_twice

def timer(func):
	"""Print the runtime of the decorated function
		returns a tuple of both the normal function result
		along with a float of the run time elapsed
	"""
	@functools.wraps(func)
	def wrapper_timer(*args, **kwargs):
		start_time = time.perf_counter()
		value = func(*args, **kwargs)
		end_time = time.perf_counter()
		run_time = end_time - start_time
		print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
		value = (value, run_time)
		return value
	return wrapper_timer

def debug(func):
	"""Print the function signature and return value"""
	@functools.wraps(func)
	def wrapper_debug(*args, **kwargs):
		args_repr = [repr(a) for a in args]
		kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
		signature = ", ".join(args_repr + kwargs_repr)
		print(f"Calling {func.__name__}({signature})")
		value = func(*args, **kwargs)
		print(f"{func.__name__!r} returned {value!r}")
		return value
	return wrapper_debug

def slow_down(func):
	"""Sleep for 1 second before calling the function"""
	@functools.wraps(func)
	def wrapper_slow_down(*args, **kwargs):
		time.sleep(1)
		return func(*args, **kwargs)
	return wrapper_slow_down

def repeat(_func=None, *, num_times=2):
	def decorator_repeat(func):
		@functools.wraps(func)
		def wrapper_repeat(*args, **kwargs):
			for _ in range(num_times):
				value = func(*args, **kwargs)
			return value
		return wrapper_repeat
	if _func is None:
		return decorator_repeat
	else:
		return decorator_repeat(_func)

def count_calls(func):
	@functools.wraps(func)
	def wrapper_count_calls(*args, **kwargs):
		wrapper_count_calls.num_calls += 1
		print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
		return func(*args, **kwargs)
	wrapper_count_calls.num_calls = 0
	return wrapper_count_calls
