import os
import json
from locust import HttpUser, TaskSet, task, between
from dotenv import load_dotenv

load_dotenv()

class WiremockLoadTest(HttpUser):
    wait_time = between(1, 5)

    host = os.getenv("TARGET_HOST", "http://localhost:8888")

    @task(1)
    def post_discharge(self):
        payload = {
            "serviceID": "DISCHARGE_OP"
        }
        headers = {
            "Content-Type": "application/json"
        }

        with self.client.post("/nahsehat", json=payload, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code == 404:
                response.failure("Not found or error occurred")
            else:
                response.failure(f"Error: {response.status_code}")