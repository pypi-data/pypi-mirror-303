import time
from functools import wraps
from typing import Callable, TypeVar, Any

# Define type variables for better type inference
F = TypeVar('F', bound=Callable[..., Any])

class RateLimiter:
    def __init__(self, rate_limit: int, period: float):
        self.rate_limit = rate_limit  # Max number of calls
        self.period = period          # Time window in seconds
        self.calls = []
    
    def __call__(self, func: F) -> F:
        @wraps(func)
        def wrapped(*args, **kwargs):
            now = time.time()

            # Remove expired calls
            self.calls = [call for call in self.calls if now - call < self.period]

            if len(self.calls) >= self.rate_limit:
                sleep_time = self.period - (now - self.calls[0])
                time.sleep(sleep_time)

            self.calls.append(time.time())
            return func(*args, **kwargs)
        return wrapped
