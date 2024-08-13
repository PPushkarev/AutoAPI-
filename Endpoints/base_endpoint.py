class Endpoint:
    response = None
    response_json = None

    def status_code(self):
        assert self.response.status_code == 200

    def status_code(self):
        assert self.response.status_code == 200
