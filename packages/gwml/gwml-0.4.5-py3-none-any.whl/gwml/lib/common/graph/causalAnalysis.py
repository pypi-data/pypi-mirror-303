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

# class causalAnaylsis:
  
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
      
  
def getData(param):
  output = {
    "status": 200,
    "message": "",
    "result": []
  }
  
  columnList = list(param["columnTypeDict"].keys())
  targetColumn = param["targetColumnName"]
  columnTypeDict = param["columnTypeDict"]
  path = param["dataPath"][0]
  
  st = time.time()
  extension = pathlib.Path(path).suffix.lower()
  
  tmp = {}
  dateColumnList = []
  for i in columnTypeDict:
    if columnTypeDict[i] == "datetime64[ns]":
      dateColumnList.append(i)
    else:
      tmp[i] = columnTypeDict[i]
  columnTypeDict = tmp
  
  df = None
  if extension == '.csv' or extension == '.txt' or extension == '.text':
    df = pd.read_csv(path, dtype=columnTypeDict, date_parser=dateColumnList, usecols=columnList) # categorical로 바꾼 컬럼 유지
  elif extension == '.xls' or extension == '.xlsx':
    df = pd.read_excel(path, dtype=columnTypeDict, date_parser=dateColumnList, usecols=columnList) # categorical로 바꾼 컬럼 유지

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
  names = labels if labels else [f'x[1]' for i in range (len(adjacency_matrix))]
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
  
  labels = [f'[{i}]. {col}' for i, col in enumerate(df.columns)]
  dot = make_graph(model.adjacency_matrix_, labels)
  newDot = []
  for b in dot.body:
    b = b.replace('\t', '')
    b = b.replace('\n', '')
    newDot.append(b)
    
  output["result"] = newDot
  
  return output


def causalAnaylsis(param=None):
  output = {
    "status": 200,
    "message": "",
    "graph": None,
  }
  
  dataOutput = getData(param) # 데이터로드
  df = dataOutput["result"]
  
  df = setCategorical(dataFrame=df, columnTypeDict=param["columnTypeDict"])
  
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


@app.route('/api/runCausalAnaylsis', methods=['POST'])
# @app.route('/', methods=['POST'])
def runCausalAnaylsis():
  global log
  
  # data = '{"evalType":"file","mlType":"tabular","targetColumnName":"label","dataPath":["/Users/hb/Downloads/evaluation_sample (2).csv"],"start":0,"end":1}'
  # data = '{"evalType":"request","mlType":"tabular","targetColumnName":"Survived","dataBody":{"Passenger Id":4,"Pclass":2.308641975308642,"Name":"Futrelle, Mrs. Jacques Heath (Lily May Peel)","Sex":"female","Age":35,"SibSp":1,"Parch":0,"Ticket":"113803","Fare":53.1,"Cabin":"C123","Embarked":"S"}}'
  # data = '{"evalType": "request", "mlType": "tabular", "targetColumnName": None, "dataBody": {"gradyear": 2007.5, "gender": "M", "age": 17.993949546439755, "friends": 30.179466666666666, "basketball": 0.2673333333333333, "football": 0.2523, "soccer": 0.22276666666666667, "softball": 0.1612, "volleyball": 0.14313333333333333, "swimming": 0.1344, "cheerleading": 0.10663333333333333, "baseball": 0.10493333333333334, "tennis": 0.08733333333333333, "sports": 0.13996666666666666, "cute": 0.3228666666666667, "sex": 0.2094, "sexy": 0.1412, "hot": 0.1266, "kissed": 0.1032, "dance": 0.4251666666666667, "band": 0.2996, "marching": 0.0406, "music": 0.7378333333333333, "rock": 0.24333333333333335, "god": 0.4653, "church": 0.24816666666666667, "jesus": 0.11206666666666666, "bible": 0.021333333333333333, "hair": 0.42256666666666665, "dress": 0.11096666666666667, "blonde": 0.09893333333333333, "mall": 0.2573666666666667, "shopping": 0.353, "clothes": 0.1485, "hollister": 0.06986666666666666, "abercrombie": 0.051166666666666666, "die": 0.1841, "death": 0.11423333333333334, "drunk": 0.08796666666666667, "drugs": 0.06043333333333333}}'
  # param = json.loads(data)
  
  param = request.json
  print("PARAM!!!!!!! {}".format(param))
  log.info(param)
  output = causalAnaylsis(param=param)
  print(output)
  return jsonify(output)


