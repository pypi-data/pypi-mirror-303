import requests
import json


class postprocessing():
    def __init__(self, data):
        self.data = data

    def sendTargetServer(self, data):
        sendUrl = "http://0.0.0.0:80/result/"
        headers = {"Content-Type": "application/json; charset=utf-8"}
        return requests.post(sendUrl, headers=headers, data=json.dumps(data))

    def run(self):
        # self.sentTargetServer(self.data)
        return 0
