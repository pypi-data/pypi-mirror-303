import os
import sys
import time
import json
import numpy as np
import pathlib



basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
modelPath = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir), os.path.pardir), "modeldata/model")) # modeldata 위치

sys.path.append(os.path.join(modelPath, "model"))
sys.path.append(os.path.join(modelPath, "bin"))
sys.path.append(os.path.join(basePath, "datalib"))
sys.path.append(os.path.join(basePath, "utils"))
sys.path.append(os.path.join(basePath, "decorator"))

from model import customModel

from dataLib import dataLib
from utils import utils
from sender import sendMsg
from logger.Logger import Logger

from error.WedaErrorDecorator import WedaErrorDecorator
from logger.WedaLogDecorator import WedaLogDecorator



class trainer(): 
    def __init__(self, param, log):
        self.model = None
        self.startTime = time.time()
        self.param = param

        self.orgLogPath = pathlib.Path(param["pathInfo"]["logPath"])
        self.log = log
        
    @WedaLogDecorator(text="Running Trainer...", logLevel="info")
    def getTrainResult(self, sendResultUrl, startTime, log):
        output = {
            "status": 200,
            "message": "",
            "extTime": None,
            "result": None,
        }

        print(self.param["dataPath"],self.param)
        self.model = customModel()
        self.model.main(dataPath=self.param["dataPath"],param=self.param)

        _ = sendMsg(sendResultUrl, output, "TRAIN", log)
        
        return output
      


@WedaErrorDecorator
@WedaLogDecorator(text="Model Training...", logLevel="train")
def runTrain(params, log, startTime, sendResultUrl): 
    
    t = trainer(param=params, log=log)
    output = t.getTrainResult(sendResultUrl=sendResultUrl, startTime=startTime, log=log)
    with open(os.path.join(modelPath, "param.json"), "w") as jsonFile:
        json.dump(t.param, jsonFile, ensure_ascii=False)
      
      