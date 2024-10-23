# -*- coding:utf-8 -*-
'''
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
'''

# 1. model load()
# 2. preprocessing()
#    2-1. script 적용 => column name mapper
#         2-1-1. pkl
#         2-1-2. python script
#    2-2. func()
# 3. flask server run
#     3-1. 0.0.0.0:80/
#     3-2. runPredict()
#     3-3. outputType operator 적용

# 4. postProcessing()
#    4-1. script 적용
#    4-2. func

# 기본 library
import os
import pathlib
import re
import sys
import json
import importlib

# error 관련 lib
import traceback

# flask 관련 lib
from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Api
import requests
from hyperopt import fmin, tpe, hp
from sklearn.model_selection import cross_val_score
# data input 관련
import pandas as pd
import numpy as np

basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(basePath)
sys.path.append(os.path.join(basePath, "model"))
sys.path.append(os.path.join(basePath, "bin"))
sys.path.append(os.path.join(basePath, "graph"))
sys.path.append(os.path.join(basePath, "decorator"))
sys.path.append(os.path.join(basePath, "sender"))

from sender import sendMsg
from logger.Logger import Logger
from copy import deepcopy

app = Flask(__name__)
api = Api(app)

model = None
predModule = None
purposeType = None
labelColumnNm = ""
columnNms = []
encodedData = {}

p = None

params = None
inputDataFormat = None
log = None


def sendOutput(output):
    global params
    serverParam = params["serverParam"]
    headers = {"Content-Type": "application/json; charset=utf-8"}

    srvIp = serverParam["serverIp"]
    srvPort = serverParam["serverPort"]
    sendRouter = serverParam["sendStatusUrl"]

    sendUrl = "{}:{}/{}".format(srvIp, srvPort, sendRouter)
    try:
        requests.post(sendUrl, headers=headers, data=json.dumps(output), timeout=1)

    except Exception:
        return


# model load
def modelLoad(log):
    global params
    global p

    modelInfo = params["modelInfo"]

    output = {
        "status": 200,
        "message": "",
        "result": ""
    }
    try:
        print("================================start")
        mdlPath = modelInfo["modelPath"] if "modelPath" in modelInfo else "/app"
        paramPath = os.path.join(modelInfo["modelPath"], "param.json") if "modelPath" in modelInfo else "/app/param.json"
        predModulePath = "model"
        predModule = importlib.import_module(predModulePath)
        p = predModule.createModel(param=None, saveMdlPath=None, log=log)



        print("================================end")
        # output["result"] = "success model run"

    except Exception as e:
        output["status"] = 400
        output["message"] = traceback.format_exc()
        print(e)
        print(traceback.format_exc())

    finally:
        print(output)
        sendOutput(output)


# get train params
def getparamsJson(paramPath):
    global labelColumnNm
    global columnNms
    global encodedData
    global purposeType

    with open(paramPath, "r") as jsonFile:
        trainparam = json.load(jsonFile)
        purposeType = str(trainparam["modelInfo"]["purposeType"]).lower()
        labelColumnNm = trainparam["dataInfo"]["labelColumnNm"]
        columnNms = trainparam["dataInfo"]["columnNms"]
        encodedData = trainparam["dataInfo"]["encodeData"]


