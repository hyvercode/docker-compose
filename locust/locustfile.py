from locust import HttpUser, task

class GrosirmobilAPI(HttpUser):
    @task
    def country(self):
         headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',  # Set your user agent
            'Authorization': 'Bearer 5379|r8jLU7KRuEXxDo8xiSgNndeKIgzfQV46cUyzPJPv',  # Set your authorization token if required
            'Content-Type': 'application/x-www-form-urlencoded',  # Add any custom headers you need
        }
        self.client.get("/api/country",headers=headers)
        @task

    def unit(self):
         headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',  # Set your user agent
            'Authorization': 'Bearer 5379|r8jLU7KRuEXxDo8xiSgNndeKIgzfQV46cUyzPJPv',  # Set your authorization token if required
            'Content-Type': 'application/x-www-form-urlencoded',  # Add any custom headers you need
        }
        self.client.get("/api/unit/4014",headers=headers)