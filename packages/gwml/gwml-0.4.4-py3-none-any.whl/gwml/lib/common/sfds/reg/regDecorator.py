import joblib
import os
# 각 파라미터 별 타입 지정 필요
import datetime
import numpy as np

from sklearn.metrics import r2_score as r2
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
commonPath = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir), os.path.pardir), os.path.pardir), "common"))

def rmse(y_test, y_pred):
    return np.sqrt(mse(y_test, y_pred))    
  
def train(func):
    def wrapper(self, *args, **kwargs):
        output =  {
            "status": 200,
            "massage": "",
            "result": {
                "r2": None,
                "mse": None,
                "mae": None,
                "rmse": None,
                "endTime": None,
                "dur": None
            },
            "score": None,
            "yPred": []
        }
        
        # 함수 호출
        result = func(self, *args, **kwargs)
        output["yPred"] = result[0]
        # 반환 값 수정
        output["user"] = result[1:]
        
        return output
    return wrapper


def validation(func):
    def wrapper(self, xTest:list, yTest:list, model):
        output =  {
            "status": 200,
            "massage": "",
            "result": {
                "r2": None,
                "mse": None,
                "mae": None,
                "rmse": None,
                "endTime": None,
                "dur": None
            },
            "score": None,
            "yPred": []
        }

        # 함수 호출
        result = func(self, xTest, yTest, model)
        
        
        try:
          yPred = self.model.predict(xTest)
          
          if np.array(yPred).ndim != 1:
            yPred = np.array(yPred).flatten().tolist()
            
          endTime = datetime.datetime.now()
          output["yPred"] = yPred
          output["result"]["r2"] = r2(yTest, yPred)
          output["result"]["mse"] = mse(yTest, yPred)
          output["result"]["mae"] = mae(yTest, yPred)
          output["result"]["rmse"] = rmse(yTest, yPred)
          output["result"]["endTime"] = endTime.astimezone().replace(microsecond=0).isoformat()
          output["result"]["startTime"] =  self.startTime.astimezone().replace(microsecond=0).isoformat()
          output["result"]["dur"] = float("{:.4f}".format(endTime.timestamp() - self.startTime.timestamp()))          
          
        except Exception as e:
          output["status"] = 400
          output["message"] = str(e)
        finally:
          # custom
          output["custom"] = result
        
        return output
    return wrapper


def predict(func):
    def wrapper(self, *args, **kwargs):
        output =  {
            "status": 200,
            "massage": "",
            "score": None,
            "yPred": []
        }
        
        # 함수 호출
        yPred = func(self, *args, **kwargs)
        if np.array(yPred).ndim != 1:
          yPred = np.array(yPred).flatten().tolist()
        output["yPred"] = yPred

          
        # 반환 값 수정
        output["custom"] = yPred
        return output
    return wrapper




# ===========================데코레이터 활용===========================

# learningModel 정의
class wedaLearningModel():
    def __init__(self, startTime:datetime, param_grid:dict={}, param:dict={}, log=None): #  *args, **kwargs
      
        self.param = param
        self.param_grid = param_grid
        self.scoreMethod = param.get("scoreMethod", "r2")
        self.weightPath = self.param["pathInfo"]["weightPath"]
        self.saveMdlPath = os.path.join(self.weightPath, "weight.pkl")
        
        self.log = log
        self.startTime = startTime
        self.params = {}

        os.makedirs(self.weightPath, exist_ok=True)
        
        if 'n_estimators' in self.param_grid.keys():
            self.epochs = self.param_grid["n_estimators"]
        elif 'max_iter' in self.param_grid.keys():
            self.epochs = self.param_grid["max_iter"]
        elif 'n_neighbors' in self.param_grid.keys():
            self.epochs = self.param_grid["n_neighbors"]
        elif 'iterations' in self.param_grid.keys():
            self.epochs = self.param_grid["iterations"]
        else:
            self.epochs = 0

        self.epochs = int(self.epochs)
        self.fstEpochStartTime = 0
        self.fstEpochEndTime = 0
  
class predictor:
  def __init__(self, param):

    self.saveMdlPath = os.path.join(param, "weight.pkl")
    self.model =  joblib.load(open(self.saveMdlPath, "rb"))
    
  def __call__(self, func, xTest:list, yTest:list=None):
    
    def wrapper():

        output =  {
            "status": 200,
            "massage": "",
            "score": None,
            "yPred": []
        }
        
        # 함수 호출
        result = func(self, xTest, yTest)
        try:
          output["yPred"] = result
          
          yPred = output["yPred"]
          if np.array(yPred).ndim != 1:
            yPred = np.array(yPred).flatten().tolist()
          output["result"]["yPred"] = yPred
        
        except Exception as e:
          output["status"] = 400
          output["message"] = str(e)
        finally:
          # output["custom"] = [result[1:]]
          return output
          
    return wrapper