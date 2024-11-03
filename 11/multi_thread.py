import threading
import time

heap_var = "stored on heap"

def task1():
    stack_var = "stack var 1"
    print("Task 1 starting...")
    time.sleep(3)
    print(heap_var)
    print(stack_var)
    print("Task 1 completed...")

def task2():
    stack_var = "stack var 2"
    print("Task 2 starting...")
    time.sleep(3)
    print(heap_var)
    print(stack_var)
    print("Task 2 completed...")

print("Running on multiple threads")

thread_1 = threading.Thread(target=task1)
thread_2 = threading.Thread(target=task2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("test")