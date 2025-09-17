import multiprocessing
import time
from .prime_utils import is_prime


def multi_process(numbers: list[int], workers: int = None) -> tuple[int, float]:
    start = time.time()
    with multiprocessing.Pool(processes=workers) as pool:
        results = pool.map(is_prime, numbers)
    prime_count = sum(results)
    elapsed = time.time() - start
    return prime_count, elapsed
