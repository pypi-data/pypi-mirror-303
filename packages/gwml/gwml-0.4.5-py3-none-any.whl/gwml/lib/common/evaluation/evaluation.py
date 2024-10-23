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


from cgi import test
import os
import re
import sys
import time
import json
import pathlib
import importlib
import traceback
import numpy as np
import pandas as pd
from copy import copy
from sklearn.preprocessing import label_binarize
from pandas import json_normalize
from sklearn.preprocessing import LabelEncoder

import graphviz
import lingam
from lingam.utils import make_dot
from lingam.utils import make_prior_knowledge

# flask lib
from flask import Flask, request
from flask_restful import Api
from flask import jsonify

basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
modelPath = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir), os.path.pardir), "modeldata")) # modeldata 위치

sys.path.append(basePath)
sys.path.append(modelPath)
sys.path.append(os.path.join(modelPath, "modeldata"))
sys.path.append(os.path.join(basePath, "graph"))
sys.path.append(os.path.join(basePath, "decorator"))
sys.path.append(os.path.join(basePath, "sender"))


from graph import graph
from sender import sendMsg
from logger import Logger
from error.WedaErrorDecorator import WedaErrorDecorator
from logger.WedaLogDecorator import WedaLogDecorator
from logger.Logger import Logger


app = Flask(__name__)
api = Api(app)


p = None
columnNms = None
originColumnNms = None
hyperParam = None
mdlPath = None
labelColumnNms = None
labelColumnNm = None
dfColumnNms = None
testColumnNms = None
purposeType = None
log = None
isLabel = None
sep = None
inputColumn = None
dateFormat = None
timeColumn = None

@WedaErrorDecorator
@WedaLogDecorator(text="Model Loading...", logLevel="info")
def modelLoad(param, log):
    global p
    global columnNms
    global originColumnNms
    global hyperParam
    global mdlPath
    global labelColumnNm
    global labelColumnNms
    global purposeType
    global sep
    global dateFormat
    global timeColumn
    global columnDict 
    
    output = {
        "status": 200,
        "message": "",
        "result": None
    }
    
    pathInfo = param["pathInfo"] if "pathInfo" in param else None
    mdlInfo = param["dataInfo"] if "dataInfo" in param else None
    mdlPath = pathInfo["modelPath"] if "modelPath" in pathInfo else f"/app/modeldata/model"
    weightPath = pathInfo["weightPath"]
    pvPath = pathInfo["pvPath"]

    sys.path.append(os.path.join(mdlPath, "bin"))
    predModulePath = 'predict'
    predModule = importlib.import_module(predModulePath)
    
    # get hyperParam to json File
    hyperParamJson = os.path.join(pvPath, 'param.json')
    if os.path.isfile(hyperParamJson):
        with open(hyperParamJson, "r") as jsonFile:
            hyperParam = json.load(jsonFile)
    else: 
        hyperParamJson = "/app/param.json"
        with open(hyperParamJson, "r") as jsonFile:
            hyperParam = json.load(jsonFile)

    modelInfoJson = os.path.join(pvPath, 'modelInfo.json')
    if os.path.isfile(modelInfoJson):
        with open(modelInfoJson, "r") as jsonFile:
            modelInfo = json.load(jsonFile)

    hyperParam["pathInfo"]["weightPath"] = weightPath

    p = predModule.predictor(param=weightPath, log=log)

    labelColumnNms = hyperParam["dataInfo"]["targetColumnNameList"] if "targetColumnNameList" in hyperParam["dataInfo"] else None # Class 이름
    columnNms = hyperParam["dataInfo"]["columnNameList"] if "columnNameList" in hyperParam["dataInfo"] else None # _ " 등 바꾼 후 컬럶 이름
    labelColumnNm = hyperParam["dataInfo"]["targetColumn"] if "targetColumn" in hyperParam["dataInfo"] else 'label' # 타겟 컬럼
    originColumnNms =  hyperParam["dataInfo"]["originColumnNameList"] if "originColumnNameList" in hyperParam["dataInfo"] else None # encode 전 컬럼 이름들
    purposeType = modelInfo["purposeType"]
    sep = hyperParam["dataInfo"]["delimiter"] if "delimiter" in hyperParam["dataInfo"] else ","
    dateFormat = hyperParam["dataInfo"].get("dateFormat", "")
    timeColumn = hyperParam["dataInfo"].get("timeColumn", "")
    columnDict = hyperParam.get("columnTypeDict", "")

    return output


def mappingEncodeData(yTest=None, yPred=None):
    global hyperParam
    global labelColumnNm

    encodeData = hyperParam["dataInfo"]["encodeData"]
    encodeDataLabel = encodeData[labelColumnNm]

    newYTest = []
    newYPred = []

    for data in encodeDataLabel.keys():
        if yTest is not None:
            for testData in yTest:
                if data == testData:
                    newYTest.append(encodeDataLabel[data])

        for predData in yPred:
            if data == predData:
                newYPred.append(encodeDataLabel[data])

    return newYTest, newYPred


