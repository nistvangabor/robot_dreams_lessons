import multiprocessing
import time

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(lower_limit, upper_limit):
    """Count prime numbers in a specific range."""
    return sum(1 for n in range(lower_limit, upper_limit) if is_prime(n))

def worker(lower_limit, upper_limit, queue):
    """Worker function to count primes in a specific range and put the result in the queue."""
    result = count_primes_in_range(lower_limit, upper_limit)
    queue.put(result)

def single_process_execution(limit):
    """Count primes using a single process."""
    print("Counting primes using a single process:")
    start_time = time.time()
    result_single = count_primes_in_range(0, limit)
    end_time = time.time()
    print(f"Number of primes up to {limit} (single process): {result_single}")
    print(f"Time taken (single process): {end_time - start_time:.2f} seconds\n")

def multiple_process_execution(limit):
    """Count primes using multiple processes."""
    print("Counting primes using multiple processes:")
    start_time = time.time()
    
    queue = multiprocessing.Queue()  # Create a queue for results
    processes = []
    
    # Divide the workload for multiple processes
    step = limit // multiprocessing.cpu_count()
    for i in range(multiprocessing.cpu_count()):
        lower_limit = i * step
        upper_limit = limit if i == multiprocessing.cpu_count() - 1 else (i + 1) * step
        process = multiprocessing.Process(target=worker, args=(lower_limit, upper_limit, queue))
        processes.append(process)
        process.start()

    # Collect results from the queue
    
    # Wait for all processes to complete
    for process in processes:
        process.join()

    results_multiple = [queue.get() for _ in processes]

    total_primes = sum(results_multiple)  # Combine results from all processes
    end_time = time.time()
    print(f"Number of primes up to {limit} (multiple processes): {total_primes}")
    print(f"Time taken (multiple processes): {end_time - start_time:.2f} seconds")

def main():
    limit = 5000000  # Adjust the limit for larger calculations
    
    # Run single process execution
    single_process_execution(limit)

    # Run multiple process execution
    multiple_process_execution(limit)

if __name__ == "__main__":
    main()
