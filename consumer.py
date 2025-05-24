import time
import redis

r = redis.Redis(host='redis', port=6379, db=0)

while True:
    task = r.brpop("task_queue", timeout=5)  # wait max 5 seconds for a task
    if task:
        task_name = task[1].decode('utf-8')
        print(f"Consumed: {task_name}")
    else:
        print("No more tasks. Exiting.")
        break
    time.sleep(1)  # simulate task processing delay