@WedaLogDecorator(text="Loading Data type of DB ...", logLevel="info")
def getDBData(dataInfo=None, log=None):
    global labelColumnNm
    global columnNms
    global originColumnNms
    global isLabel
    global dfColumnNms
    global testColumnNms
    global sep

    output = {
        "status": 200,
        "message": "",
        "result": None
    }

    testDf = pd.DataFrame()
    start = int(dataInfo["start"])
    end = int(dataInfo["end"])
    dbInfo = dataInfo["dbInfo"]
    dbType = dbInfo["client"].lower()

    if dbType == "mysql":
        log.info("mysql들어왔다")
        import pymysql
        conn = pymysql.connect(
            host=dbInfo["address"],
            port=int(dbInfo["port"]),
            database=dbInfo["dbName"],
            user=dbInfo["user"],
            password=dbInfo["password"]
        )
        st = time.time()
        testDf = testDf.append(pd.read_sql(dbInfo["query"], conn))
        conn.close()

    elif dbType == "oracle":
        import cx_Oracle as co
        oraclePath = os.environ["ORACLE_HOME"]
        co.init_oracle_client(lib_dir=os.path.join(oraclePath, "lib"))

        st = time.time()
        dsnTns = co.makedsn(dbInfo["address"], int(dbInfo["port"]), dbInfo["dbName"])
        conn = co.connect(user=dbInfo["user"], password=dbInfo["password"], dsn=dsnTns)
        testDf = testDf.append(pd.read_sql(dbInfo["query"], conn))
        conn.close()

    elif dbType == "pg":
        import psycopg2 as pg
        conn = pg.connect(
            host=dbInfo["address"],
            port=int(dbInfo["port"]),
            dbname=dbInfo["dbName"],
            user=dbInfo["user"],
            password=dbInfo["password"]
        )
        st = time.time()
        testDf = testDf.append(pd.read_sql(dbInfo["qurey"], conn))
        conn.close()

    elif dbType == "db2":
        import ibm_db_dbi
        connInfo = "DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={};PWD={};".format(
            dbInfo["dbName"],
            dbInfo["address"],
            int(dbInfo["port"]),
            dbInfo["user"],
            dbInfo["password"]
        )

        st = time.time()
        conn = ibm_db_dbi.connect(connInfo, "", "")
        testDf = testDf.append(pd.read_sql(dbInfo["query"], conn))
        conn.close()

    labelDf = testDf[labelColumnNm]
    testDf = testDf.drop(labels=labelColumnNm, axis=1)
    testDf = pd.concat([testDf, labelDf], axis=1)
    dfColumnNms = list(testDf.columns)
    
    if purposeType.lower() == "classification":
        if labelColumnNm in dfColumnNms:
            testDf[labelColumnNm] = testDf[labelColumnNm].apply(str)
    testDf = testDf.iloc[start:end+1].values

    testColumnNms = []
    for colName in dfColumnNms:
        if colName == labelColumnNm:
            testColumnNms.append(colName)
        else:
            if re.search("^[A-Za-z0-9_.\\-/>]*$", colName):
                pass
            else:
                colName = colName.replace("(", "_")
                colName = colName.replace(")", "_")
                colName = colName.replace(" ", "_")
            testColumnNms.append(colName)

    if labelColumnNm in testColumnNms:
        testDf = pd.DataFrame(testDf, columns=testColumnNms)
        dataDf = testDf.drop(labelColumnNm, axis=1)
        labelDf = testDf[labelColumnNm]
        predictDf = pd.concat([dataDf, labelDf], axis=1)

        isLabel = True
        output["result"] = {
            "dataFrame": predictDf
        }

    else:
        predictDf = pd.DataFrame(testDf, columns=testColumnNms)

        isLabel = False
        output["result"] = {
            "dataFrame": predictDf
        }

    return output


@WedaLogDecorator(text="Loading Data type of File ...", logLevel="info")
def getFileData(evalInfo=None, log=None):
    global labelColumnNm
    global columnNms
    global originColumnNms
    global isLabel
    global dfColumnNms
    global testColumnNms
    global sep
    global inputColumn
    
    output = {
        "status": 200,
        "message": "",
        "result": None
    }

    dataPath = evalInfo["dataPath"][0]
    extension = pathlib.Path(dataPath).suffix.lower()
    start = int(evalInfo["start"])
    end = int(evalInfo["end"])

    testDf = None
    if extension == '.csv' or extension == '.txt' or extension == '.text':
        testDf = pd.read_csv(dataPath)
        
        if labelColumnNm in testDf.columns:
            labelDf = testDf[labelColumnNm]
            testDf = testDf.drop(labels=labelColumnNm, axis=1)
            # testDf = testDf[columnNms]
            testDf = testDf[originColumnNms]
            testDf = pd.concat([testDf, labelDf], axis=1)


    elif extension == '.xls' or extension == '.xlsx':
        dfColumnNms = list(pd.read_excel(dataPath).columns)
        testDf = pd.read_excel(
            dataPath,
            skiprows=start,
            nrows=end - start + 1,
            encoding='utf-8-sig'
        )
    
    dfColumnNms = list(testDf.columns)
    
    if purposeType.lower() == "classification":
        if labelColumnNm in dfColumnNms:
            testDf[labelColumnNm] = testDf[labelColumnNm].apply(str)
    testDf = testDf.iloc[start:end+1].values

    testColumnNms = []
    for colName in dfColumnNms:
        if colName == labelColumnNm:
            testColumnNms.append(colName)
        else:
            if re.search("^[A-Za-z0-9_.\\-/>]*$", colName):
                pass
            else:
                colName = colName.replace("(", "_")
                colName = colName.replace(")", "_")
                colName = colName.replace(" ", "_")

            testColumnNms.append(colName)

    if labelColumnNm in testColumnNms:
        testDf = pd.DataFrame(testDf, columns=testColumnNms)
        dataDf = testDf.drop(labelColumnNm, axis=1)
        labelDf = testDf[labelColumnNm]
        predictDf = pd.concat([dataDf, labelDf], axis=1)

        isLabel = True
        output["result"] = {
            "dataFrame": predictDf,
            "columns": dfColumnNms
        }

    else:
        predictDf = pd.DataFrame(testDf, columns=testColumnNms)

        isLabel = False
        output["result"] = {
            "dataFrame": predictDf,
            "columns": dfColumnNms
        }

    return output


