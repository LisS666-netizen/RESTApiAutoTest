import os
import json
import random
from logModule import logModule
from HttpUtil import HttpUtil
class Dishwasher:

    def __init__(self,token,haID, url):
        self.token = "Bearer " + token
        self.haID = haID
        self.url = url
        self.headers = {"Accept":"application/vnd.bsh.sdk.v1+json","Content-Type":"application/json","Authorization": self.token}
        self.httputil = HttpUtil()
        self.logger = logModule()
    def getStatus(self):
        url = self.url + self.haID + "/status"
        self.logger.debug(url)
        duration = self.httputil.Get(url,self.headers)
        if duration is not -1:
            self.logger.info("Get Status in "+ str(duration) + " seconds")
        else:
            self.logger.error("Fail to operate HA due to unknown reason")

    def putProgram(self):
        program = ""
        randomPick = (random.randint(0,4))
        if randomPick is 0:
            body = {"data":{"key":"Dishcare.Dishwasher.Program.Auto1","options":[{"key":"BSH.Common.Option.StartInRelative","value":1800,"unit":"seconds"}]}}
            program = "Auto 35-45 degree"
        elif randomPick is 1:
            body = {"data":{"key":"Dishcare.Dishwasher.Program.Auto2","options":[{"key":"BSH.Common.Option.StartInRelative","value":1800,"unit":"seconds"}]}}
            program = "Auto 45-65 degree"
        elif randomPick is 2:
            body = {"data":{"key":"Dishcare.Dishwasher.Program.Auto3","options":[{"key":"BSH.Common.Option.StartInRelative","value":1800,"unit":"seconds"}]}}
            program = "Auto 65-75 degree"
        elif randomPick is 3:
            body = {"data":{"key":"Dishcare.Dishwasher.Program.Eco50","options":[{"key":"BSH.Common.Option.StartInRelative","value":1800,"unit":"seconds"}]}}
            program = "Eco 50 degree"
        elif randomPick is 4:
            body = {"data":{"key":"Dishcare.Dishwasher.Program.Quick45","options":[{"key":"BSH.Common.Option.StartInRelative","value":1800,"unit":"seconds"}]}} 
            program = "Quick45" 
        url = self.url + self.haID + "/programs/active"
        self.logger.debug(url)
        bodyJson = json.dumps(body)
        duration = self.httputil.Put(url,bodyJson,self.headers)
        if duration is not -1:
            self.logger.info(program + " starts in " + str(duration) + " seconds")
        else:
            self.logger.error("Failed to operation HA due to unknown reason")

    def stopProgram(self):
        url = self.url + self.haID + "/programs/active"
        duration = self.httputil.Delete(url,self.headers)
        if duration is not -1:
            self.logger.info("program stops in "+ str(duration)+ " seconds")
        else:
            self.logger.error("Failed to operate HA due to unknown reason")
