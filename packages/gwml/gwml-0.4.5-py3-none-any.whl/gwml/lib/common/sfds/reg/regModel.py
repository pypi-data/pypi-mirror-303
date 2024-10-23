import os
import datetime


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