@WedaLogDecorator(text="Loading Data type of Request ...", logLevel="info")
def getCurlData(evalInfo=None, log=None):
    global labelColumnNm
    global columnNms
    global originColumnNms
    global isLabel
    global dfColumnNms
    global testColumnNms
    global sep
    global inputColumn
    
    output = {
        "status": 200,
        "message": "",
        "result": None
    }

    inputColumn = [evalInfo["dataBody"]]
    dataBody = evalInfo["dataBody"]
    testDf = json_normalize(dataBody)
    labelDf = pd.DataFrame()
    
    if labelColumnNm in testDf.columns:
      testDf[labelColumnNm] = [0]
      labelDf = testDf[labelColumnNm]
      testDf = testDf.drop(labels=labelColumnNm, axis=1)
    
    testDf = testDf[originColumnNms]

    testDf = pd.concat([testDf, labelDf], axis=1)
    dfColumnNms = list(testDf.columns)

    if purposeType.lower() == "classification":
        if labelColumnNm in dfColumnNms:
            testDf[labelColumnNm] = testDf[labelColumnNm].apply(str)

    output["result"] = {
            "dataFrame": testDf
        }

    testColumnNms = []
    for colName in dfColumnNms:
        if colName == labelColumnNm:
            testColumnNms.append(colName)
        else:
            if re.search("^[A-Za-z0-9_.\\-/>]*$", colName):
                pass
            else:
                colName = colName.replace("(", "_")
                colName = colName.replace(")", "_")
                colName = colName.replace(" ", "_")
            testColumnNms.append(colName)

    if labelColumnNm in testColumnNms:
        testDf.columns = testColumnNms
        predictDf = testDf

        isLabel = True
        output["result"] = {
            "dataFrame": predictDf,
            "columns": dfColumnNms
        }

    else:
        testDf.columns = testColumnNms
        predictDf = testDf

        isLabel = False
        output["result"] = {
            "dataFrame": predictDf,
            "columns": dfColumnNms
        }
    isLabel = False
    return output




@WedaLogDecorator(text="Loading Data type of Request ...", logLevel="info")
def getDataset(evalInfo=None, log=None):    
    global labelColumnNm
    global columnNms
    global originColumnNms
    global isLabel
    global dfColumnNms
    global testColumnNms
    global sep
    global inputColumn
    
    output = {
        "status": 200,
        "message": "",
        "result": None
    }

    dataPath = evalInfo["dataPath"][0]
    extension = pathlib.Path(dataPath).suffix.lower()

    testDf = None
    if extension == '.csv' or extension == '.txt' or extension == '.text':
        testDf = pd.read_csv(dataPath)
        
        if labelColumnNm in testDf.columns:
            labelDf = testDf[labelColumnNm]
            testDf = testDf.drop(labels=labelColumnNm, axis=1)
            testDf = testDf[originColumnNms]
            testDf = pd.concat([testDf, labelDf], axis=1)


    elif extension == '.xls' or extension == '.xlsx':
        dfColumnNms = list(pd.read_excel(dataPath).columns)
        testDf = pd.read_excel(
            dataPath,
            encoding='utf-8-sig'
        )
    
    dfColumnNms = list(testDf.columns)
    inputColumn = testDf.to_dict(orient="records")
    
    if purposeType.lower() == "classification":
        if labelColumnNm in dfColumnNms:
            testDf[labelColumnNm] = testDf[labelColumnNm].apply(str)

    if evalInfo["selectType"] == "range":
      testDf = testDf[(testDf[evalInfo["columnName"]] >= evalInfo["min"]) & (testDf[evalInfo["columnName"]] <= evalInfo["max"])]

    testColumnNms = []
    for colName in dfColumnNms:
        if colName == labelColumnNm:
            testColumnNms.append(colName)
        else:
            if re.search("^[A-Za-z0-9_.\\-/>]*$", colName):
                pass
            else:
                colName = colName.replace("(", "_")
                colName = colName.replace(")", "_")
                colName = colName.replace(" ", "_")

            testColumnNms.append(colName)

    if labelColumnNm in testColumnNms:
        testDf = pd.DataFrame(testDf, columns=testColumnNms)
        dataDf = testDf.drop(labelColumnNm, axis=1)
        labelDf = testDf[labelColumnNm]
        predictDf = pd.concat([dataDf, labelDf], axis=1)

        isLabel = True
        output["result"] = {
            "dataFrame": predictDf,
            "columns": dfColumnNms
        }

    else:
        predictDf = pd.DataFrame(testDf, columns=testColumnNms)

        isLabel = False
        output["result"] = {
            "dataFrame": predictDf,
            "columns": dfColumnNms
        }

    return output
  
    
@WedaLogDecorator(text="Loading Data type of Request ...", logLevel="info")
def getTimeSeries(evalInfo=None, log=None):    
    global labelColumnNm
    global columnNms
    global originColumnNms
    global isLabel
    global dfColumnNms
    global testColumnNms
    global sep
    global inputColumn
    global dateFormat
    
    output = {
        "status": 200,
        "message": "",
        "result": None
    }

    startDate = evalInfo["startDate"]
    endDate = evalInfo["endDate"]
    
    if 'f' in dateFormat:
      freq = 'L'
    elif 's' in dateFormat:
      freq = 'S'
    elif 'M' in dateFormat:
      freq = 'T'
    elif 'H' in dateFormat:
      freq = 'H'
    elif 'd' in dateFormat:
      freq = 'D'
    elif 'm' in dateFormat:
      freq = 'M'
    elif 'Y' in dateFormat:
      freq = 'Y'
    
    predictDf = pd.date_range(start=startDate, end=endDate, freq=freq)
    isLabel = False
    output["result"] = {
        "dataFrame": predictDf,
        "columns": dfColumnNms
    }
    isLabel = False
    return output


