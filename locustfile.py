from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")

class HeavierLoadUser(HttpUser):
    @task
    def hello_heavier(self):
        self.client.get("/heavier")
