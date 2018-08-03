import os
import json
import random
from logModule import logModule
from HttpUtil import HttpUtil
class FridgeFreezer:

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
            self.logger.info("Get Status in "+ str(duration)+ " seconds")
        else:
            self.logger.error("Fail to operate HA due to unknown reason")

    def changeTemperature(self):
        program = ""
        randomPick = random.randint(0,3)
        if randomPick is 0:
            settingKey = "Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer"
            Temperature = random.randint(-24,-16)
            body = {"data":{"key":"Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer","value":Temperature,"unit":"°C"}}
            program = "Freezer Temperature"
        elif randomPick is 1:
            settingKey = "Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator"
            Temperature = random.randint(2,8)
            body = {"data":{"key":"Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefridgerator","value":Temperature,"unit":"°C"}}
            program = "Refrigerator Temperature"
        elif randomPick is 2:
            settingKey = "Refrigeration.FridgeFreezer.Setting.SuperModeFreezer"
            body = {"data":{"key":"Refrigeration.FridgeFreezer.Setting.SuperModeFreezer","value":True}}
            program = "Super Mode Freezer"
        elif randomPick is 3:
            settingKey = "Refrigeration.FridgeFreezer.Setting.SuperModeRefrigerator"
            body = {"data":{"key":"Refrigeration.FridgeFreezer.Setting.SuperModeRefrigerator","value":True}}
            program = "Super Mode Refridgerator"
        url = self.url + self.haID + "/settings/" + settingKey
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
            print ("program stops in "+ str(duration)+ " seconds")
        else:
            print ("Failed to operate HA due to unknown reason")

