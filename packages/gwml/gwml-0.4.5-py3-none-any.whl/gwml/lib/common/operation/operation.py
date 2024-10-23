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
import time
# error 관련 lib
import traceback

# flask 관련 lib
from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Api
import requests

# data input 관련
import pandas as pd
import numpy as np

basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(basePath)
sys.path.append(os.path.join(basePath, "graph"))
sys.path.append(os.path.join(basePath, "decorator"))
sys.path.append(os.path.join(basePath, "sender"))

from sender import sendMsg
from logger.Logger import Logger
from condition import operation
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
def modelLoad():
    global params
    global p
    global modelId

    # modelInfo = params["modelInfo"]

    output = {
        "status": 200,
        "message": "",
        "result": ""
    }
    try:

        mdlPath = "/app/modeldata/model"
        paramPath = "/app/param.json"
        weightPath = "/app/weight" 
        
        modelInfoPath = "/app/modelInfo.json"
        with open(modelInfoPath, "r") as jsonFile:
          modelInfo = json.load(jsonFile)
          modelName = modelInfo["modelName"]
          modelVersion = modelInfo["version"]
          modelId = modelName+"_v"+modelVersion
        
        
        getparamsJson(paramPath)

        sys.path.append(os.path.join(mdlPath, "bin"))
        predModulePath = 'predict'
        predModule = importlib.import_module(predModulePath)
        
        p = predModule.predictor(param=weightPath, log=log)
        output["result"] = "success model run"

    except Exception as e:
        output["status"] = 400
        output["message"] = traceback.format_exc()
        print(e)
        print(traceback.format_exc())

    finally:
        print(output)
        # sendOutput(output)


# get train params
def getparamsJson(paramPath):
    global labelColumnNm
    global columnNms
    global encodedData
    global purposeType
    global columnList

    with open(paramPath, "r") as jsonFile:
        trainparam = json.load(jsonFile)
        purposeType = str(trainparam["dataInfo"]["purposeType"]).lower()
        labelColumnNm = trainparam["dataInfo"]["targetColumn"]
        columnList = trainparam["dataInfo"]["columnList"]
        columnNms = trainparam["dataInfo"]["columnNameList"]
        encodedData = trainparam["dataInfo"]["encodeData"]


