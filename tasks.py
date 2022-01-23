from celery import Celery
import time

app = Celery("tasks", broker="redis://localhost:6379/0")


@app.task
def run_long_task():
    print("Starting long task")
    time.sleep(10)
    return "Complete"
