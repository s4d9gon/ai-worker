import time

def run_worker():
    print("Worker online ✓")
    while True:
        print("Processing batch...")
        time.sleep(5)