if __name__ == "__main__":
  output = {}
  try:
    # data = '{"runType":"evaluation","trainId":"43989485393f690483df0b418ba3dae8","dataInfo":{"mlType":"tabular","delimiter":",","targetColumn":"Close","sourceType":"file","columnList":[{"columnName":"Date","columnType":"datetime64[ns]","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Low","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Open","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Volume","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"High","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Close","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Adjusted Close","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FET_POST_CRE_TIME","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true}],"purposeType":"timeSeries","classInfo":[],"splitInfo":{"trainRatio":{"startRatio":0,"endRatio":80,"startDate":"1992-01-09","endDate":"2016-10-05"},"validRatio":{"startRatio":80,"endRatio":90,"startDate":"2016-10-06","endDate":"2019-11-09"},"holdoutRatio":{"startRatio":90,"endRatio":100,"startDate":"2019-11-10","endDate":"2022-12-12"}},"timeColumn":"Date","dateFormat":"%Y-%m-%d","feDateFormat":"YYYY-MM-DD"},"selectedHyperParam":{"patience":10,"earlyStopping":"true","monitor":"r2","mode":"auto","iterations":100,"order_p":10,"order_d":1,"order_q":1,"freq":"B","trend":"nc"},"scoreMethod":"r2","pathInfo":{"trainPathList":["/Users/hb/Downloads/WIRE_ts.csv"],"weightPath":"/Users/hb/tabular-model/test/weight","logPath":"/Users/hb/tabular-model/test/train.log","pvPath":"/Users/hb/tabular-model/test","logLevel":"debug"}}'
    # data = '{"runType":"evaluation","trainId":"455a782aeaf3b9cba1f53f6a8196eb17","dataInfo":{"mlType":"tabular","delimiter":",","targetColumn":"label","sourceType":"file","columnList":[{"columnName":"crim","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"zn","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"indus","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"chas","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"nox","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"rm","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"age","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"dis","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"rad","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"tax","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"ptratio","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"b","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"lstat","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"label","classTf":false,"defaultValue":"null","checkTf":true}],"purposeType":"regression","classInfo":{},"splitInfo":20},"selectedHyperParam":{"max_depth":6,"patience":10,"earlyStopping":"true","monitor":"r2","mode":"auto","n_estimators":100,"learning_rate":0.3,"min_child_weight":1,"gamma":0,"colsample_bytree":1,"colsample_bylevel":1,"colsample_bynode":1,"subsample":1},"scoreMethod":"r2","pathInfo":{"trainPathList":["/Users/hb/Desktop/DATASET/reg/boston.csv"],"weightPath":"/Users/hb/tabular-model/weight","logPath":"/Users/hb/tabular-model/test/train.log","pvPath":"/Users/hb/tabular-model/modeldata/XGBoost-Regression","modelPath":"/Users/hb/tabular-model/modeldata/XGBoost-Regression","logLevel":"debug"}}'
    # data = '{"runType":"evaluation","trainId":"47bcb252e7213919ba92ed4a7c547aa3","dataInfo":{"mlType":"tabular","delimiter":",","targetColumn":"KS","sourceType":"file","columnList":[{"columnName":"MCH_CODE","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MCH_PRD_ID","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"INPUT_MAT_ID","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FET_GB","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_MIN_TP_14100","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_MAX_TP_14100","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_STD_TP_14100","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_MIN_TP_14240","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_MAX_TP_14240","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"PEAK_STD_TP_14240","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MAT_TST_ML_02","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MAT_TST_T5","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MAT_TST_TS90","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"MAT_TST_TENSILE_STREN","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE1_ML1_4","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE1_T5","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE1_TMAX","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE2_TS90","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE3_HARDNESS","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FORCE2_REL_WEIGHT","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"SUB_MAT_STRETCH","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"SUB_MAT_TENSILE_STREN","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"UPPER_MOLD_TEMP","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"LOWER_MOLD_TEMP","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Pressure","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"KS","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true}],"purposeType":"regression","classInfo":[],"splitInfo":20},"selectedHyperParam":{"max_depth":6,"patience":10,"earlyStopping":"true","monitor":"r2","mode":"auto","n_estimators":100,"learning_rate":0.3,"min_child_weight":1,"gamma":0,"colsample_bytree":1,"reg_alpha":1,"reg_lambda":1,"colsample_bylevel":1,"colsample_bynode":1,"subsample":1},"scoreMethod":"r2","pathInfo":{"trainPathList":["/Users/hb/Desktop/tabular/시연/expoData.csv"],"weightPath":"/Users/hb/tabular-model/test/weight","logPath":"/Users/hb/tabular-model/test/train.log","pvPath":"/Users/hb/tabular-model/test","logLevel":"debug"}}'
    # data = '{"runType":"causalAnalysis","trainId":"4425e4a4f56020ddae517ecbef6c2790","dataInfo":{"mlType":"tabular","delimiter":",","targetColumn":"Close","sourceType":"file","columnList":[{"columnName":"Date","columnType":"datetime64[ns]","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Low","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Open","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Volume","columnType":"int64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"High","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Close","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"Adjusted Close","columnType":"float64","classTf":false,"defaultValue":"null","checkTf":true},{"columnName":"FET_POST_CRE_TIME","columnType":"object","classTf":false,"defaultValue":"null","checkTf":true}],"purposeType":"timeSeries","classInfo":[],"splitInfo":{"trainRatio":{"startRatio":0,"endRatio":80,"startDate":"1992-01-09","endDate":"2016-10-05"},"validRatio":{"startRatio":80,"endRatio":90,"startDate":"2016-10-06","endDate":"2019-11-09"},"holdoutRatio":{"startRatio":90,"endRatio":100,"startDate":"2019-11-10","endDate":"2022-12-12"}},"timeColumn":"Date","dateFormat":"%Y-%m-%d","feDateFormat":"YYYY-MM-DD"},"selectedHyperParam":{"max_depth":6,"patience":10,"earlyStopping":"true","monitor":"r2","mode":"auto","n_estimators":100,"learning_rate":0.3,"min_child_weight":1,"gamma":0,"colsample_bytree":1,"reg_alpha":1,"reg_lambda":1,"colsample_bylevel":1,"colsample_bynode":1,"subsample":1},"scoreMethod":"r2","pathInfo":{"trainPathList":["/Users/hb/Downloads/WIRE_ts.csv"],"weightPath":"/Users/hb/tabular-model/test/weight","logPath":"/Users/hb/tabular-model/test/train.log","pvPath":"/Users/hb/tabular-model/test","logLevel":"debug"}}'
    
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

    _ = sendMsg(sendStatusUrl, output, "EVAL", log=log)
    app.run(host='0.0.0.0', port=80)
    

  except Exception as e:
    print(e)
    print(traceback.format_exc())
    output["status"] = 400
    output["message"] = str(e)

    log.error(traceback.format_exc())

    _ = sendMsg(sendStatusUrl, output, "EVAL", log=log)
    exit(-1)
