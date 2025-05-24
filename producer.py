import time
import redis

r = redis.Redis(host='redis', port=6379, db=0)

for i in range(1, 21):  # Only produce Task-1 to Task-20
    task = f"Task-{i}"
    r.lpush("task_queue", task)
    print(f"Produced: {task}")
    time.sleep(1)  # simulate delay

