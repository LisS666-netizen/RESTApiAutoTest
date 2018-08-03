import os
import json
import random
from logModule import logModule
from HttpUtil import HttpUtil
class Washer:

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
        randomPick = (random.randint(0,20)%5)
        if randomPick is 0:
            body = {"data":{"key":"LaundryCare.Washer.Program.Cotton","options":[{"key":"LaundryCare.Washer.Option.Temperature","value":"LaundryCare.Washer.EnumType.Temperature.GC30"},{"key":"LaundryCare.Washer.Option.SpinSpeed","value":"LaundryCare.Washer.EnumType.SpinSpeed.RPM800"}]}}
            program = "Cotton"
        elif randomPick is 1:
            body = {"data":{"key":"LaundryCare.Washer.Program.EasyCare","options":[{"key":"LaundryCare.Washer.Option.Temperature","value":"LaundryCare.Washer.EnumType.Temperature.GC30"},{"key":"LaundryCare.Washer.Option.SpinSpeed","value":"LaundryCare.Washer.EnumType.SpinSpeed.RPM800"}]}}
            program = "EasyCare"
        elif randomPick is 2:
            body = {"data":{"key":"LaundryCare.Washer.Program.Mix","options":[{"key":"LaundryCare.Washer.Option.Temperature","value":"LaundryCare.Washer.EnumType.Temperature.GC30"},{"key":"LaundryCare.Washer.Option.SpinSpeed","value":"LaundryCare.Washer.EnumType.SpinSpeed.RPM800"}]}}
            program = "Mix"
        elif randomPick is 3:
            body = {"data":{"key":"LaundryCare.Washer.Program.Wool","options":[{"key":"LaundryCare.Washer.Option.Temperature","value":"LaundryCare.Washer.EnumType.Temperature.GC30"},{"key":"LaundryCare.Washer.Option.SpinSpeed","value":"LaundryCare.Washer.EnumType.SpinSpeed.RPM800"}]}}
            program = "Wool"
        elif randomPick is 4:
            body = {"data":{"key":"LaundryCare.Washer.Program.DelicatesSilk","options":[{"key":"LaundryCare.Washer.Option.Temperature","value":"LaundryCare.Washer.EnumType.Temperature.GC30"},{"key":"LaundryCare.Washer.Option.SpinSpeed","value":"LaundryCare.Washer.EnumType.SpinSpeed.RPM800"}]}}
            program = "Delicates Silk"

        url = self.url + self.haID + "/programs/active"
        self.logger.debug(url)
        bodyJson = json.dumps(body)
        duration = self.httputil.Put(url,bodyJson,self.headers)
        if duration is not -1:
            self.logger.info(program + " starts in " + str(duration)+ " seconds")
        else:
            self.logger.error("Failed to operation HA due to unknown reason")

    def stopProgram(self):
        url = self.url + self.haID + "/programs/active"
        duration = self.httputil.Delete(url,self.headers)
        if duration is not -1:
            self.logger.info("program stops in "+ str(duration)+ " seconds")
        else:
            self.logger.error("Failed to operate HA due to unknown reason")

