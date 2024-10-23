import json
import os 
import datetime

class utils():
  def getDatetime():
      return datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    
  def initData(data):
    params = json.loads(data)
    runType = params["runType"]
    serverParam = params.get("serverParam", None)

    return runType, params, ""
  
  def getHyperParam(selectedHyperParam, basePath):
    param_grid = {}
    with open(os.path.join(basePath, "hyperParamScheme.json"), "r") as jsonFile:
      hyperParamScheme = json.load(jsonFile) 
    
    # param_grid = selectedHyperParam
    for key in hyperParamScheme:
      if key != "earlyStopping":
        for param in hyperParamScheme[key]:
            paramNm = param["parameterName"]
            
            if paramNm in selectedHyperParam:
              value = selectedHyperParam[paramNm] 
            else:
              value = param["defaultValue"]

            if param["type"] == "string":
                if value != "None":
                  value = str(value)
                else:
                  value = None
                
            elif param["type"] == "float":
                value = float(value)
                
            elif param["type"] == "int":
                value = int(value)
                
            elif param["type"] == "bool":
                if value == "true":
                  value = True
                elif value == "false":
                  value = False
                else:
                  value = bool(value)
                  
            elif param["type"] == "chr":
                value = chr(value)
                
            elif param["type"] == "str/int":
                if value != "None":
                  value = int(value) 
                else:
                  value = None
                  
            elif param["type"] == "str/float":
                if value != "None":
                  value = float(value) 
                else:
                  value = None

            param_grid[param["parameterName"]] = value
      # else:
      #   for param in hyperParamScheme[key]:
      #       if param["parameterName"] in selectedHyperParam:
      #             param_grid[param["parameterName"]] = selectedHyperParam[param["parameterName"]]
                  
    return param_grid