import os 
import json 
import random
from logModule import logModule
from HttpUtil import HttpUtil
class Dryer:

    def __init__(self,token,haID, url):
        self.token = "Bearer " + token
        self.haID = haID
        self.url = url
        self.headers = {"Accept":"application/vnd.bsh.sdk.v1+json","Content-Type":"application/json","Authorization": self.token}
        self.httputil = HttpUtil()
        self.logger = logModule()        
    def getStatus(self):
        url = self.url + self.haID + "/status"
        print (url)
        duration = self.httputil.Get(url,self.headers)
        if duration is not -1:
            self.logger.info("Get Status in "+ str(duration) + " seconds")
        else:
            self.logger.error("Fail to operate HA due to unknown reason")

    def putProgram(self):
        program = ""
        randomPick = (random.randint(0,9)%3)
        if randomPick is 0:
            body = {"data":{"key":"LaundryCare.Dryer.Program.Cotton","options":[{"key":"LaundryCare.Dryer.Option.DryingTarget","value":"LaundryCare.Dryer.EnumType.DryingTarget.CupboardDry"}]}}
            program = "Cotton"
        elif randomPick is 1:
            body = {"data":{"key":"LaundryCare.Dryer.Program.Synthetic","options":[{"key":"LaundryCare.Dryer.Option.DryingTarget","value":"LaundryCare.Dryer.EnumType.DryingTarget.CupboardDry"}]}}
            program = "Synthetic"
        elif randomPick is 2:
            body = {"data":{"key":"LaundryCare.Dryer.Program.Mix","options":[{"key":"LaundryCare.Dryer.Option.DryingTarget","value":"LaundryCare.Dryer.EnumType.DryingTarget.CupboardDry"}]}}
            program = "Mix"
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
