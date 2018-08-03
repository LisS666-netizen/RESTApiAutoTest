import os
import json
import random
from logModule import logModule
from HttpUtil import HttpUtil
class CoffeeMaker:

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
        randomPick = (random.randint(0,5))
        if randomPick is 0:
            body = {"data":{"key":"ConsumerProducts.CoffeeMaker.Program.Beverage.Espresso","options":[{"key":"ConsumerProducts.CoffeeMaker.Option.BeanAmount","value":"ConsumerProducts.CoffeeMaker.EnumType.BeanAmount.Mild"},{"key":"ConsumerProducts.CoffeeMaker.Option.FillQuantity","value":45,"unit":"ml"}]}}
            program = "Espresso"
        elif randomPick is 1:
            body = {"data":{"key":"ConsumerProducts.CoffeeMaker.Program.Beverage.EspressoMacchiato","options":[{"key":"ConsumerProducts.CoffeeMaker.Option.BeanAmount","value":"ConsumerProducts.CoffeeMaker.EnumType.BeanAmount.Mild"},{"key":"ConsumerProducts.CoffeeMaker.Option.FillQuantity","value":50,"unit":"ml"}]}}
            program = "HotAir"
        elif randomPick is 2:
            body = {"data":{"key":"ConsumerProducts.CoffeeMaker.Program.Beverage.Coffee","options":[{"key":"ConsumerProducts.CoffeeMaker.Option.BeanAmount","value":"ConsumerProducts.CoffeeMaker.EnumType.BeanAmount.Mild"},{"key":"ConsumerProducts.CoffeeMaker.Option.FillQuantity","value":120,"unit":"ml"}]}}
            program = "TopBottomHeating"
        elif randomPick is 3:
            body = {"data":{"key":"ConsumerProducts.CoffeeMaker.Program.Beverage.Cappuccino","options":[{"key":"ConsumerProducts.CoffeeMaker.Option.BeanAmount","value":"ConsumerProducts.CoffeeMaker.EnumType.BeanAmount.Mild"},{"key":"ConsumerProducts.CoffeeMaker.Option.FillQuantity","value":180,"unit":"ml"}]}}
            program = "Cappuccino"
        elif randomPick is 4:
            body = {"data":{"key":"ConsumerProducts.CoffeeMaker.Program.Beverage.LatteMacchiato","options":[{"key":"ConsumerProducts.CoffeeMaker.Option.BeanAmount","value":"ConsumerProducts.CoffeeMaker.EnumType.BeanAmount.Mild"},{"key":"ConsumerProducts.CoffeeMaker.Option.FillQuantity","value":320,"unit":"ml"}]}}
            program = "Latte Macchiato"
        elif randomPick is 5:
            body = {"data":{"key":"ConsumerProducts.CoffeeMaker.Program.Beverage.CaffeLatte","options":[{"key":"ConsumerProducts.CoffeeMaker.Option.BeanAmount","value":"ConsumerProducts.CoffeeMaker.EnumType.BeanAmount.Mild"},{"key":"ConsumerProducts.CoffeeMaker.Option.FillQuantity","value":240,"unit":"ml"}]}}
            program = "Caffe Latte"
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

