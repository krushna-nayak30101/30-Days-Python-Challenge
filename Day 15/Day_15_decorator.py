import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"⏱️ Execution Time: {end - start:.4f} seconds")
    return wrapper

@timer_decorator
def sample_task():
    time.sleep(2)  # Simulate a delay
    print("✅ Task completed.")

sample_task()
