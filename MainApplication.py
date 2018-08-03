from Dryer import Dryer
from Washer import Washer
from Oven import Oven
from Dishwasher import Dishwasher
from FridgeFreezer import FridgeFreezer
from CoffeeMaker import CoffeeMaker
import json
import os 
import time
from logModule import logModule
import random

url = ""
j_file = open("accesstoken",'r')
data = json.load(j_file)
j_file.close()
accessToken = data.get("access_token")
logger = logModule()
logger.info("API test starts")
getFlag = random.randint(0,1)
DryerID = ""
WasherID = ""
OvenID = ""
CoffeeMakerID = ""
FridgeFreezerID = ""
DishwasherID = ""  
dryer = Dryer(accessToken,DryerID,url)
washer = Washer(accessToken,WasherID,url)
oven = Oven(accessToken, OvenID, url)
dishwasher = Dishwasher(accessToken, DishwasherID,url)
freezer = FridgeFreezer(accessToken, FridgeFreezerID, url)
#coffeemaker = CoffeeMaker(accessToken, CoffeeMakerID, url)
if getFlag is 1:
    dryer.getStatus()
    washer.getStatus()
    dishwasher.getStatus()
    oven.getStatus()
    freezer.getStatus()
 #   coffeemaker.getStatus()
dryer.putProgram()
washer.putProgram()
freezer.changeTemperature()
oven.putProgram()
dishwasher.putProgram()
#coffeemaker.putProgram()
time.sleep(20)
dryer.stopProgram()
washer.stopProgram()
dishwasher.stopProgram()
oven.stopProgram()
