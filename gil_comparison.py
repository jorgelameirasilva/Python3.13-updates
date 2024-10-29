import time
import threading
import argparse

def count(n):
    """A simple CPU-bound task that counts down from n to 0."""
    while n > 0:
        n -= 1

def run_threads(num_threads, count_to):
    threads = []
    start = time.time()
    
    for _ in range(num_threads):
        t = threading.Thread(target=count, args=(count_to,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    end = time.time()
    print(f"Time taken with {num_threads} threads: {end - start:.2f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare GIL and GIL-free Python performance")
    parser.add_argument("--count", type=int, default=100_000_000, help="Number to count down from")
    args = parser.parse_args()

    count_to = args.count
    for num_threads in [1, 2, 4, 8]:
        run_threads(num_threads, count_to)
