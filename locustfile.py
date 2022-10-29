from locust import Locust, TaskSet, task

class UserTaskSet(TaskSet):
    @task
    def my_task(self):
        print("executing my_task")

class User(Locust):
    task_set = UserTaskSet
    min_wait = 5000
    max_wait = 15000