# column mapping, data 정리 : [[], [], []...]
def loadData(data):
    global params
    global labelColumnNm
    global columnNms
    global encodedData
    global inputDataFormat

    dataDf = pd.DataFrame()

    if inputDataFormat == 'filePath':
        for filePath in data["filePath"]:
            ext = pathlib.Path(filePath).suffix
            if "csv" in ext or "txt" in ext or "text" in ext:
                # csv, txt인 경우
                tmpDf = pd.read_csv(filePath, encoding="utf-8-sig", sep=data["seperator"] if "seperator" in data else ",")
                dataDf = dataDf.append(tmpDf, ignore_index=True)
                dataDf.fillna(0, inplace=True)

            elif "xls" in ext:
                # excel인 경우
                tmpDf = pd.read_excel(filePath, encoding="utf-8-sig")
                dataDf = dataDf.append(tmpDf, ignore_index=True)
                dataDf.fillna(0, inplace=True)

    elif inputDataFormat == 'database':
        if "mysql" in params["dataInfo"]["client"] or "maria" in params["dataInfo"]["client"]:
            import pymysql
            conn = pymysql.connect(host=data["address"],
                                   port=int(data["port"]),
                                   database=data["dbName"],
                                   user=data["user"],
                                   password=data["password"])

        elif "pg" in params["dataInfo"]["client"]:
            import psycopg2 as pg
            conn = pg.connect(host=data["address"],
                              port=int(data["port"]),
                              database=data["dbName"],
                              user=data["user"],
                              password=data["password"])

        elif "oracle" in params["dataInfo"]["client"]:
            import cx_Oracle as co
            oraclePath = os.environ["ORACLE_HOME"]
            co.init_oracle_client(lib_dir=os.path.join(oraclePath, "lib"))
            dsnTns = co.makedsn(
                data["address"],
                int(data["port"]),
                data["dbName"]
            )
            conn = co.connect(
                user=data["user"],
                password=data["password"],
                dsn=dsnTns
            )
        dataDf = pd.read_sql(data["query"], conn)
        dataDf.fillna(0, inplace=True)

        conn.close()

    elif inputDataFormat == 'tabular':
        header = []
        originHeader = []

        for tmp in data["header"]:
            colName = tmp["columnNames"]
            originHeader.append(colName)
            if re.search("^[A-Za-z0-9_.\\-/>]*$", tmp["columnNames"]):
                pass
            else:
                colName = colName.replace("(", "_")
                colName = colName.replace(")", "_")
                colName = colName.replace(" ", "_")
            header.append(colName)

        testDf = pd.DataFrame(columns=header)

        originJson = []
        for xTestTmp in data["xTest"]:
            testDf.loc[len(testDf)] = xTestTmp
            originJsonTmp = {}

            for idx, xTestData in enumerate(xTestTmp):
                originJsonTmp.update({originHeader[idx]: xTestData})

            originJson.append(originJsonTmp)

        testDf.fillna(0, inplace=True)

        # encodeData mapping
        for dfColumn in testDf.columns:
            for key in encodedData.keys():
                if key == dfColumn:
                    for i in testDf.index:
                        testDf.loc[i, key] = encodedData[key][testDf.loc[i, key]] if key in encodedData and str(testDf.loc[i, key]) in encodedData[key] else 0
                else:
                    pass

        if labelColumnNm in originHeader:
            testDf = testDf.drop(labels=labelColumnNm, axis=1)

        predData = testDf.values

    return predData, originJson


def labeling(data):
    global params
    global purposeType
    global encodedData
    global labelColumnNm
    global p

    output = {
        "status": 200,
        "message": "",
        "result": []
    }
    predDatas, originJson = loadData(data)

    if purposeType == "classification":
        newEncodedData = {v: k for k, v in encodedData[labelColumnNm].items()}

        for i in range(len(predDatas)):
            result = originJson[i]
            tmpResult = p.runPredict(xTest=np.array([predDatas[i]]), yTest=None, log=log)

            message = tmpResult["message"]
            yPred = tmpResult["result"]["yPred"]
            score = tmpResult["result"]["score"]

            result["label"] = newEncodedData.get(int(yPred[0])) if yPred is not None else None
            result["accuracy"] = float("{:.4f}".format(float(score))) if score is not None else None
            result["status"] = 200 if result["label"] is not None else 400
            result["errMessage"] = message
            output["result"].append(result)

    else:
        for i in range(len(predDatas)):
            result = originJson[i]
            tmpResult = p.runPredict(xTest=np.array([predDatas[i]]), yTest=None, log=log)
            message = tmpResult["message"]
            yPred = tmpResult["result"]["yPred"]
            score = tmpResult["result"]["score"]
  
            result["label"] = float("{:.4f}".format(float(yPred[0]))) if yPred is not None else None
            result["accuracy"] = abs(float(yPred[0]) - float(result[labelColumnNm])) if labelColumnNm in result else 0
            result["status"] = 200 if result["label"] is not None else 400
            result["errMessage"] = message
            output["result"].append(result)

    return output


# pre processing
def preprocessing(data):
    global params
    prepInfo = params["preProcessingInfo"]

    if prepInfo["type"].lower() == "pkl":
        print("pickle!!!")

    elif prepInfo["type"].lower() == "script":
        import pathlib
        if prepInfo["path"] is None or len(prepInfo["path"]) == 0:
            output = {
                "status": 400,
                "message": "script path None",
                "result": ""
            }
            if data == "check":
                print(output)
                sendOutput(output)
            return data

        for scriptFile in prepInfo["path"]:
            baseName = os.path.basename(scriptFile)
            dirName = os.path.dirname(scriptFile)
            sys.path.append(dirName)

            moduleName = baseName.replace(pathlib.Path(baseName).suffix, "")
            prepModule = importlib.import_module(moduleName)

            p = prepModule.preprocessing(data)
            data = p.run()

    elif prepInfo["type"].lower() == "function":
        print("function!!!!")

    elif prepInfo["type"] == "empty":
        data = data

    return data


# post processing
def postProcessing(data):
    global params
    prepInfo = params["postProcessingInfo"]

    if prepInfo["type"].lower() == "pkl":
        print("pickle!!!")

    elif prepInfo["type"].lower() == "script":
        import pathlib
        if prepInfo["path"] is None or len(prepInfo["path"]) == 0:
            output = {
                "status": 400,
                "message": "script path None",
                "result": ""
            }
            if data == "check":
                print(output)
                sendOutput(output)
            return data

        for scriptFile in prepInfo["path"]:
            baseName = os.path.basename(scriptFile)
            dirName = os.path.dirname(scriptFile)
            sys.path.append(dirName)

            moduleName = baseName.replace(pathlib.Path(baseName).suffix, "")
            prepModule = importlib.import_module(moduleName)

            p = prepModule.postprocessing(data)
            data = p.run()

    elif prepInfo["type"].lower() == "function":
        print("function!!!!")

    elif prepInfo["type"] == "empty":
        data = data

    return data

