import requests
import json
import os
import time
from logModule import logModule
class HttpUtil:
    def __init__(self):
        self.url = ""
        self.logger = logModule()
    def Put(self,url,body,headers):
        duration = -1
        try:
            startTime = time.time()
            response = requests.put(url=url,data=body,headers=headers)
            self.logger.debug(response.text)
            if response.status_code == 200 or response.status_code == 204:
                endTime = time.time()
                duration = endTime - startTime
                self.logger.debug(str(duration))
        except Exception as e:
            self.logger.error("Error is " + str(e))
        return duration
    
    def Get(self,url,headers):
        duration = -1
        try:
            startTime = time.time()
            response = requests.get(url=url,headers=headers)
            self.logger.debug(response.text)
            if response.status_code == 200:
                endTime = time.time()
                duration = endTime - startTime
                self.logger.debug(str(duration))
        except Exception as e:
            self.logger.error("Error is "+ str(e))

        return duration

    def Delete(self,url,headers):
        duration = -1
        try: 
            startTime = time.time()
            response = requests.delete(url=url,headers=headers)
            self.logger.debug(response.text)
            if response.status_code == 200 or response.status_code == 204:
                endTime = time.time()
                duration = endTime - startTime
                self.logger.debug(str(duration))
        except Exception as e:
            self.logger.error("Error is " + str(e))
        

        return duration