@WedaLogDecorator(text="Get Data ...", logLevel="info")
def getData(evalInfo, log):
    global columnNms
    global originColumnNms
    global hyperParam
    global mdlPath
    global isLabel
    global dfColumnNms
    global testColumnNms
    global inputColumn

    inputType = evalInfo["evalType"]
    output = {
        "status": 200,
        "message": "",
        "result": None
    }

    if inputType.lower() == "file":
        getDataResult = getFileData(evalInfo=evalInfo, log=log)

        if getDataResult["status"] == 200:
            predictDf = getDataResult["result"]["dataFrame"]

            if isLabel:
                for column in testColumnNms:
                    if column in hyperParam["dataInfo"]["encodeData"]:
                        predictDf[column].fillna("None", inplace=True)
                    else:
                        predictDf[column].fillna(0, inplace=True)

            else:
                for column in testColumnNms:
                    if column in hyperParam["dataInfo"]["encodeData"]:
                        predictDf[column].fillna("None", inplace=True)
                    else:
                        predictDf[column].fillna(0, inplace=True)
            
            inputColumn = predictDf.to_dict(orient="records")

            output["result"] = {
                "dataFrame": predictDf,
                "columns": getDataResult["result"]["columns"]
            }

        else:
            output["status"] = 400
            output["message"] = "can't read data"

    elif inputType.lower() == "request":
        getDataResult = getCurlData(evalInfo=evalInfo, log=log)
        if getDataResult["status"] == 200:
            predictDf = getDataResult["result"]["dataFrame"]
            if isLabel:
                for column in testColumnNms:
                    if column in hyperParam["dataInfo"]["encodeData"]:
                        predictDf[column].fillna("None", inplace=True)
                    else:
                        predictDf[column].fillna(0, inplace=True)

            else:
                for column in testColumnNms:
                    if column in hyperParam["dataInfo"]["encodeData"]:
                        predictDf[column].fillna("None", inplace=True)
                    else:
                        predictDf[column].fillna(0, inplace=True)
            
            inputColumn = predictDf.to_dict(orient="records")
            output["result"] = {
                "dataFrame": predictDf,
                "columns": getDataResult["result"]["columns"]
            }

        else:
            output["status"] = 400
            output["message"] = "can't read data"

    elif inputType.lower() == "database":
        log.info("db들어왔다")
        getDataResult = getDBData(dataInfo=evalInfo, log=log)

        if getDataResult["status"] == 200:
            predictDf = getDataResult["result"]["dataFrame"]

            if isLabel:
                for column in testColumnNms:
                    if column in hyperParam["dataInfo"]["encodeData"]:
                        predictDf[column].fillna("None", inplace=True)
                    else:
                        predictDf[column].fillna(0, inplace=True)

            else:
                for column in testColumnNms:
                    if column in hyperParam["dataInfo"]["encodeData"]:
                        predictDf[column].fillna("None", inplace=True)
                    else:
                        predictDf[column].fillna(0, inplace=True)
                        
            inputColumn = predictDf.to_dict(orient="records")
           
            output["result"] = {
                "dataFrame": predictDf
            }

        else:
            output["status"] = 400
            output["message"] = "can't read data"
            
    elif inputType.lower() == "dataset":
        getDataResult = getDataset(evalInfo=evalInfo, log=log)

        if getDataResult["status"] == 200:
            predictDf = getDataResult["result"]["dataFrame"]

            if isLabel:
                for column in testColumnNms:
                    if column in hyperParam["dataInfo"]["encodeData"]:
                        predictDf[column].fillna("None", inplace=True)
                    else:
                        predictDf[column].fillna(0, inplace=True)

            else:
                for column in testColumnNms:
                    if column in hyperParam["dataInfo"]["encodeData"]:
                        predictDf[column].fillna("None", inplace=True)
                    else:
                        predictDf[column].fillna(0, inplace=True)
            
            inputColumn = predictDf.to_dict(orient="records")
            output["result"] = {
                "dataFrame": predictDf,
                "columns": getDataResult["result"]["columns"]
            }   
            
    elif inputType.lower() == "timeseries":
        getDataResult = getTimeSeries(evalInfo=evalInfo, log=log)

        if getDataResult["status"] == 200:
            predictDf = getDataResult["result"]["dataFrame"]


            output["result"] = {
                "dataFrame": predictDf,
                "columns": getDataResult["result"]["columns"]
            }

    else:
        output["status"] = 400
        output["message"] = "check your inputType"
    return output


