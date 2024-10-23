from pyinstrument import Profiler
import functools

def profile_function(func):
    """
    A decorator that profiles the execution of a function using pyinstrument.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler = Profiler()
        profiler.start()

        # Execute the original function
        result = func(*args, **kwargs)

        profiler.stop()

        # Print profiling results
        print(profiler.output_text(unicode=True, color=True))

        return result

    return wrapper
