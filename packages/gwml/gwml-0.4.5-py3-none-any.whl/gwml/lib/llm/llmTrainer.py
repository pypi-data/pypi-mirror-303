import os
import sys
import time
import json
import pathlib
import datetime



basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
commonPath = os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),"common") # os.path.abspath("../common")

sys.path.append(os.path.join(commonPath, "sender"))
sys.path.append(os.path.join(commonPath, "decorator"))


from logger.Logger import Logger
from sender import sendMsg


class trainer(): 
    def __init__(self, params, log=None):
        self.model = None
        self.startTime = time.time()
        self.param = params
        self.log = log
        
    def getTrainResult(self, model, sendResultUrl, log):
        output = {
            "status": 200,
            "message": "",
            "extTime": None,
            "result": None,
        }

        self.model = model()
        self.model.main(dataPath=self.param["dataPath"], param=self.param)

        _ = sendMsg(sendResultUrl, output, "TRAIN", log)
        
        return output
      


def train(params={}): 
    startTime = datetime.datetime.now()
    params["pathInfo"] = {}
    params["pathInfo"]["weightPath"] = "./"
    
    t = trainer(params=params)
    print(params)
    
    modelPath = params["modelPath"]
    modelDirPath = os.path.dirname(modelPath)
    
    if modelDirPath not in sys.path:
        sys.path.append(modelDirPath)
    
    from model import customModel
    sendResultUrl = ""
    log = Logger("log.log", "info")
    
    output = t.getTrainResult(model=customModel, sendResultUrl=sendResultUrl, log=log)
    
      

# if __name__ == '__main__':
#     model_name = "bert-base-uncased"
#     dataPath = "/Users/hb/weda/LGD/LLM/bert_sample.json"
#     param = {"modelPath": "/Users/hb/customGW/customTestLLM/model.py", "dataPath": dataPath, "config":{"max_length":32,"batch_size":2,"epochs":3,"learning_rate":2e-5}}

#     # 모델 일반 학습
#     # 파라미터: df(학습할 데이터 프레임), lm(model.py에서 정의한 learningModel 클래스), hyperParamSceme(모델의 하이퍼 파라미터), target(타겟명)
#     model = train(params=param)