@WedaLogDecorator(text="Model Evaluation ...", logLevel="info")
def getGraphData(purposeType=None, yTest=None, yPred=None, log=None):
    global hyperParam
    global labelColumnNms
    global isLabel

    yTestLength = len(list(set(yTest)))

    graphData = []
    output = {
        "status": 200,
        "message": "",
        "result": []
    }
    g = graph(param=hyperParam, classes=labelColumnNms, log=log)

    log.info("Starting {} Evaluation...".format(purposeType.capitalize()))
    if purposeType.lower() == "regression":
        if isLabel:
            log.info("Regression isLabel Data...")
            yTest = np.array(yTest)
            yPred = np.array(yPred)
            # REG Plot
            regPlotOutput = g.regPlot(yTest=yTest, yPred=yPred, log=log)
            graphData.append(regPlotOutput)

            # distribution Plot
            distributionPlotOutput = g.distributionPlot(
                yTest=yTest, yPred=yPred, log=log)
            graphData.append(distributionPlotOutput)

            output["result"] = graphData
        else:
            log.info("Regression noLabel Data")
            graphData = None
            output["result"] = graphData

    elif purposeType.lower() == "classification":
        if isLabel:
            log.info("Classification is-Label Data...")
            yTest, yPred = mappingEncodeData(yTest=yTest, yPred=yPred)

            barChartOutput = g.barChart(yTest=yTest, yPred=yPred, log=log)
            graphData.append(barChartOutput)

            yTest = np.array(yTest)
            yPred = np.array(yPred)

            yTestBinary = label_binarize(yTest, classes=range(len(labelColumnNms)))
            yPredBinary = label_binarize(yPred, classes=range(len(labelColumnNms)))

            if yTestLength > 1:
                # Precision Recall Curve
                preRecallOutput = g.precisionRecall(yTest=yTestBinary, yPred=yPredBinary, log=log)
                graphData.append(preRecallOutput)

                # ROC Curve
                rocOutput = g.roc(yTest=yTestBinary, yPred=yPredBinary, log=log)
                graphData.append(rocOutput)

            # Confusion Matrix
            confMat = g.confusionMatrix(yTest=yTest, yPred=yPred, classes=labelColumnNms, log=log)
            graphData.append(confMat)

            output["result"] = graphData
    

        else:
            log.info("Classification no-Label Data...")
            _, yPred = mappingEncodeData(yPred=yPred)
            yPred = np.array(yPred)

            noLabelOutput = g.noLabelBarChart(yPred, log=log)
            graphData.append(noLabelOutput)

            output["result"] = graphData

    return output


def getEnData(xTest):
    global columnNms
    global originColumnNms
    global hyperParam

    encodeData = []
    for col in columnNms:
        for i in range(len(xTest)):
            tmp = xTest[i]
            if tmp["header"] == col:
                if tmp["header"] in list(hyperParam["dataInfo"]["encodeData"].keys()):
                    encodeData.append(
                        hyperParam["dataInfo"]["encodeData"][tmp["header"]][tmp["value"]] if tmp["value"] in hyperParam["dataInfo"]["encodeData"][tmp["header"]] else 0
                    )
                else:
                    encodeData.append(tmp["value"])

    return encodeData


@WedaErrorDecorator
def main(param=None):
  global p
  global hyperParam
  global columnNms
  global originColumnNms
  global dfColumnNms
  global testColumnNms
  global labelColumnNm
  global labelColumnNms
  global purposeType
  global log
  global isLabel
  global inputColumn
  global timeColumn

  yPred = []
  yTest = []
  getDataOutput = None
  resultData = []
  inputColumn = []
  
  output = {
      "status": 200,
      "message": "",
      "evalInfo": None,
      "graph": None,
      "result": None
  }

  getDataOutput = getData(evalInfo=param, log=log)
  try:
    if getDataOutput is not None:
      if getDataOutput["status"] == 200:
        if purposeType != "timeSeries":
            predictDf = getDataOutput["result"]["dataFrame"]

            for idx, tmp in predictDf.iterrows():
                xTestTmp = []
                for j in range(len(testColumnNms)):

                    if testColumnNms[j] == labelColumnNm:
                        if isLabel:
                            yTestTmp = tmp[j]
                        else:
                            yTestTmp = None
                        continue
                    else:
                        yTestTmp = None
                    xTestTmp.append({
                        "header": testColumnNms[j],
                        "value": tmp[j]
                    })

                encodeData = getEnData(xTestTmp)
                xTest = np.array(encodeData)
                # xTest = xTest.reshape((1, -1))
                xTest = xTest.reshape(1, -1)
                st = time.time()
                
                tmpResult = p.runPredict(xTest=xTest, yTest=yTestTmp, log=log)
                if tmpResult["status"] == 200:
                    predY = tmpResult["result"]["yPred"]
                    score = tmpResult["result"]["score"]

                    if purposeType == "regression":
                        yTest.append(yTestTmp)
                        yPred.append(predY[0])
                        
                        resultData.append(
                            {"dataRow": inputColumn[idx], # 테스트 해보기 api, file일 때
                                "accuracy": "{:.4f}".format(float(score)),
                                "dpLabel": "{:.4f}".format(float(predY[0])),
                                "predictTime": float(time.time() - st)
                            }
                        )
                    elif purposeType == "classification":
                        yTest.append(yTestTmp)
                        yPred.append(labelColumnNms[predY[0][0]] if predY is not None else None)
                        
                        resultData.append(
                            {
                                "dataRow": inputColumn[idx],
                                "accuracy": "{:.4f}".format(float(score)),
                                "dpLabel": labelColumnNms[predY[0][0]] if predY is not None else None,
                                "predictTime": float(time.time() - st)
                            }
                        )
                    elif purposeType == "clustering":
                        yTest.append(yTestTmp)
                        yPred.append(predY[0])

                        resultData.append(
                            {
                              "dataRow": inputColumn[idx], # 테스트 해보기 api, file일 때
                              "accuracy": "{:.4f}".format(float(score)),
                              "dpLabel": int(predY[0]),
                              "predictTime": float(time.time() - st)
                            }
                        )
                    elif purposeType == "timeSeries":
                        yTest.append(yTestTmp)
                        yPred.append(predY[0])
                        resultData.append(
                            {
                              "dataRow": inputColumn[idx], # 테스트 해보기 api, file일 때
                              "accuracy": "{:.4f}".format(float(score)),
                              "dpLabel": "{:.4f}".format(float(predY[0])),
                              "predictTime": float(time.time() - st)
                            }
                        )

            output["result"] = resultData

            if tmpResult["status"] == 200:
                graphData = getGraphData(
                    purposeType=purposeType,
                    yTest=yTest,
                    yPred=yPred,
                    log=log
                )
                param["isLabel"] = isLabel
                output["evalInfo"] = param

                if graphData["status"] == 200:
                    output["graph"] = graphData["result"]
            else:
                output["status"] = 400
                output["message"] = tmpResult["message"]
                
        else:
          xTest = getDataOutput["result"]["dataFrame"].astype(str).to_list()
          st = time.time()
          tmpResult = p.runPredict(xTest=xTest, yTest=None, log=log)
          yPred = tmpResult["result"]["yPred"]

          for idx in range(len(xTest)):
            resultData.append(
                {
                  "dataRow": {timeColumn: xTest[idx]}, # 테스트 해보기 api, file일 때
                  "dpLabel": yPred[idx],
                  "predictTime": float(time.time() - st)
                }
            )
          output["result"] = resultData
          
      else:
          output["status"] = 400
          output["message"] = graphData["message"]
    else:
        output["status"] = 400
        output["message"] = "can't read data"

  except Exception as e:
      print(e)
      print(traceback.format_exc())
      log.info(traceback.format_exc())
      log.info(e)

  return output


