import requests
from flask import abort
from providers.Settings import Settings 

class ApiConnector:

    def __init__(self):
        self.settings = Settings()
        
    def get(self, endpoint):
        resp = requests.get(self.settings.config.api.basepath + endpoint)

        if resp.status_code != 200:
            return { 'status': resp.status_code }

        return { 'status': resp.status_code, 'data': resp.json() }

    def post(self, endpoint, data):
        resp = requests.post(self.settings.config.api.basepath + endpoint, json = data)

        if resp.status_code != 200:
            return { 'status': resp.status_code }

        return { 'status': resp.status_code, 'data': resp.json() }

  #  def delete(self, endpoint, data):
   #     resp = requests.delete(endpoint, data = data)