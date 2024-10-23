"""
MIT License

Copyright (c) 2021 WEDA CORP.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import sys
import time
import json
import numpy as np
import datetime
import pandas as pd
import shap
import joblib
from sklearn.preprocessing import LabelEncoder

basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
commonPath = os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),"common") # os.path.abspath("../common")
# modelPath = "../../legacy" # modeldata 위치

sys.path.append(basePath)
sys.path.append(commonPath)

from hyperopt import fmin, tpe, hp, STATUS_OK, Trials, STATUS_FAIL
from sender.sender import sendMsg
from graph.graph import graph
from logger.WedaLogDecorator import WedaLogDecorator
from error.WedaErrorDecorator import WedaErrorDecorator
from logger.Logger import Logger
from datalib.dataLib import dataLib
from utils.utils import utils

# from wedaLib.reg import regDecorator


class trainer:
    # @WedaLogDecorator(text="Train Start...", logLevel="info")
    def __init__(self, param, xTrain, xTest, yTrain, yTest, startTime, lm, log=None):

        self.param = param
        self.startTime = startTime
        self.dataInfo = param["dataInfo"] if "dataInfo" in param else None
        self.serverParam = param["serverParam"] if "serverParam" in param else None
        self.selectedHyperParam = param["selectedHyperParam"]

        self.timeColumn = self.dataInfo.get("timeColumn", "")
        self.purposeType = self.dataInfo["purposeType"]
        self.targetColumn = self.dataInfo["targetColumn"]
        self.classList = [
            i["className"] for i in param["dataInfo"].get("classInfo", [])
        ]
        self.encodeData = self.dataInfo["encodeData"]
        self.columnList = self.dataInfo["columnNameList"]

        self.originColumnNms = self.dataInfo["originColumnNameList"]
        if self.targetColumn in  self.originColumnNms:
            self.originColumnNms.remove(self.targetColumn)


        self.originColumnList = self.dataInfo["originColumnNameList"]
        if self.targetColumn in self.originColumnList:
            self.originColumnList.remove(self.targetColumn)

        self.hyperscheme = param.get("hyperParamScheme", {})
        self.weightPath = param.get("savePath", "./")
        self.saveMdlPath = os.path.join(self.weightPath, "weight.pkl")

        self.columnTypeDict = {}
        for i in self.dataInfo["columnList"]:
            self.columnTypeDict[i["columnName"]] = i["columnType"]
        self.param["columnTypeDict"] = self.columnTypeDict

        # 애매한 변수들
        self.customLM = lm
        self.log = log
        self.hyperParamScheme = param["hyperParamScheme"]
        # 데이터셋
        self.xTrain = xTrain
        self.xTest = xTest
        self.yTrain = yTrain
        self.yTest = yTest

        # 그래프 생성
        self.graphTf = param.get("graphTf", False)
        self.xaiTf = param.get("xaiTf", False)
        self.graphList = param["dataInfo"].get("graphList", [])

        # 모델 학습에 필요한 파라미터
        self.model = None
        self.scoreMethod = param.get("scoreMethod", "r2")

        # hyperParamScheme, hpo space에 사용
        self.hyperParamScheme = param.get("hyperParamScheme", {})

    @WedaLogDecorator(text="Running XAI...", logLevel="info")
    def createShapValue(self, model, xTrain, savePath, log):
        try:
            shap.initjs()
        except:
            pass

        if str(type(model))=="<class 'model.chain_reg'>":
            model = model.model_dict[self.targetColumn][0]
        
        try:
            explainer = shap.TreeExplainer(model, data=xTrain)
        except:

            try:
                explainer = shap.KernelExplainer(model.predict, data=xTrain)
            except:
                try:
                    explainer = shap.Explainer(model, data=xTrain)
                except:
                    try:
                        explainer = shap.Explainer(model.predict, data=xTrain)
                    except:
                        explainer = shap.Explainer(model)


        shap_exp = explainer(xTrain)
        joblib.dump(
            shap_exp,
            filename=os.path.join(savePath, "explainer.bz2"),
            compress=("bz2", 9),
        )
        yPred = model.predict(xTrain)
        np.save(os.path.join(savePath, "yPred.npy"), yPred)

    @WedaLogDecorator(text="Running Graph...", logLevel="info")
    def getGraphData(self, yPred, model, score, log):
        graphResult = []
        output = {"status": 200, "message": "", "result": []}
        
        if str(type(model))=="<class 'model.chain_reg'>":
            model = model.model_dict[self.targetColumn][0]
            
        g = graph(param=self.param, classes=self.classList, log=log)

        yTest = np.array(self.yTest)
        yPred = np.array(yPred)

        if self.purposeType == "timeSeries":
            yTest = np.array(self.yHoldout)
            yPred = np.array(yPred)

        # REG Plot
        if "regPlot" in self.graphList:
            regPlotOutput = g.regPlot(yTest=yTest, yPred=yPred, log=log)
            graphResult.append(regPlotOutput)

        if "distributionPlot" in self.graphList:
            # distribution Plot
            distributionPlotOutput = g.distributionPlot(
                yTest=yTest, yPred=yPred, log=log
            )
            graphResult.append(distributionPlotOutput)

        # Feature Importance
        if "FeatureImportance" in self.graphList:
            try:
                featureImp = []
                featureImp = g.featureImportance(
                    columnNms=self.originColumnList,
                    fiValue=model.feature_importances_,
                    log=log,
                )
            except:
                featureImp = g.permutationImportance(
                    model=self.model,
                    xTest=self.xTest,
                    yTest=self.yTest,
                    columnNms=self.originColumnList,
                    n_repeats=30,
                    log=log,
                )
            finally:
                graphResult.append(featureImp)

        with open(os.path.join(self.weightPath, "graphInfo.json"), "w") as jsonFile:
            json.dump(graphResult, jsonFile, ensure_ascii=False)

        output["result"] = {"score": float(score), "chartList": graphResult}

        return output

    @WedaLogDecorator(text="Running FeatureEffect...", logLevel="info")
    def getXAIData(self, partialDict, columnFlag, yPred, log):

        graphResult = []
        output = {"status": 200, "message": "", "result": []}

        g = graph(param=self.param, classes=self.classList, log=log)

        xTest = self.xTest
        yTest = np.array(self.yTest)

        if self.purposeType == "timeSeries":
            xTest = self.xHoldout
            yTest = np.array(self.yHoldout)
        
        featureEffect = {}
        if len(partialDict) > 0:
        # Feature Effect
            featureEffect = g.featureEffect(
                xTest=xTest,
                yTest=yTest,
                yPred=yPred,
                columnNms=self.originColumnList,
                partialDict=partialDict,
                target=self.targetColumn,
                columnFlag=columnFlag,
                log=log,
            )

        graphResult.append(featureEffect)

        output["result"] = {"chartList": graphResult}

        xaiInfoPath = "xaiInfo.json"
        with open(os.path.join(self.weightPath, xaiInfoPath), "w") as file:
            json.dump(output["result"], file)

        # Prediction Explanation
        self.createShapValue(model=self.model, xTrain=self.xTrain, savePath="", log=log)

        return output


    def makeFeatureEffect(self, lm, log):

        try:
            columnFlag = {}
            partialDict = {}

            # feature effect
            for index, col in enumerate(self.originColumnNms):
                # colXTest = np.array(self.xTest).T[index]  # 해당 컬럼 xTest값
                colXTest = self.xTest[col]
                
                if self.columnTypeDict[col] == "object":
                    columnFlag[col] = "pass"
                    continue

                elif self.columnTypeDict[col] == "int64" and len(np.unique(colXTest)) < 20:
                    # newXTest = pd.DataFrame([self.xTest[0]]*len(np.unique(colXTest)), columns=self.originColumnNms)
                    intData = np.unique(colXTest)
                    row_to_copy = self.xTest.iloc[0]
                    newXTest = pd.DataFrame([row_to_copy]*len(intData), columns=self.originColumnNms)
                    newXTest[col] = intData
                    # newXTest[col] = np.unique(colXTest)  # 새로우 xTest 생성
                    columnFlag[col] = "int64"

                else:
                    bins = np.histogram_bin_edges(colXTest, bins='auto')
                    # bins = pd.cut(colXTest)
                    columnFlag[col] = "float64"

                    if len(bins) > 20:
                        bins = np.histogram_bin_edges(colXTest, bins=20)
                        # bins = pd.cut(colXTest, bins=20)
                        columnFlag[col] = "float64-20"

                    # 해당 컬럼의 bin의 중앙값
                    
                    binMedian = [round(np.median([bins[i], bins[i+1]]), 4)
                                for i in range(len(bins)-1)]

                    row_to_copy = self.xTest.iloc[0]
                    newXTest = pd.DataFrame([row_to_copy]*len(binMedian), columns=self.originColumnNms)
                    newXTest[col] = binMedian  # 새로우 xTest 생성
                    
                newYPred = lm.validation(xTest=newXTest, model=self.model)[
                    "yPred"
                ]
                newYPred = list(map(lambda x: round(x, 4), newYPred))
                newXTest["newYPred"] = newYPred
                partialDict[col] = newXTest[[col, "newYPred"]].values.tolist()

            return partialDict, columnFlag
        except Exception as e:
            return partialDict, columnFlag


    def hyperParamTuning(self, space):
        output = {
            "status": 200,
            "message": "",
            "extTime": None,
            "result": None,
        }

        startTime = datetime.datetime.now()

        try:
            lm = self.customLM(
                param_grid=space, param=self.param, log=self.log, startTime=startTime
            )

            lm.model = lm.createModel()

            # model.setSpaceType()
            for i in space:
                if self.hyperscheme[i]["type"] == "int":
                    space[i] = int(space[i])
                elif self.hyperscheme[i]["type"] == "float":
                    space[i] = float(space[i])
                elif self.hyperscheme[i]["type"] == "str":
                    space[i] = str(space[i])

            try:
                lm.model.set_params(**space)
            except:
                pass

            model = lm.fit(X=self.xTrain, y=self.yTrain)
            output, yPred, score = lm.validation(xTest=self.xTest, yTest=self.yTest, model=model)

            score = output["result"].get("score", 1)
            return {"loss": 1 - score, "status": STATUS_OK, "model": model}
        except:
            return {"status": STATUS_FAIL}

    @WedaLogDecorator(text="Running Trainer...", logLevel="info")
    def getTrainResult(self, startTime, hpoTf, sendResultUrl, log):
        output = {"status": 200, "massage": "", "result": {}}

        st = time.time()

        # custom model fit
        lm = self.customLM(startTime=self.startTime, param=self.param, param_grid=self.selectedHyperParam)
        lm.model = lm.createModel()

        hyperParameter = {"hyperParameter": []}
        for key in self.hyperParamScheme:
            hyperParam = {}
            if self.hyperscheme[key]["type"] == "int":
                hyperParam["range"] = {
                    "min": self.hyperscheme[key]["min"],
                    "max": self.hyperscheme[key]["max"],
                }
            elif self.hyperscheme[key]["type"] == "float":
                hyperParam["range"] = {
                    "min": self.hyperscheme[key]["min"],
                    "max": self.hyperscheme[key]["max"],
                }

            elif self.hyperscheme[key]["type"] == "str":
                hyperParam["range"] = [
                    {"label": str(v), "value": str(v)}
                    for v in self.selectedHyperParam[key]["value"]
                ]
                
            hyperParam["parameterName"] = key
            hyperParam["defaultValue"] = self.hyperscheme[key]["defaultValue"]
            hyperParam["type"] = self.hyperscheme[key]["type"]
            hyperParameter["hyperParameter"].append(hyperParam)
                
        for key in self.selectedHyperParam:
            hyperParam = {}
            if self.hyperscheme[key]["type"] == "int":
                self.selectedHyperParam[key] = int(self.selectedHyperParam[key])

            elif self.hyperscheme[key]["type"] == "float":
                self.selectedHyperParam[key] = float(self.selectedHyperParam[key])

            elif self.hyperscheme[key]["type"] == "str":
                self.selectedHyperParam[key] = str(self.selectedHyperParam[key])

        
        try:
            lm.model.set_params(**self.selectedHyperParam)
        except:
            pass

        self.model = lm.fit(X=self.xTrain, y=self.yTrain, saveYn=True)
        # joblib.dump(self.model, open(self.saveMdlPath, "wb"))

        output, yPred, score = lm.validation(xTest=self.xTest, yTest=self.yTest, model=self.model)
        
        output["result"]["saveMdlPath"] = self.saveMdlPath
        output["selectedHyperParam"] = self.selectedHyperParam

        yPred = list(map(lambda x: round(x, 4), yPred))
        score = output["score"]

        # 그래프 확인
        if self.graphTf:
            graphResult = self.getGraphData(
                yPred=yPred, model=self.model, score=score, log=log
            )
            output["graphResult"] = graphResult["result"]
            output["graphExtTime"] = time.time() - st
            _ = sendMsg(sendResultUrl, output, "GRAPH", log)

        # XAI 확인
        if self.xaiTf:
            partialDict, columnFlag = self.makeFeatureEffect(lm=lm, log=log)

            xaiResult = self.getXAIData(
                yPred=yPred, partialDict=partialDict, columnFlag=columnFlag, log=log
            )

            output["xaiResult"] = xaiResult["result"]
            output["xaiExtTime"] = time.time() - st
            _ = sendMsg(sendResultUrl, output, "XAI", log)

        return output



@WedaLogDecorator(text="Model Training...", logLevel="info")
def runCustomHPO(params, df, startTime, hpoOption, sendResultUrl, lm, log):

    # 데이터 취득
    dl = dataLib(param=params, log=log)
    data = dl.getData(dataFrame=df, log=log)

    xTrain = data["result"]["xTrain"]
    xTest = data["result"]["xTest"]
    yTrain = data["result"]["yTrain"]
    yTest = data["result"]["yTest"]
    xHoldout = data["result"].get("xHoldout", pd.DataFrame())
    yHoldout = data["result"].get("yHoldout", pd.DataFrame())

    space = {}
    hyperParamScheme = hpoOption["hyperParamScheme"]

    space = lm.getSpace(hyperParamScheme) 

    t = trainer(
        param=dl.param,
        xTrain=xTrain,
        xTest=xTest,
        yTrain=yTrain,
        yTest=yTest,
        lm=lm,
        startTime=startTime
    )
    
    
    # learningModel.getSpace() 대신
    # for key, value in hyperParamScheme.items():
    #     if value.get("q", "") != "":
    #         if value["type"] == "int":
    #             space[key] = hp.quniform(key, value["min"], value["max"], value["q"])
    #         elif value["type"] == "float":
    #             space[key] = hp.quniform(key, value["min"], value["max"], value["q"])
    #     else:
    #         if value["type"] == "int":
    #             space[key] = hp.uniform(key, value["min"], value["max"])

    #         elif value["type"] == "float":
    #             space[key] = hp.uniform(key, value["min"], value["max"])

    #         elif value["type"] == "str":
    #             space[key] = hp.choice(key, value["value"])

    if "trialCount" in t.param:
        trialCount = int(t.param["trialCount"])
    else:
        trialCount = 10

    # Trials 객체 선언합니다.
    trials = Trials()

    # best에 최적의 하이퍼 파라미터를 return 받습니다.
    best = fmin(
        fn=t.hyperParamTuning,
        space=space,
        algo=tpe.suggest,
        max_evals=trialCount,  # 최대 반복 횟수를 지정합니다.
        trials=trials,
    )

    # convertParam 대신
    for i, v in best.items():
        if t.hyperscheme[i]["type"] == "str":
            best[i] = hyperParamScheme[i]["value"][v]

    # 최적화된 결과를 int로 변환해야하는 파라미터는 타입 변환을 수행합니다.
    for key in best:
        if type(best[key]) == np.float64:
            best[key] = round(float(best[key]), 5)
        elif type(best[key]) == np.int64:
            best[key] = int(best[key])

    dl.param["selectedHyperParam"].update(best)
    _ = sendMsg(sendResultUrl, dl.param["selectedHyperParam"], "HYPER", log)

    re = trainer(
        param=dl.param,
        xTrain=xTrain,
        xTest=xTest,
        yTrain=yTrain,
        yTest=yTest,
        lm=lm,
        startTime=startTime,
    )
    re.selectedHyperParam = best
    output = re.getTrainResult(
        startTime=startTime, hpoTf=True, sendResultUrl=sendResultUrl, log=log
    )

    print("re train done")

    with open(os.path.join(basePath, "param.json"), "w") as jsonFile:
        json.dump(re.param, jsonFile, ensure_ascii=False)

    return output


def runCustomTrain(params, df, startTime, sendResultUrl, lm, log):

    dl = dataLib(params, log)
    data = dl.getData(log=log, dataFrame=df)

    xTrain = data["result"]["xTrain"]
    xTest = data["result"]["xTest"]
    yTrain = data["result"]["yTrain"]
    yTest = data["result"]["yTest"]

    t = trainer(
        param=params,
        xTrain=xTrain,
        xTest=xTest,
        yTrain=yTrain,
        yTest=yTest,
        lm=lm,
        startTime=startTime
    )
    output = t.getTrainResult(
        startTime=startTime, hpoTf=False, sendResultUrl=sendResultUrl, log=log
    )

    with open(os.path.join(basePath, "param.json"), "w") as jsonFile:
        json.dump(t.param, jsonFile, ensure_ascii=False)

    return output


def setCategorical(df, target):
    le = LabelEncoder()
    for column in  df.columns:
        if str(df[column].dtypes) == "object" and column != target:
            df[column].fillna("None", inplace=True)
            df[column] = le.fit_transform(df[column])
    return df


def train(
    df=pd.DataFrame(),
    lm=None,
    target: str = "",
    graph: bool = False,
    xai: bool = False,
    splitInfo: int = 70,
    hyperParams: dict = {},
    savePath: str = "./",
    graphList: list = [],
    hyperParamScheme: dict = {},
    filePath: str = "",
    *args,
    **kwargs,
):
    """
    df : 학습할 dataframe
    lm : 사용자가 정의한 lm 클래스
    target : 학습 타겟
    graph : 그래프 계산 유무
    xai : xai 계산 유무
    splitInfo : 학습, 테스트 비율
    hyperParams : 모델의 하이퍼 파라미터
    hyperParamScheme: 파라미터 형태
    graphList: grapTf가 True일 떄 그릴 그래프 종류 (reg: regPlot, distribution Plot, Feature Importance)
    savePath: 모델, 그래프 등등 저장할 경로
    """
    validRatio = 100 - splitInfo
    splitInfo = {"validRatio": validRatio}

    startTime = datetime.datetime.now()
    if target == "":
        target = df.columns[-1]

    dataInfo = {}
    dataInfo["targetColumn"] = target
    dataInfo["purposeType"] = "regression"
    dataInfo["sourceType"] = "dataframe"
    dataInfo["columnList"] = [
        {"columnName": col, "columnType": str(df[col].dtype)} for col in df.columns
    ]

    dataInfo["splitInfo"] = splitInfo
    dataInfo["hyperParam"] = hyperParams
    dataInfo["savePath"] = savePath
    dataInfo["graphList"] = graphList
    
    data = {
        "runType": "custom",
        "dataInfo": dataInfo,
        "selectedHyperParam": hyperParams,
        "pathInfo": {},
        "hyperParamScheme": hyperParamScheme,
        "graphTf": graph,
        "xaiTf": xai,
    }

    data = json.dumps(data)
    runType, params, sendResultUrl = utils.initData(data)

    log = Logger("log.log", "info")
    output = runCustomTrain(
        params=params,
        df=df,
        startTime=startTime,
        sendResultUrl=sendResultUrl,
        lm=lm,
        log=log,
    )
    return output


def hpo(
    df = pd.DataFrame(),
    lm = None,
    hyperParamScheme:dict = {},
    splitInfo:int = 70,
    target:str = "",
    graph:bool = False,
    xai:bool = False,
    trialCount:int = 10,
    savePath:str = "./",
    filePath:str = ""
):
    """
    df : 학습할 dataframe
    lm : 사용자가 정의한 lm 클래스
    target : 학습 타겟
    graph : 그래프 계산 유무
    xai : xai 계산 유무
    splitInfo : 학습, 테스트 비율
    trialCount : 파라미터를 찾는 trial 횟수
    hyperParamScheme : 모델의 하이퍼 정보({"파라미터명": {"min": 0, "max": 100, "type":"float", "q":0.05, "defaultValue": 1.3},})
    graphList: grapTf가 True일 떄 그릴 그래프 종류 (reg: regPlot, distribution Plot, Feature Importance)
    savePath: 모델, 그래프 등등 저장할 경로
    filePath: 
    """
    validRatio = 100 - splitInfo
    splitInfo = {"validRatio": validRatio}
    
    hyperParameter = []
    for key, value in hyperParamScheme.items():
        tmp = {}
        tmp["range"] = {}
        
        tmp["parameterName"] = key
        tmp["defaultValue"] = value["defaultValue"]
        tmp["type"] = value["type"]
        tmp["range"]["min"] = value["min"]
        tmp["range"]["max"] = value["max"]
        
        if value.get("q", ""):
            tmp["q"] = value["q"]

        hyperParameter.append(tmp)

    
    
    hpoOption = {
        "graphTf": graph,
        "xaiTf": xai,
        "hyperParamScheme": hyperParameter,
        "savePath": savePath,
    }

    startTime = datetime.datetime.now()

    dataInfo = {}

    if target == "":
        target = df.columns[-1]

    dataInfo["targetColumn"] = target
    dataInfo["purposeType"] = "regression"
    dataInfo["sourceType"] = "dataframe"
    dataInfo["columnList"] = [
        {"columnName": col, "columnType": str(df[col].dtype)} for col in df.columns
    ]
    dataInfo["splitInfo"] = splitInfo
    
    data = {
        "runType": "custom",
        "dataInfo": dataInfo,
        "trialCount": trialCount,
        "hyperParamScheme": hyperParamScheme,
        "selectedHyperParam": {},
        "pathInfo": {},
    }

    data = json.dumps(data)

    runType, params, sendResultUrl = utils.initData(data)
    log = Logger("hpo.log", "info")

    output = runCustomHPO(
        params=params,
        df=df,
        startTime=startTime,
        hpoOption=hpoOption,
        sendResultUrl=sendResultUrl,
        lm=lm,
        log=log
    )
    return output


# 예측 실행
def predict(predictor, modelPath, df, target):
    from sklearn import metrics

    # model = lm().createModel()
    # model = joblib.load(open(modelPath, "rb"))

    if target in df.columns:
        xTest = df.drop(columns=[target])
        yTest = df[target]
    else:
        xTest = df
        yTest = None

    # ecode
    xTest = setCategorical(xTest, target)
    predictor = predictor(param=".")
    # output = pd.runPredict(model=model, xTest=xTest)
    output = predictor.runPredict(xTest=xTest)

    yPred = output["result"]["yPred"]
    if np.array(yPred).ndim != 1:
        yPred = np.array(yPred).flatten().tolist()
    if isinstance(yPred, np.ndarray):
        yPred = yPred.tolist()
    elif isinstance(yPred, pd.Series):
        yPred = yPred.tolist()
    elif not isinstance(yPred, list):
        yPred = yPred.tolist()

    output["yPred"] = yPred
    if yTest is not None:
        score = metrics.r2_score(yTest, yPred)
        output["score"] = score

    return output
