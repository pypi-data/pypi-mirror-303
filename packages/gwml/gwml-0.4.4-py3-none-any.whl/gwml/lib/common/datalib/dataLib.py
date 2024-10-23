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

import os
import re
import sys
import time
import json
import pathlib
import traceback
import pandas as pd
import numpy as np

from posixpath import splitdrive
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import dask.dataframe as dd

basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(basePath)
sys.path.append(os.path.join(basePath, "decorator"))
from logger.WedaLogDecorator import WedaLogDecorator

class dataLib():

    # @WedaLogDecorator(text="get Train Data Start", logLevel="info")
    def __init__(self, param, log):
        self.param = param
        self.dataInfo = param["dataInfo"] if "dataInfo" in param else None
        self.pathInfo = param["pathInfo"] if "pathInfo" in param else None
        
        self.columnTypeDict = {}
        for i in param["dataInfo"]["columnList"]:
            self.columnTypeDict[i["columnName"]] = i["columnType"]
        self.columnList = [i["columnName"] for i in param["dataInfo"]["columnList"]]
        
        self.timeColumn = self.dataInfo.get("timeColumn", "")
        self.targetColumn = self.dataInfo.get("targetColumn", "")
        self.purposeType = self.dataInfo.get("purposeType", "")
        self.dateFormat = self.dataInfo.get("dateFormat", "")
        
        if self.timeColumn:
            self.trainStart = self.dataInfo["splitInfo"]["trainRatio"]["startDate"]
            self.trainEnd = self.dataInfo["splitInfo"]["trainRatio"]["endDate"]
            self.validStart = self.dataInfo["splitInfo"]["validRatio"]["startDate"]
            self.validEnd = self.dataInfo["splitInfo"]["validRatio"]["endDate"]
            self.holdoutStart = self.dataInfo["splitInfo"]["holdoutRatio"]["startDate"]
            self.holdoutEnd = self.dataInfo["splitInfo"]["holdoutRatio"]["endDate"]
        else:
            self.datasetSplit = float(int(self.dataInfo["splitInfo"].get("validRatio", 20))/100)
                
        self.dbInfo = self.dataInfo["dbInfo"] if "dbInfo" in self.dataInfo else None
        self.sep = self.dataInfo.get("delimiter", ",") if self.dataInfo is not None else ","
        self.log = log

    # setCategorical / set object data to num
    # @WedaLogDecorator(text="setCategorical", logLevel="info")
    def setCategorical(self, dataFrame, columnNms, log):
        encoderData = dict()
        le = LabelEncoder()
        for column in columnNms:
            if self.columnTypeDict[column] == 'object' or self.columnTypeDict[column] == 'bool' or self.columnTypeDict[column] == 'datetime64[ns]':  
                encoderData[column] = {}
                dataFrame[column].fillna("None", inplace=True)
                dataFrame[column] = le.fit_transform(dataFrame[column])
                for i in range(len(list(le.classes_))):
                    encoderData[column][str(le.classes_[i])] = i
            else:
                dataFrame[column].fillna(0, inplace=True)
        self.dataInfo["encodeData"] = encoderData

        return dataFrame

    
    def getTimeFileData(self, path, log):

        output = {
            "status": 400,
            "message": "",
            "extTime": None,
            "result": None
        }
        st = time.time()
        extension = pathlib.Path(path).suffix.lower()

        tmp = {}
        dateColumnList = []
        for i in self.columnTypeDict:
          if 'datetime' in self.columnTypeDict[i]:
            dateColumnList.append(i)
          else:
            tmp[i] = self.columnTypeDict[i]
        
        if extension == '.csv' or extension == '.txt' or extension == '.text':
            # df = pd.read_csv(path, sep=self.sep, dtype=tmp, usecols=self.columnList, parse_dates=dateColumnList) # categorical로 바꾼 컬럼 유지
            df = dd.read_csv(path, dtype=tmp)
            
        elif extension == '.xls' or extension == '.xlsx':
            df = pd.read_excel(path, dtype=tmp, usecols=self.columnList, parse_dates=dateColumnList) # categorical로 바꾼 컬럼 유지
        
        
        for i in dateColumnList:
          df[i] = dd.to_datetime(df[i])
        
        df = df.compute()
        output["status"] = 200
        output["extTime"] = time.time() - st
        output["result"] = df
        return output
      
    # getFileData / Common Filedata -> allData in output["result"] (type:dataFrame)
    # @WedaLogDecorator(text="getFileData", logLevel="info")
    def getFileData(self, path, log):

        output = {
            "status": 400,
            "message": "",
            "extTime": None,
            "result": None
        }
        st = time.time()
        extension = pathlib.Path(path).suffix.lower()
        df = None
        
        tmp = {}
        dateColumnList = []
        for i in self.columnTypeDict:
          if 'datetime' in self.columnTypeDict[i]:
            dateColumnList.append(i)
          else:
            tmp[i] = self.columnTypeDict[i]
        
        if extension == '.csv' or extension == '.txt' or extension == '.text':
            # df = pd.read_csv(path, sep=self.sep, dtype=tmp, usecols=self.columnList, parse_dates=dateColumnList) # categorical로 바꾼 컬럼 유지
            df = dd.read_csv(path, dtype=tmp)
            
        elif extension == '.xls' or extension == '.xlsx':
            df = pd.read_excel(path, dtype=tmp, usecols=self.columnList, parse_dates=dateColumnList) # categorical로 바꾼 컬럼 유지

        for i in dateColumnList:
          df[i] = dd.to_datetime(df[i])
          
        df = df.compute()
        output["status"] = 200
        output["extTime"] = time.time() - st
        output["result"] = df
        return output

    # getDbData / Common Dbdata -> allData in output["result"] (type:dataFrame)
    # @WedaLogDecorator(text="getDbData", logLevel="info")
    def getDbData(self, dbInfo, log):
        self.log.info(dbInfo)
        output = {
            "status": 400,
            "message": "",
            "extTime": None,
            "result": None
        }
        st = time.time()
        dbType = dbInfo["client"].lower()
        df = None
        if dbType == "mysql":
            import pymysql
            conn = pymysql.connect(
                host=dbInfo["address"],
                port=int(dbInfo["port"]),
                database=dbInfo["dbName"],
                user=dbInfo["user"],
                password=dbInfo["password"]
            )
            st = time.time()
            df = pd.read_sql(dbInfo["query"], conn)
            output["extTime"] = time.time() - st
            output["status"] = 200
            output["result"] = df
            conn.close()

        elif dbType == "oracle":
            import cx_Oracle as co

            oraclePath = os.environ["ORACLE_HOME"]
            co.init_oracle_client(lib_dir=os.path.join(oraclePath, "lib"))

            st = time.time()
            dsnTns = co.makedsn(dbInfo["address"], int(dbInfo["port"]), dbInfo["dbName"])
            conn = co.connect(user=dbInfo["user"], password=dbInfo["password"], dsn=dsnTns)
            df = pd.read_sql(sql=dbInfo["query"], con=conn, columns=self.columnList)
            output["extTime"] = time.time() - st
            output["status"] = 200
            output["result"] = df
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
            df = pd.read_sql(dbInfo["query"], conn)
            output["extTime"] = time.time() - st
            output["status"] = 200
            output["result"] = df
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
            df = pd.read_sql(dbInfo["query"], conn)
            output["extTime"] = time.time() - st
            output["status"] = 200
            output["result"] = df
            conn.close()

        return output

    # getData / Common data -> xTrain, xTest, yTrain, yTest in output["result"] (type:numpy)
    @WedaLogDecorator(text="Getting Data...", logLevel="info")
    def getData(self, log, dataFrame=None):
        output = {
            "status": 400,
            "message": "",
            "extTime": None,
            "result": None
        }
        xTrain = yTrain = xTest = yTest = None

        if self.dataInfo["sourceType"].lower() == "file":
            if len(self.pathInfo["trainPathList"]) > 0:
                dataFrame = pd.DataFrame()
                trainDs = pd.DataFrame()
                testDs = pd.DataFrame()

                for path in self.pathInfo["trainPathList"]:
                    if self.purposeType == "timeSeries":
                      tmp = self.getTimeFileData(path=path, log=log)
                    else:
                      tmp = self.getFileData(path=path, log=log)

                    if tmp["status"] == 200: 
                        # dataFrame = dataFrame.append(tmp["result"])
                        dataFrame = pd.concat([dataFrame, tmp["result"]], axis=0)
                        
                    elif tmp["status"] == 400:
                        # output["result"] = "{} File Not Found Error".format(os.path.basename(path))
                        output["result"] = "{} File Not Found Error".format(path)
                        break

                if tmp["status"] == 200:
                    try:
                        columnNms = []
                        
                        for mapping in self.dataInfo["columnList"]:
                                columnNms.append(mapping["columnName"])

                        newColNameList = []
                        for colName in columnNms:
                            if colName == self.dataInfo["targetColumn"]:
                                pass
                            else:
                                if re.search("^[A-Za-z0-9_.\\-/>]*$", colName):
                                    pass
                                else:
                                    colName = colName.replace("(", "_")
                                    colName = colName.replace(")", "_")
                                    colName = colName.replace(" ", "_")
                                newColNameList.append(colName)
                            
                        self.dataInfo["columnNameList"] = newColNameList
                        self.dataInfo["originColumnNameList"] = columnNms
                        
                        # trainDs, testDs split
                        if self.timeColumn == "":

                            if float(self.datasetSplit) != 0 or "testPath" not in self.dataInfo:
                                dataFrame = self.setCategorical(dataFrame=dataFrame, columnNms=columnNms, log=log)
                                trainDs, testDs = train_test_split(
                                    dataFrame,
                                    test_size=float(self.datasetSplit),
                                    random_state=66,
                                    shuffle=True,
                                    stratify=dataFrame[self.dataInfo["targetColumn"]] if self.param["dataInfo"]["purposeType"].lower() == "classification" else None
                                )

                            else:
                                trainDs = dataFrame

                                for path in self.dataInfo["testPath"]:
                                    tmp = self.getFileData(path=path, log=log)
                                    if tmp["status"] == 200:
                                        testDs = testDs.append(tmp["result"])

                                    elif tmp["status"] == 400:
                                        output["result"].append("{} File Error".format(os.path.basename(path)))
                                        continue
                        else:
                            dataFrame.index = dataFrame[self.timeColumn]
                            dataFrame = self.setCategorical(dataFrame=dataFrame, columnNms=columnNms, log=log)
                            
                            trainDs = dataFrame[(dataFrame.index <= self.trainEnd) & (dataFrame.index >= self.trainStart)]
                            trainDs = trainDs.reset_index(drop=True)
                            
                            testDs = dataFrame[(dataFrame.index <= self.validEnd) & (dataFrame.index >= self.validStart)]
                            testDs = testDs.reset_index(drop=True)
                            
                            holdoutDs = dataFrame[(dataFrame.index <= self.holdoutEnd) & (dataFrame.index >= self.holdoutStart)]              
                            holdoutDs = holdoutDs.reset_index(drop=True)


                            output["status"] = 200

                    except Exception as e:
                        print(str(e))
                        print(traceback.format_exc())
                        self.log.error(traceback.format_exc())
            else:
                output["status"] = 400
                output["message"] = "check Dataset!"

        elif self.dataInfo["sourceType"].lower() == "database":
            self.log.info(self.dataInfo)
            tmp = self.getDbData(dbInfo=self.dbInfo, log=log)
          
            if tmp["status"] == 200:
                try:
                    columnNms = []
                    for mapping in self.dataInfo["columnList"]:
                            columnNms.append(mapping["columnName"])

                    newColNameList = []
                    for colName in columnNms:
                        if colName == self.dataInfo["targetColumn"]:
                            pass
                        else:
                            if re.search("^[A-Za-z0-9_.\\-/>]*$", colName):
                                pass
                            else:
                                colName = colName.replace("(", "_")
                                colName = colName.replace(")", "_")
                                colName = colName.replace(" ", "_")
                            newColNameList.append(colName)
                        
                    self.dataInfo["originColumnNameList"] = columnNms 
                    self.dataInfo["columnNameList"] = newColNameList

                    # trainDs, testDs split
                    if float(self.datasetSplit) != 0 or "testPath" not in self.dataInfo:
                        dataFrame = self.setCategorical(dataFrame=tmp["result"], columnNms=columnNms, log=log)
                        if self.timeColumn == "":
                          trainDs, testDs = train_test_split(
                              dataFrame,
                              test_size=float(self.datasetSplit),
                              stratify=dataFrame[self.dataInfo["targetColumn"]] if self.param["dataInfo"]["purposeType"].lower() == "classification" else None,
                              random_state=66,
                              shuffle=True
                          )
                        else:
                          trainDs = dataFrame[(dataFrame[self.timeColumn] <= self.trainEnd) & (dataFrame[self.timeColumn] >= self.trainStart)]
                          testDs = dataFrame[(dataFrame[self.timeColumn] <= self.validEnd) & (dataFrame[self.timeColumn] >= self.validStart)]
                          holdoutDs = dataFrame[(dataFrame[self.timeColumn] <= self.holdoutEnd) & (dataFrame[self.timeColumn] >= self.holdoutStart)]
                          
                    output["status"] = 200

                except Exception as e:
                    print(str(e))
                    print(traceback.format_exc())
                    self.log.error(traceback.format_exc())
                    
        elif self.dataInfo["sourceType"].lower() == "dataframe":
            try:
                columnNms = []
                for mapping in self.dataInfo["columnList"]:
                    columnNms.append(mapping["columnName"])
                newColNameList = []
                for colName in columnNms:
                    if colName == self.dataInfo["targetColumn"]:
                        pass
                    else:
                        if re.search("^[A-Za-z0-9_.\\-/>]*$", colName):
                            pass
                        else:
                            colName = colName.replace("(", "_")
                            colName = colName.replace(")", "_")
                            colName = colName.replace(" ", "_")
                        newColNameList.append(colName)
                    
                self.dataInfo["columnNameList"] = newColNameList
                self.dataInfo["originColumnNameList"] = columnNms

                if float(self.datasetSplit) != 0 or "testPath" not in self.dataInfo:
                    dataFrame = self.setCategorical(dataFrame=dataFrame, columnNms=columnNms, log=log)
                    trainDs, testDs = train_test_split(
                        dataFrame,
                        test_size=float(self.datasetSplit),
                        random_state=66,
                        shuffle=True,
                        stratify=dataFrame[self.dataInfo["targetColumn"]] if self.param["dataInfo"]["purposeType"].lower() == "classification" else None
                    )
                output["status"] = 200
                    
            except Exception as e:
                print(str(e))
                print(traceback.format_exc())
                self.log.error(traceback.format_exc())

        if output["status"] == 200:
            if self.dataInfo["sourceType"].lower() != "dataframe":
                trainDs = pd.DataFrame(trainDs, columns=columnNms)
                testDs = pd.DataFrame(testDs, columns=columnNms)
                
            xTrain = trainDs.drop([self.dataInfo["targetColumn"]], axis=1)
            yTrain = trainDs[self.dataInfo["targetColumn"]]
            xTest = testDs.drop([self.dataInfo["targetColumn"]], axis=1)
            yTest = testDs[self.dataInfo["targetColumn"]]
            output["result"] = {
                "xTrain": xTrain,
                "yTrain": yTrain,
                "xTest": xTest,
                "yTest": yTest
            } 

        return output