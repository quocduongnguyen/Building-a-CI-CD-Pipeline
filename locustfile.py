from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    host = "https://duongnq9-project2-webapp.azurewebsites.net:443"
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")