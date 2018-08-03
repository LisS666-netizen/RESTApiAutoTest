import os
import json
import random
from logModule import logModule
from HttpUtil import HttpUtil
class Oven:

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
        randomPick = (random.randint(0,20)%3)
        if randomPick is 0:
            body = {"data":{"key":"Cooking.Oven.Program.HeatingMode.PreHeating","options":[{"key":"Cooking.Oven.Option.SetpointTemperature","value":230,"unit":"°C"},{"key":"BSH.Common.Option.Duration","value":1200,"unit":"seconds"}]}}
            program = "PreHeating"
        elif randomPick is 1:
            body = {"data":{"key":"Cooking.Oven.Program.HeatingMode.HotAir","options":[{"key":"Cooking.Oven.Option.SetpointTemperature","value":230,"unit":"°C"},{"key":"BSH.Common.Option.Duration","value":1200,"unit":"seconds"}]}}
            program = "HotAir"
        elif randomPick is 2:
            body = {"data":{"key":"Cooking.Oven.Program.HeatingMode.TopBottomHeating","options":[{"key":"Cooking.Oven.Option.SetpointTemperature","value":230,"unit":"°C"},{"key":"BSH.Common.Option.Duration","value":1200,"unit":"seconds"}]}}
            program = "TopBottomHeating"
        elif randomPick is 3:
            body = {"data":{"key":"Cooking.Oven.Program.HeatingMode.PizzaSetting","options":[{"key":"Cooking.Oven.Option.SetpointTemperature","value":230,"unit":"°C"},{"key":"BSH.Common.Option.Duration","value":1200,"unit":"seconds"}]}}
            program = "Eco 50 degree"
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