def setCategorical(dataFrame, columnTypeDict):
    encoderData = dict()
    le = LabelEncoder()
    columnList = list(dataFrame.columns)
    for column in columnList:
        if columnTypeDict[column] == 'object' or columnTypeDict[column] == 'bool' or columnTypeDict[column] == 'datetime64[ns]':  
            encoderData[column] = {}
            dataFrame[column].fillna("None", inplace=True)
            dataFrame[column] = le.fit_transform(dataFrame[column])
            
            for i in range(len(list(le.classes_))):
                encoderData[column][str(le.classes_[i])] = i
        else:
            dataFrame[column].fillna(0, inplace=True)

    return dataFrame
  

def causalMain(param=None):
  global columnDict
  
  output = {
    "status": 200,
    "message": "",
    "graph": None,
  }
  
  dataOutput = getCausalData(param) # 데이터로드
  df = dataOutput["result"]
  
  df = setCategorical(dataFrame=df, columnTypeDict=columnDict)
  
  if dataOutput["status"] == 200:
    modelOutput = trainModel(df)
    model = modelOutput["result"]
    
    if modelOutput["status"] == 200:
      graphOutput = causalGraph(model=model, df=df)
    
      if graphOutput["status"] == 200:
        output["graph"] = graphOutput["result"]
      else:
        output["status"] = 400
        output["message"] = graphOutput["message"]
  
    else:
      output["status"] = 400
      output["message"] = modelOutput["message"]
  
  else:
      output["status"] = 400
      output["message"] = dataOutput["message"]
  
  return output


def getCausalData(param):
  global columnDict

  output = {
    "status": 200,
    "message": "",
    "result": []
  }
  
  columnList = list(columnDict.keys())
  targetColumn = param["targetColumnName"]
  path = param["dataPath"][0]
  
  st = time.time()
  extension = pathlib.Path(path).suffix.lower()
  
  tmp = {}
  dateColumnList = []
  for i in columnDict:
    if columnDict[i] == "datetime64[ns]":
      dateColumnList.append(i)
    else:
      tmp[i] = columnDict[i]
  columnDict = tmp
  
  df = None
  if extension == '.csv' or extension == '.txt' or extension == '.text':
    df = pd.read_csv(path, dtype=columnDict, date_parser=dateColumnList, usecols=columnList) # categorical로 바꾼 컬럼 유지
  elif extension == '.xls' or extension == '.xlsx':
    df = pd.read_excel(path, dtype=columnDict, date_parser=dateColumnList, usecols=columnList) # categorical로 바꾼 컬럼 유지

  if ["purposeType"] == "classification":
    df[targetColumn] = df[targetColumn].apply(str)

  output["status"] = 200
  output["extTime"] = time.time() - st
  output["result"] = df
  
  return output


def trainModel(df):
  output = {
    "status": 200,
    "message": "",
    "result": []
  }
  
  pk = make_prior_knowledge(n_variables=len(df.columns), sink_variables=[4])
  model = lingam.DirectLiNGAM(prior_knowledge=pk)
  model = model.fit(df)
  output["result"] = model
  
  return output

def make_graph(adjacency_matrix, labels=None):
  idx = np.abs(adjacency_matrix) > 0.01
  dirs = np.where(idx)
  d = graphviz.Digraph(engine='dot')

  names = labels if labels else [f"x[1]" for i in range (len(adjacency_matrix))]
  for to, from_, coef in zip(dirs[0], dirs[1], adjacency_matrix[idx]):
    d.edge(names[from_], names[to], label=f'{coef:.2f}')
    
  return d


def causalGraph(df, model):
  output = {
    "status": 200,
    "message": "",
    "graph": None,
    "result": None
  }
  
  labels = [f"[{i}].{col}" for i, col in enumerate(df.columns)]

  dot = make_graph(model.adjacency_matrix_, labels)
  newDot = []

  for b in dot.body:
    b = b.replace("\t", "")
    b = b.replace("\n", "")
    b = b.replace("\"", "")
    newDot.append(b)
    
  output["result"] = newDot
  
  return output


