'''
<다른 부분>
1. xai
2. graph
3. model output?
4. hpo convert 
5. model : hpo setting

<동일한 부분>
runTrain
runHpo
getTrainResult(안에서 fit, graph, xai 실행함)

<분류>
purposeType: reg, clf, clu, time 별로 그래프, xai fit 결과 다름
각 purposeType 안에서도 모델 별로 graph, xai, hpo다름
'''

import os
import sys
import time
import json
import numpy as np
import datetime
import pathlib
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import shap
import joblib


basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
modelPath = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir), os.path.pardir), "modeldata/model")) # modeldata 위치

sys.path.append(os.path.join(modelPath, "model"))
sys.path.append(os.path.join(modelPath, "bin"))
sys.path.append(os.path.join(basePath, "datalib"))
sys.path.append(os.path.join(basePath, "utils"))
sys.path.append(os.path.join(basePath, "decorator"))

from model import learningModel
from train import modelGraph
from dataLib import dataLib
from utils import utils
from sender import sendMsg
from logger.Logger import Logger

from error.WedaErrorDecorator import WedaErrorDecorator
from logger.WedaLogDecorator import WedaLogDecorator
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials, STATUS_FAIL



class trainer():
  # @WedaLogDecorator(text="Train Start...", logLevel="info")
  def __init__(self, param, xTrain, xTest, yTrain, yTest, xHoldout, yHoldout, log):
    self.model = None
    self.startTime = time.time()
    self.param = param
    self.dataInfo = param["dataInfo"] if "dataInfo" in param else None
    self.serverParam = param["serverParam"] if "serverParam" in param else None
    self.selectedHyperParam = utils.getHyperParam(param["selectedHyperParam"], modelPath) if param["selectedHyperParam"] else param["selectedHyperParam"]

    # self.modelInfo = param["dataInfo"]
    self.timeColumn = self.dataInfo.get("timeColumn", "")
    self.purposeType = self.dataInfo["purposeType"]
    self.labelColumnNm = self.dataInfo["targetColumn"]
    self.labelColumnNms = [ i["className"] for i in param["dataInfo"].get("classInfo", []) ]
    self.encodeData = self.dataInfo["encodeData"]
    self.columnNms = self.dataInfo["columnNameList"]

    self.originColumnNms = self.dataInfo["originColumnNameList"]
    if self.labelColumnNm in  self.originColumnNms:
      self.originColumnNms.remove(self.labelColumnNm)

    self.columnTypeDict = self.param.get("columnTypeDict", {})
    if not self.columnTypeDict:
      for i in self.dataInfo["columnList"]:
        self.columnTypeDict[i["columnName"]] = i["columnType"]
    self.param["columnTypeDict"] = self.columnTypeDict

    self.xTrain = xTrain
    self.xTest = xTest
    self.yTrain = yTrain
    self.yTest = yTest
    self.xHoldout = xHoldout
    self.yHoldout = yHoldout
    
    self.tryCount = 0
    self.orgLogPath = pathlib.Path(param["pathInfo"]["logPath"])
    self.log = log

  def hyperParamTuning(self, space):
    output = {
      "status": 200,
      "message": "",
      "extTime": None,
      "result": None,
    }

    st = time.time()
    startTime = datetime.datetime.now()

    try:
      model = learningModel(
        param_grid=space,
        param=self.param,
        log=self.log,
        startTime=startTime
      )
      model.setSpaceType()
      self.model = model.new_fit(X=self.xTrain, y=self.yTrain, log=log, saveYn=False)
      output, yPred, score = model.validation(xTrain=self.xTrain, xTest=self.xTest, yTrain=self.yTrain, yTest=self.yTest, model=self.model, log=log)
      print(score)
      return {"loss": 1 - score, "status": STATUS_OK, "model": model}
    except:
      return {"status": STATUS_FAIL}

  @WedaLogDecorator(text="Running Trainer...", logLevel="info")
  def getTrainResult(self, sendResultUrl, startTime, hpoTf, log):
    output = {
        "status": 200,
        "message": "",
        "extTime": None,
        "result": None,
    }

    param_grid = self.selectedHyperParam
    model = learningModel(
        param_grid=param_grid,
        param=self.param,
        log=self.log,
        startTime=startTime
    )

    # model fit
    if hpoTf:
      self.model = model.new_fit(X=self.xTrain, y=self.yTrain, log=log, saveYn=True)
    else:
      self.model = model.fit(X=self.xTrain, y=self.yTrain, log=log, saveYn=True)

    if self.purposeType=="timeSeries":
      output = model.validation(xTest=self.xHoldout, yTest=self.yHoldout, model=self.model, log=log)
    else:
      output = model.validation(xTest=self.xTest, yTest=self.yTest, model=self.model, log=log)
    
    _ = sendMsg(sendResultUrl, output, "TRAIN", log)
    return output
      
      
  def getGraphResult(self, result, sendResultUrl, log):
      output = {
          "status": 200,
          "message": "",
          "extTime": None,
          "result": None,
      }
      score = result["score"]
      yPred = result["yPred"]
      
      yPred = list(map(lambda x: round(x, 4), yPred))
      print(score)
      
      mG = modelGraph(self.param, self.xTrain, self.xTest, self.yTrain, self.yTest, self.xHoldout, self.yHoldout, self.model, log)

      graphResult = mG.getGraphData(yPred=yPred, score=score, model=self.model, log=log)

      output["result"] = graphResult["result"]
      output["selectedHyperParam"] = self.selectedHyperParam

      _ = sendMsg(sendResultUrl, output, "GRAPH", log)

      partialDict, columnFlag = mG.makeFeatureEffect(log=log)
      xaiResult = mG.getXAIData(yPred=yPred, partialDict=partialDict, columnFlag=columnFlag, log=log)

      output["result"] = xaiResult["result"]
      output["extTime"] = time.time() - self.startTime
      _ = sendMsg(sendResultUrl, output, "XAI", log)
      
      return output


