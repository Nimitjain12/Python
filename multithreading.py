# import threading
# import time
#
# def disp(thread_name):
#     for i in range(5):
#         #time.sleep(1)
#         current_thread = threading.current_thread()
#         print(f"Thread Name: {current_thread.name}")
#         print(f"{thread_name} - {i}")
#
# # Creating threads
# thread1 = threading.Thread(target=disp, args=("First_Thread",))
# thread2 = threading.Thread(target=disp, args=("Second_Thread",))
#
# # Starting threads
# thread1.start()
# thread2.start()
#
# # Wait for both threads to finish
# thread1.join()
# thread2.join()
#
# print("guess who is running main")
# current_thread = threading.current_thread()
# print(f"Thread Name: {current_thread.name}")
# print("All threads finished.")



"""
Shared Resource: counter is a global variable
that is shared between threads.

Lock Creation: counter_lock is a lock object
( Lock class) that will be used to synchronize
access to the counter.

So in this example,the lock is created on the instance of Lock class from the threading module. This lock is used to synchronize access to the shared resource, "counter".

Whenever a thread wants to modify the "counter", it must first acquire the lock using a context manager (with counter_lock:). This ensures that only one thread can modify counter at a time, preventing race conditions. When one thread holds the lock, the other thread must wait until the lock is released before it can proceed with its own modifications to "counter".

"""

import threading
import time

# Shared resource
# counter = 0
#
# # Create a lock
# counter_lock = threading.Lock()
#
# def increment_counter():
#     global counter
#     for _ in range(10):
#         # Acquire the lock before accessing the shared resource
#         with counter_lock:
#             counter += 1
#         print("Counter incrementing\t",counter)
#
# def decrement_counter():
#     global counter
#     for _ in range(10,1,-1):
#         # Acquire the lock before accessing the shared resource
#         with counter_lock:
#             counter -= 1
#         print("Counter decrementing\t",counter)
#
# # Create threads
# thread1 = threading.Thread(target=increment_counter)
# thread2 = threading.Thread(target=decrement_counter)
#
# # Start threads
# thread1.start()
# thread2.start()

# Wait for both threads to finish
#thread1.join()  # try commenting this
#thread2.join()  # try commenting this

# there is no guarantee of main thread will
# complete at the end if you don't use "join"

# Final counter value
# print("\n\n\n")
# print(f"Final counter value: {counter}")

# import threading
# import time
# class MyClass:
#     def disp(self):
#         # Synchronize access to this method using a lock
#         with self.lock:
#             for i in range(10):
#                 print(f"Hello\t{i}")
#                 time.sleep(1)
#
#     def __init__(self):
#         self.lock = threading.Lock()  # Create a lock for synchronization
#
#
# def main():
#     m1 = MyClass()  # Shared instance of MyClass
#     m2 = MyClass() # try this
#     thread1 = threading.Thread(target=m1.disp)
#     thread2 = threading.Thread(target=m1.disp)
#     #thread2 = threading.Thread(target=m2.disp)  # try this
#     thread1.start()
#     thread2.start()
#
#
# if __name__ == "__main__":
#     main()

import threading

class MyClass:
    def __init__(self):
        self.lock = threading.Lock()  # Create a lock for synchronization
        self.condition = threading.Condition(self.lock)  # Create a condition variable
        self.current_thread = "ascending"  # Track the current thread

    def disp(self):
        with self.lock:
                for i in range(10):
                    print(f"Ascending: {i}\t{threading.current_thread().name}")
                    if i == 5:
                        self.condition.notify()  # Notify the descending
                        self.condition.wait()  # Wait for the descending thread to finish
                self.condition.notify()


def main():
    m1 = MyClass()  # Shared instance of MyClass
    thread1 = threading.Thread(target=m1.disp, name="First_Thread")
    thread2 = threading.Thread(target=m1.disp, name="Second_Thread")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()