# @app.route('/', methods=['POST'])
@app.route('/runCausalAnalysis', methods=['POST'])
def causalAnalysis():
    global log
    
    # data = '{"evalType": "file", "mlType": "tabular", "targetColumnName": "label", "dataPath": ["/Users/hb/tabular-model/test/boston.csv"]}'
    # param = json.loads(data)

    param = request.json
    print("PARAM!!!!!!! {}".format(param))
    log.info(param)
    output = causalMain(param=param)
    return jsonify(output)
  
  
# @app.route('/api/runEvaluation', methods=['POST'])
@app.route('/', methods=['POST'])
def runEvaluation():
    global log
    
    # data = '{"evalType":"file","mlType":"tabular","targetColumnName":"label","dataPath":["/Users/hb/Downloads/evaluation_sample (2).csv"],"start":0,"end":1}'
    # data = '{"evalType":"request","mlType":"tabular","targetColumnName":"Survived","dataBody":{"Passenger Id":4,"Pclass":2.308641975308642,"Name":"Futrelle, Mrs. Jacques Heath (Lily May Peel)","Sex":"female","Age":35,"SibSp":1,"Parch":0,"Ticket":"113803","Fare":53.1,"Cabin":"C123","Embarked":"S"}}'
    # data = '{"evalType": "request", "mlType": "tabular", "targetColumnName": None, "dataBody": {"gradyear": 2007.5, "gender": "M", "age": 17.993949546439755, "friends": 30.179466666666666, "basketball": 0.2673333333333333, "football": 0.2523, "soccer": 0.22276666666666667, "softball": 0.1612, "volleyball": 0.14313333333333333, "swimming": 0.1344, "cheerleading": 0.10663333333333333, "baseball": 0.10493333333333334, "tennis": 0.08733333333333333, "sports": 0.13996666666666666, "cute": 0.3228666666666667, "sex": 0.2094, "sexy": 0.1412, "hot": 0.1266, "kissed": 0.1032, "dance": 0.4251666666666667, "band": 0.2996, "marching": 0.0406, "music": 0.7378333333333333, "rock": 0.24333333333333335, "god": 0.4653, "church": 0.24816666666666667, "jesus": 0.11206666666666666, "bible": 0.021333333333333333, "hair": 0.42256666666666665, "dress": 0.11096666666666667, "blonde": 0.09893333333333333, "mall": 0.2573666666666667, "shopping": 0.353, "clothes": 0.1485, "hollister": 0.06986666666666666, "abercrombie": 0.051166666666666666, "die": 0.1841, "death": 0.11423333333333334, "drunk": 0.08796666666666667, "drugs": 0.06043333333333333}}'
    # param = json.loads(data)
    
    param = request.json
    print("PARAM!!!!!!! {}".format(param))
    log.info(param)
    output = main(param=param)
    return jsonify(output)