def objective(params):
    global p
    params = {'max_depth': int(params['max_depth']),
              'subsample': params['subsample']}
    best_score = cross_val_score(p, X_train, y_train, 
                                 scoring='accuracy', 
                                 cv=5, 
                                 n_jobs=8).mean()
    loss = 1 - best_score
    return loss

# runEasyLabeling
@app.route('/', methods=['POST'])
def runPredict():

    
    global p
    global params

    print(p)

    # 알고리즘 실행
    best = fmin(fn=objective, space=param_space, 
            max_evals=10, 
            rstate=np.random.RandomState(777), 
            algo=tpe.suggest)
    param_space = {'max_depth': hp.quniform('max_depth', 2, 10, 1),
               'subsample': hp.uniform('subsample', 0.1, 0.9)}
    # output = {
    #     "status": 200,
    #     "message": "",
    #     "result": []
    # }

    # req = request.json
    # data = req["data"]

    # keyColumn = data["key"] if "key" in data else None

    # if p is None:
    #     output["status"] = 400
    #     output["message"] = "model is not running!"


    # else:
    #     try:
    #         # data load
    #         predResult = labeling(data)

    #         # oprator 적용
    #         conditions = params["conditionList"] if params["postProcessingInfo"]["type"] == "condition" else []

    #         if len(conditions) == 0:
    #             for result in predResult["result"]:
    #                 output["result"].append(result)

    #         else:
    #             pred = deepcopy(predResult)
    #             condResult = pred["result"]
    #             for result in condResult:
    #                 result["key"] = keyColumn
    #                 for condition in conditions:
    #                     conditionListCount = len(condition)
    #                     if conditionListCount > 0:
    #                         for conditionList in condition["classConditionList"]:
    #                             conditionList["conditionName"] = condition["conditionName"]
    #                             conditionList["color"] = condition["color"]
    #                             condResult, checker = operation(conditionList["target"], conditionList, result)

    #                         if checker:
    #                             output["result"].append(condResult)
    #                             break

    #                 if not checker:
    #                     output["result"].append(result)

    #     except Exception as e:
    #         output["status"] = 400
    #         output["message"] = traceback.format_exc()
    #         print(e)
    #         print(traceback.format_exc())

    #     postProcessing(output)

    return jsonify({})


if __name__ == "__main__":
    # data = '{"runType":"operation","inputDataFormat":"tabular","params":{"serverParam":{"serverIp":"10.140.142.30","serverPort":80,"sendStatusUrl":"/api/sample/test"},"dataInfo":{"dataType":"json"},"preProcessingInfo":{"type":"empty"},"postProcessingInfo":{"type":"empty"},"modelInfo":{"modelPath":"/Users/gimminjong/decorator/XGBClassification/model","weightPath":"/Users/gimminjong/decorator/XGBClassification/model/weight","gpuIdx":-1}}}'
    # data = '{"runType":"operation","inputDataFormat":"tabular","params":{"serverParam":{"serverIp":"10.140.142.10","serverPort":80,"sendStatusUrl":"/api/sample/test"},"dataInfo":{"dataType":"json"},"preProcessingInfo":{"type":"empty"},"postProcessingInfo":{"type":"empty"},"modelInfo":{"modelPath":"/Users/gimminjong/decorator/Tabular/Regression/XGBRegression/model","weightPath":"/Users/gimminjong/decorator/Tabular/Regression/XGBRegression/model/weight","gpuIdx":-1}}}'
    data = '{"runType":"operation","inputDataFormat":"tabular","params":{"serverParam":{"serverIp":"10.140.142.10","serverPort":80,"sendStatusUrl":"/api/sample/test"},"dataInfo":{"dataType":"json"},"preProcessingInfo":{"type":"empty"},"postProcessingInfo":{"type":"empty"},"modelInfo":{"modelPath":"/Users/dmshin/onion/tabular-legacy-model/Regression/XGBRegression/model","weightPath":"/data/tab33421/48c3e76c5fb45321af42ac2a9055f2fb/train/472e5ebf034dc6d294b06e458847b8bf/weight","gpuIdx":-1}}}'
    # data = sys.argv[1]
    params = json.loads(data)
    inputDataFormat = params["inputDataFormat"]
    params = params["params"]
    # with open('./clf/op_input.json') as f:
    #     params = json.load(f)

    log = Logger("log.log", "info")

    preprocessing("check")
    postProcessing("check")
    modelLoad(log)
    app.run(host='0.0.0.0', port=80)