# column mapping, data 정리 : [[], [], []...]
def loadData(data):
    global params
    global labelColumnNm
    global columnNms
    global encodedData
    global inputDataFormat
    global columnList
    
    output = {
        "status": 200,
        "message": "",
        "result": None
    }
    
    dataDf = pd.DataFrame()

    removedColumn = []

    try:
        for inputCol in data["header"]:
            trained = False
            for orgCol in columnList:
                if inputCol["columnName"] == orgCol["columnName"]:
                    trained = True
            if trained == False:
                removedColumn.append(inputCol["columnName"])


        for col in columnList:
            if col["checkTf"] == False:
                removedColumn.append(col["columnName"])

        # 컬럼 순서 맞추기
        tmp_header = []
        tmp_xTest = {}
        for x in range(len(data["xTest"])):
            tmp_xTest[x] = []
        
        for i in columnList:
            for j in range(len(data["header"])):
                if i["columnName"] == data["header"][j]["columnName"]:
                    tmp_header.append(data["header"][j])
                    for x in range(len(data["xTest"])):
                        tmp_xTest[x].append(data["xTest"][x][j])
                            
        data["header"] = tmp_header
        data["xTest"] = list(tmp_xTest.values())
    
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        output["status"] = 400
        output["message"] = f'check your opData (required column Length: {len(data["header"])})'
        return output
    
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
            colName = tmp["columnName"]
            originHeader.append(colName)
            if re.search("^[A-Za-z0-9_.\\-/>]*$", tmp["columnName"]):
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
        
        for rmCol in removedColumn:
            if rmCol in originHeader:
                testDf = testDf.drop(labels=rmCol, axis=1)

        predData = testDf.values
        output["status"] = 200
        output["result"] = {"predData": predData, "originJson": originJson}
        return output
    
    else:
        output["status"] = 400
        output["message"] = "check your inputDataFormat"
        return output

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
        
    loadDataOutput = loadData(data)
    if loadDataOutput["status"] == 200:
        try:
            predDatas = loadDataOutput["result"]["predData"]
            originJson = loadDataOutput["result"]["originJson"]

            if purposeType == "classification":
                newEncodedData = {v: k for k, v in encodedData[labelColumnNm].items()}

                for i in range(len(predDatas)):
                    result = originJson[i]
                    
                    startTime = time.time()
                    tmpResult = p.runPredict(xTest=np.array([predDatas[i]]), yTest=None, log=log)
                    endTime = time.time()
                    
                    elapsedTime = int(round(endTime - startTime, 5) * 1000)

                    message = tmpResult["message"]
                    yPred = tmpResult["result"]["yPred"]
                    score = tmpResult["result"]["score"]

                    result["label"] = newEncodedData.get(int(yPred[0])) if yPred is not None else None
                    result["accuracy"] = float("{:.4f}".format(float(score))) if score is not None else None
                    result["status"] = 200 if result["label"] is not None else 400
                    result["errMessage"] = message
                    output["result"].append(result)
                    output["elapsedTime"] = elapsedTime

            else:
                for i in range(len(predDatas)):
                    result = originJson[i]

                    startTime = time.time()
                    tmpResult = p.runPredict(xTest=np.array([predDatas[i]]), yTest=None, log=log)
                    endTime = time.time()
                    elapsedTime = int(round(endTime - startTime, 5) * 1000)

                    message = tmpResult["message"]
                    yPred = tmpResult["result"]["yPred"]
                    score = tmpResult["result"]["score"]

                    result["label"] = float("{:.4f}".format(float(yPred[0]))) if yPred is not None else None
                    result["accuracy"] = abs(float(yPred[0]) - float(result[labelColumnNm])) if labelColumnNm in result and result[labelColumnNm] != None else 0
                    result["status"] = 200 if result["label"] is not None else 400
                    result["errMessage"] = message
                    output["status"] = result["status"]
                    output["message"] = result["errMessage"]
                    output["result"].append(result)
                    output["elapsedTime"] = elapsedTime
            return output
                
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            output["status"] = 400
            output["message"] = str(traceback.format_exc())

            return output
    else:
        return loadDataOutput


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
                # sendOutput(output)
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
                # sendOutput(output)
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


# runEasyLabeling
@app.route('/api/runOperation', methods=['POST'])
def runPredict():
    global p
    global params
    global modelId

    opResult = []
    req = request.json
    data = req["opData"]
    
    inputColumn = []
    header = [i["columnName"] for i in data["header"] ]
  
    for i in data["xTest"]:
      inputColumn.append(dict(zip(header, i)))

    keyColumn = data["key"] if "key" in data else None

    if p is None:
        result = {
                'code': 400,
                'message': "model is not running!"
                }
        resp = jsonify(result)
        resp.status_code = result['code']
        return resp

    else:
        try:
            # data load
            predResult = labeling(data)
            if predResult["status"] == 200:    
                elapsedTime = predResult["elapsedTime"]
                # oprator 적용
                conditions = params["conditionList"] if params["postProcessingInfo"]["type"] == "condition" else []

                if len(conditions) == 0:
                    for result in range(len(predResult["result"])):
                        predResult["result"][result]["key"] = keyColumn
                        inputColumn[result].update(predResult["result"][result])
                        opResult.append(inputColumn[result])

                else:
                    pred = deepcopy(predResult)
                    condResult = pred["result"]
                    for result in range(len(condResult)):
                        condResult[result]["key"] = keyColumn
                        for condition in conditions:
                            conditionListCount = len(condition)
                            if conditionListCount > 0:
                                for conditionList in condition["classConditionList"]:
                                    conditionList["conditionName"] = condition["conditionName"]
                                    conditionList["color"] = condition["color"]
                                    opCondResult, checker = operation(conditionList["target"], conditionList, condResult[result])
                                print("opCondResult!!! ", opCondResult)
                                if checker:
                                    inputColumn[result].update(opCondResult)
                                    opResult.append(inputColumn[result])
                                    break

                        if not checker:
                            inputColumn[result].update(condResult[result])
                            opResult.append(inputColumn[result])

                opPredResult = {
                    "elapsedTime": elapsedTime,
                    "opResult": opResult,
                    "modelId": modelId
                }
            else:
                result = {
                    'code': 400,
                    'message': str(predResult["message"])
                    }
                resp = jsonify(result)
                resp.status_code = result['code']
                return resp

            
        except Exception as e:
            print(e)

            result = {
                    'code': 400,
                    'message': str(traceback.format_exc())
                    }
            resp = jsonify(result)
            resp.status_code = result['code']
            return resp
        # postProcessing(op_result)
  
    return jsonify(opPredResult)