if __name__ == "__main__":
  output = {}
  try:
    # data = '{"runType":"evaluation","trainId":"469062dfbe89f593a06915419cf9b42c","dataInfo":{"mlType":"tabular","delimiter":",","targetColumn":"label","sourceType":"file","columnList":[{"columnName":"crim","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"zn","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"indus","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"chas","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"nox","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"rm","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"age","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"dis","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"rad","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"tax","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"ptratio","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"b","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"lstat","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"label","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true}],"purposeType":"regression","classInfo":[],"splitInfo":20},"columnTypeDict":{"crim":"float64","zn":"float64","indus":"float64","chas":"int64","nox":"float64","rm":"float64","age":"float64","dis":"float64","rad":"int64","tax":"int64","ptratio":"float64","b":"object","lstat":"float64","label":"float64"},"selectedHyperParam":{"gamma":0},"scoreMethod":"r2","pathInfo":{"trainPathList":["/Users/hb/tabular-model/test/boston.csv"],"weightPath":"/Users/hb/tabular-model/weight","logPath":"/Users/hb/tabular-model/test/train.log","pvPath":"/Users/hb/tabular-model/test","logLevel":"debug"}}'
    # data = '{"runType":"evaluation","trainId":"455a782aeaf3b9cba1f53f6a8196eb17","dataInfo":{"mlType":"tabular","delimiter":",","targetColumn":"label","sourceType":"file","columnList":[{"columnName":"crim","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"zn","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"indus","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"chas","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"nox","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"rm","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"age","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"dis","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"rad","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"tax","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"ptratio","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"b","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"lstat","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"label","classTf":false,"defaultValue":"null","checkTf":true}],"purposeType":"regression","classInfo":{},"splitInfo":20},"selectedHyperParam":{"max_depth":6,"patience":10,"earlyStopping":"true","monitor":"r2","mode":"auto","n_estimators":100,"learning_rate":0.3,"min_child_weight":1,"gamma":0,"colsample_bytree":1,"colsample_bylevel":1,"colsample_bynode":1,"subsample":1},"scoreMethod":"r2","pathInfo":{"trainPathList":["/Users/hb/Desktop/DATASET/reg/boston.csv"],"weightPath":"/Users/hb/tabular-model/weight","logPath":"/Users/hb/tabular-model/test/train.log","pvPath":"/Users/hb/tabular-model/modeldata/XGBoost-Regression","modelPath":"/Users/hb/tabular-model/modeldata/XGBoost-Regression","logLevel":"debug"}}'
    # data = '{"runType":"evaluation","trainId":"47bcb252e7213919ba92ed4a7c547aa3","dataInfo":{"mlType":"tabular","delimiter":",","targetColumn":"KS","sourceType":"file","columnList":[{"columnName":"MCH_CODE","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MCH_PRD_ID","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"INPUT_MAT_ID","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FET_GB","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_MIN_TP_14100","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_MAX_TP_14100","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_STD_TP_14100","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_MIN_TP_14240","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_MAX_TP_14240","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_STD_TP_14240","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MAT_TST_ML_02","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MAT_TST_T5","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MAT_TST_TS90","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MAT_TST_TENSILE_STREN","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE1_ML1_4","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE1_T5","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE1_TMAX","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE2_TS90","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE3_HARDNESS","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE2_REL_WEIGHT","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"SUB_MAT_STRETCH","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"SUB_MAT_TENSILE_STREN","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"UPPER_MOLD_TEMP","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"LOWER_MOLD_TEMP","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Pressure","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"KS","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true}],"purposeType":"regression","classInfo":[],"splitInfo":20},"selectedHyperParam":{"max_depth":6,"patience":10,"earlyStopping":"true","monitor":"r2","mode":"auto","n_estimators":100,"learning_rate":0.3,"min_child_weight":1,"gamma":0,"colsample_bytree":1,"reg_alpha":1,"reg_lambda":1,"colsample_bylevel":1,"colsample_bynode":1,"subsample":1},"scoreMethod":"r2","pathInfo":{"trainPathList":["/Users/hb/Desktop/tabular/시연/expoData.csv"],"weightPath":"/Users/hb/tabular-model/test/weight","logPath":"/Users/hb/tabular-model/test/train.log","pvPath":"/Users/hb/tabular-model/test","logLevel":"debug"}}'
    # data = '{"runType":"evaluation","trainId":"4ad0202428c1772fa39a05d439253d0e","dataInfo":{"mlType":"tabular","delimiter":",","targetColumn":null,"sourceType":"file","columnList":[{"columnName":"sepal length (cm)","classTf":false,"defaultValue":"null","columnType":"float64","checkTf":true},{"columnName":"sepal width (cm)","classTf":false,"defaultValue":"null","columnType":"float64","checkTf":true},{"columnName":"petal length (cm)","classTf":false,"defaultValue":"null","columnType":"float64","checkTf":true},{"columnName":"petal width (cm)","classTf":false,"defaultValue":"null","columnType":"float64","checkTf":true}],"purposeType":"clustering","classInfo":[{"className":"virginica"},{"className":"versicolor"},{"className":"setosa"}],"splitInfo":20},"selectedHyperParam":{"max_samples":"None", "prediction_data": "true"},"scoreMethod":"silhouette","pathInfo":{"trainPathList":["/Users/hb/tabular-model/test/iris.csv"],"weightPath":"/Users/hb/tabular-model/weight","logPath":"/Users/hb/tabular-model/test/train.log","pvPath":"/Users/hb/tabular-model/test","logLevel":"debug"}}'
    # data = '{"runType":"train","trainId":"44b8c9433f71207e86c258fcca5963d7","dataInfo":{"mlType":"tabular","delimiter":",","targetColumn":"Close","sourceType":"file","columnList":[{"columnName":"Date","columnType":"datetime64[ns]","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Open","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"High","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Low","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Close","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Adj Close","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Volume","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"date2","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true}],"purposeType":"timeSeries","classInfo":[],"splitInfo":{"trainRatio":{"startRatio":0,"endRatio":80,"startDate":"2021-01-04","endDate":"2021-03-08"},"validRatio":{"startRatio":80,"endRatio":90,"startDate":"2021-03-09","endDate":"2021-03-16"},"holdoutRatio":{"startRatio":90,"endRatio":100,"startDate":"2021-03-17","endDate":"2021-03-24"}},"timeColumn":"Date","dateFormat":"%Y-%m-%d","feDateFormat":"YYYY-MM-DD"},"selectedHyperParam":{"patience":10,"earlyStopping":"true","monitor":"r2","mode":"auto","changepoint_prior_scale":0.05,"seasonality_prior_scale":10,"holidays":"false","holidays_prior_scale":10,"seasonality_mode":"additive","changepoint_range":0.8,"growth":"linear"},"scoreMethod":"r2","pathInfo":{"trainPathList":["/Users/hb/Desktop/WEDA/Tabular/2023하반기/모델/timeseries/sample_ts.csv"],"weightPath":"/Users/hb/tabular-model/test/weight","logPath":"/Users/hb/tabular-model/test/train.log","pvPath":"/Users/hb/tabular-model/test","logLevel":"debug"}}'
    
    data = sys.argv[1]
    params = json.loads(data)

    serverParam = params.get("serverParam", None)

    if serverParam is not None:
      sendStatusUrl = '{}:{}/{}'.format(serverParam["serverIp"], int(
          serverParam["serverPort"]), serverParam["sendStatusUrl"])
    else:
      sendStatusUrl = params["pathInfo"]["logPath"]

    # log
    log = Logger(params["pathInfo"]["logPath"],
                  params["pathInfo"]["logLevel"])

    # model load
    output = modelLoad(param=params, log=log)
    if output["status"] == 200:
      output["result"] = "Model Load Success..."
      _ = sendMsg(sendStatusUrl, output, "EVAL", log=log)

      app.run(host='0.0.0.0', port=80)
    else:
      _ = sendMsg(sendStatusUrl, output, "EVAL", log=log)

  except Exception as e:
    print(e)
    print(traceback.format_exc())
    output["status"] = 400
    output["message"] = str(e)

    log.error(traceback.format_exc())

    _ = sendMsg(sendStatusUrl, output, "EVAL", log=log)
    exit(-1)
