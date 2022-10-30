from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    host = "https://duongnq9-project2-webapp.azurewebsites.net:443"
    wait_time = between(5, 10)

    @task
    def task1(self):
        self.client.get("/")