if __name__ == "__main__":
    # data = '{"runType":"operation","inputDataFormat":"tabular","params":{"serverParam":{"serverIp":"10.140.142.30","serverPort":80,"sendStatusUrl":"/api/sample/test"},"dataInfo":{"dataType":"json"},"preProcessingInfo":{"type":"empty"},"postProcessingInfo":{"type":"empty"},"modelInfo":{"modelPath":"/Users/gimminjong/decorator/XGBClassification/model","weightPath":"/Users/gimminjong/decorator/XGBClassification/model/weight","gpuIdx":-1}}}'
    # data = '{"runType":"operation","inputDataFormat":"tabular","params":{"serverParam":{"serverIp":"10.140.142.10","serverPort":80,"sendStatusUrl":"/api/sample/test"},"dataInfo":{"dataType":"json"},"preProcessingInfo":{"type":"empty"},"postProcessingInfo":{"type":"empty"},"modelInfo":{"modelPath":"/Users/gimminjong/decorator/Tabular/Regression/XGBRegression/model","weightPath":"/Users/gimminjong/decorator/Tabular/Regression/XGBRegression/model/weight","gpuIdx":-1}}}'
    # data = '{"runType":"operation","inputDataFormat":"tabular","preProcessingInfo":{"type":"empty"},"postProcessingInfo":{"type":"condition"},"conditionList":[{"conditionName":"test","color":"#2100ff","className": 123, "classConditionList":[{"className": 123, "target":"value","leftValue":"10","leftCondition":"lt","rightValue":"30","rightCondition":"lt"}]}]}'
    # data = '{"runType":"operation","inputDataFormat":"tabular","preProcessingInfo":{"type":"empty"},"postProcessingInfo":{"type":"empty"},"conditionList":[]}'
    # data = '{"runType":"operation","inputDataFormat":"tabular","preProcessingInfo":{"type":"empty"},"postProcessingInfo":{"type":"condition"},"conditionList":[{"classConditionList":[{"className":"0","leftCondition":"none","leftValue":"","rightCondition":"lteq","rightValue":"0.1","target":"accuracy"}],"className":"0","color":"#1400ff","conditionName":"승인"},{"classConditionList":[{"className":"1","leftCondition":"none","leftValue":"","rightCondition":"lteq","rightValue":"0.1","target":"accuracy"}],"className":"1","color":"#ff9e00","conditionName":"승인대기"},{"classConditionList":[{"className":"2","leftCondition":"none","leftValue":"","rightCondition":"lteq","rightValue":"0.1","target":"accuracy"}],"className":"2","color":"#ff0000","conditionName":"거절"}]}'    
    
    data = sys.argv[1]
    params = json.loads(data)
    print("params!!!!", params)
    inputDataFormat = params["inputDataFormat"]

    # with open('./clf/op_input.json') as f:
    #     params = json.load(f)

    log = Logger("log.log", "info")

    preprocessing("check")
    postProcessing("check")
    modelLoad()
    app.run(host='0.0.0.0', port=80)

