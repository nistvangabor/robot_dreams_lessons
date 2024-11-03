import concurrent.futures
import threading
import time 
# Shared variable
counter = 0

# Lock for synchronizing access to the shared variable
counter_lock = threading.Lock()

def increment_counter(increment_value):
    global counter
    for _ in range(1000):
        with counter_lock:  # Lock to prevent race conditions
            counter += increment_value  # Increment by the specified value
    time.sleep(2)
    print(counter)
    return counter  # Return the counter value after incrementing

# Use ThreadPoolExecutor to manage threads
increment_amount = 5  # Example parameter
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # Submit tasks to the executor, passing the parameter as an argument
    futures = [
        executor.submit(increment_counter, increment_amount) for _ in range(5)
    ]

print(futures)
# Wait for all threads to complete and gather results
results = [future.result() for future in futures]
print(results)
# Final counter value after both threads finish
print(f"Final counter value: {counter}")