import time
import statistics
from functools import wraps

def timing_decorator(func):
    times = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
        return result

    def get_stats():
        return {
            'average': statistics.mean(times),
            'min': min(times),
            'max': max(times),
            'sdev': statistics.stdev(times) if len(times) > 1 else 0
        }

    wrapper.get_stats = get_stats
    return wrapper

@timing_decorator
def time_consuming_function():
    time.sleep(1)  # niby tylko sleep, ale wyniki nie są równe 1.0

for _ in range(5):
    time_consuming_function()

print(time_consuming_function.get_stats())