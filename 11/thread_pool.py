from concurrent.futures import ThreadPoolExecutor
import time

def task(name, duration):
    print(f"Task {name} starting...")
    time.sleep(duration)
    print(f"Task {name} completed.")

# Create a ThreadPoolExecutor with 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to the pool
    executor.submit(task, "A", 2)
    executor.submit(task, "B", 1)
    executor.submit(task, "C", 3)
    executor.submit(task, "D", 3)
    executor.submit(task, "E", 3)
    executor.submit(task, "F", 3)
    executor.submit(task, "G", 3)