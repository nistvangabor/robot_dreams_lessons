import time

def task1():
    print("Task 1 starting...")
    time.sleep(3)  # Simulates a delay in execution
    print("Task 1 completed.")

def task2():
    print("Task 2 starting...")
    time.sleep(3)
    print("Task 2 completed.")

# Running in a single thread
print("Single-threaded execution:")
task1()
task2()