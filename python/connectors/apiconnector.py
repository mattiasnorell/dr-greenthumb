import requests
from providers.Settings import Settings 

class ApiConnector:

    def __init__(self):
        self.settings = Settings()
        
    def get(self, endpoint):
        print(self.settings.config.api.basepath + endpoint)
        resp = requests.get(self.settings.config.api.basepath + endpoint)

        #if resp.status_code != 200:
            #raise ApiError("ApiError: ".format(restp-status_code))

        return resp.json()

    def post(self, endpoint, data):
        resp = requests.post(self.settings.config.api.basepath + endpoint, json = data)

        #if resp.status_code != 200:
            #raise ApiError("ApiError: ".format(restp-status_code))

        return resp.json()

  #  def delete(self, endpoint, data):
   #     resp = requests.delete(endpoint, data = data)