# opr에서 모델 입출력 스키마 정의
def setModelInfo(scheme):
    subList = []
    for i in scheme["dataInfo"]["columnList"]:
      subList.append({
        "type": "string" if i["columnType"] == "string" else "number",
        "name": i["columnName"]
      })

    inputScheme = [
      {
        "type": "object",
        "name": "opData",
        "subObject": [
          {
            "type": "array",
            "name": "header",
            "subList": subList
          },
          {
            "type": "array",
            "name": "xTest"
          }
        ]
      }
    ]
    
    # output 타입, 분류 등 다른 모델에서 OPR에서 다르게 나올 경우 수정 필요
    subList.append({
          "type": "string",
          "name": "errMessage"
        })
    subList.append({        
          "type": "number",
          "name": "label"
        })
    subList.append(                   
        {
          "type": "number",
          "name": "accuracy"
        })
    
    outputScheme = [
    {
      "type": "array",
      "name": "opResult",
      "subList": subList
    },
    {
      "type": "string",
      "name": "modelId"
    }
  ]
    with open(os.path.join(modelPath, "modelInfo.json"), "r+") as jsonFile:
      file_data = json.load(jsonFile)
      file_data["ioScheme"] = {}
      file_data["ioScheme"]["inputScheme"] = inputScheme
      file_data["ioScheme"]["outputScheme"] = outputScheme
      jsonFile.seek(0)
      json.dump(file_data, jsonFile, indent = 4)
      

@WedaErrorDecorator
@WedaLogDecorator(text="Model Training...", logLevel="info")
def runTrain(params, log, startTime, sendResultUrl):
  # 데이터 취득
  dl = dataLib(param=params, log=log)
  data = dl.getData(log=log)

  xTrain = data["result"]["xTrain"]
  xTest = data["result"]["xTest"]
  yTrain = data["result"]["yTrain"]
  yTest = data["result"]["yTest"]
  xHoldout = data["result"].get("xHoldout", [])
  yHoldout = data["result"].get("yHoldout", [])

  # 시계열에만 holdout 있음
  if params.get("timeColumn", "") != "":
    xHoldout = np.concatenate((xTest, xHoldout), axis=0)
    yHoldout = np.concatenate((yTest, yHoldout), axis=0)
  
  t = trainer(param=dl.param, xTrain=xTrain, xTest=xTest, yTrain=yTrain, yTest=yTest, xHoldout=xHoldout, yHoldout=yHoldout, log=log)

  # train/validation
  result = t.getTrainResult(sendResultUrl=sendResultUrl, startTime=startTime, hpoTf=False, log=log)
  output = t.getGraphResult(result=result, sendResultUrl=sendResultUrl, log=log)
  
  classInfo = {
    "classInfo": [{
        "className": t.labelColumnNm
    }]
  }

  t.param["dataInfo"]["classInfo"] = classInfo
  output["classInfo"] = classInfo

  #opr에서 모델 입출력 스키마 정의 함수 호출
  setModelInfo(t.param)

  with open(os.path.join(basePath, "param.json"), "w") as jsonFile:
      json.dump(t.param, jsonFile, ensure_ascii=False)
      
      
@WedaErrorDecorator
@WedaLogDecorator(text="Model Training...", logLevel="info")
def runHPO(params, log, startTime, sendResultUrl):

    # 데이터 취득
    dl = dataLib(param=params, log=log)
    data = dl.getData(log=log)

    xTrain = data["result"]["xTrain"]
    xTest = data["result"]["xTest"]
    yTrain = data["result"]["yTrain"]
    yTest = data["result"]["yTest"]
    xHoldout = data["result"].get("xHoldout", [])
    yHoldout = data["result"].get("yHoldout", [])

    t = trainer(param=dl.param, xTrain=xTrain, xTest=xTest, yTrain=yTrain, yTest=yTest, xHoldout=xHoldout, yHoldout=yHoldout, log=log)
    space = learningModel.getSpace()

    if 'trialCount' in t.param:
        trialCount = int(t.param["trialCount"])
    else:
        trialCount = 10

    # Trials 객체 선언합니다.
    trials = Trials()

    # best에 최적의 하이퍼 파라미터를 return 받습니다.
    best = fmin(fn=t.hyperParamTuning,
                space=space,
                algo=tpe.suggest,
                max_evals=trialCount, # 최대 반복 횟수를 지정합니다.
                trials=trials)

    best = t.convertParam(best)

    # 최적화된 결과를 int로 변환해야하는 파라미터는 타입 변환을 수행합니다.
    for key in best:
        if type(best[key]) == np.float64:
            best[key] = round(float(best[key]),5)
        elif type(best[key]) == np.int64:
            best[key] = int(best[key])
    dl.param["selectedHyperParam"].update(best)

    _ = sendMsg(sendResultUrl, dl.param["selectedHyperParam"], "HYPER", log)

    re = trainer(param=dl.param, xTrain=xTrain, xTest=xTest, yTrain=yTrain, yTest=yTest, xHoldout=xHoldout, yHoldout=yHoldout, log=log)
    output = re.getTrainResult(log=log, hpoTf=True)
    

    classInfo = {
        "classInfo": [{
            "className": re.labelColumnNm
        }]
    }

    re.param["dataInfo"]["classInfo"] = classInfo
    output["classInfo"] = classInfo

    print("re train done")

    #opr에서 모델 입출력 스키마 정의 함수 호출
    setModelInfo(re.param)

    with open(os.path.join(basePath, "param.json"), "w") as jsonFile:
        json.dump(re.param, jsonFile, ensure_ascii=False)
        
  