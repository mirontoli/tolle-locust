from locust import HttpUser, task

class HeavierLoadUser(HttpUser):
    @task
    def hello_heavier(self):
        self.client.get("/heavier")