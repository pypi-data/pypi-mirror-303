import hyperopt
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

def RMSE(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

SEED = 3

# load dataset
data = load_boston()

# train, test split
x_train, x_test, y_train, y_test = train_test_split(data['data'], data['target'], random_state=SEED)

print(x_train.shape, y_train.shape)
# 출력
# (379, 13) (379,)



# regularization candiate 정의
reg_candidate = [1e-5, 1e-4, 1e-3, 1e-2, 0.1, 1, 5, 10, 100]

# space 정의, Hyperparameter의 이름을 key 값으로 입력
space={'max_depth': hp.quniform("max_depth", 5, 15, 1),
       'learning_rate': hp.quniform ('learning_rate', 0.01, 0.05, 0.005),
       'reg_alpha' : hp.choice('reg_alpha', reg_candidate),
       'reg_lambda' : hp.choice('reg_lambda', reg_candidate),
       'subsample': hp.quniform('subsample', 0.6, 1, 0.05),
       'colsample_bytree' : hp.quniform('colsample_bytree', 0.6, 1, 0.05),
       'min_child_weight' : hp.quniform('min_child_weight', 1, 10, 1),
       'n_estimators': hp.quniform('n_estimators', 200, 1500, 100)
      }

# 목적 함수 정의
# n_estimators, max_depth와 같은 반드시 int 타입을 가져야 하는 hyperparamter는 int로 타입 캐스팅 합니다.
def hyperparameter_tuning(space, x_train2, y_train2):
    print(space)
    model=XGBRegressor(n_estimators =int(space['n_estimators']), 
                       max_depth = int(space['max_depth']), 
                       learning_rate = space['learning_rate'],
                       reg_alpha = space['reg_alpha'],
                       reg_lambda = space['reg_lambda'],
                       subsample = space['subsample'],
                       colsample_bytree = space['colsample_bytree'], 
                       min_child_weight = int(space['min_child_weight']),
                       random_state=SEED, 
                      )
    print(model)
    # model=XGBRegressor(n_estimators =int(space['n_estimators']), 
    #                    max_depth = int(space['max_depth']), 
    #                    learning_rate = space['learning_rate'],
    #                    reg_alpha = space['reg_alpha'],
    #                    reg_lambda = space['reg_lambda'],
    #                    subsample = space['subsample'],
    #                    colsample_bytree = space['colsample_bytree'], 
    #                    min_child_weight = int(space['min_child_weight']),
    #                    random_state=SEED, 
    #                   )
    # evaluation = [(x_train, y_train), (x_test, y_test)]
    model.n_estimators = n_estimators =int(space['n_estimators'])
    best_score = cross_val_score(model, x_train2, y_train2, 
                                 scoring='r2', 
                                 cv=5, 
                                 n_jobs=8).mean()
    loss = 1 - best_score

    # model.fit(x_train, y_train,
    #           eval_set=evaluation, 
    #           eval_metric="rmse",
    #           early_stopping_rounds=20,
    #           verbose=0)

    # pred = model.predict(x_test)
    # rmse= RMSE(y_test, pred)    
    # 평가 방식 선정
    print(loss)
    return {'loss':loss, 'status': STATUS_OK, 'model': model}

# Trials 객체 선언합니다.
trials = Trials()
# best에 최적의 하이퍼 파라미터를 return 받습니다.
best = fmin(fn=hyperparameter_tuning,
            space=space,
            algo=tpe.suggest,
            x_train2 = x_train,
            y_train2 = y_train,
            max_evals=50, # 최대 반복 횟수를 지정합니다.
            trials=trials)

# 최적화된 결과를 int로 변환해야하는 파라미터는 타입 변환을 수행합니다.
best['max_depth'] = int(best['max_depth'])
best['min_child_weight'] = int(best['min_child_weight'])
best['n_estimators'] = int(best['n_estimators'])
best['reg_alpha'] = reg_candidate[int(best['reg_alpha'])]
best['reg_lambda'] = reg_candidate[int(best['reg_lambda'])]
best['random_state'] = SEED
print (best)
# {'colsample_bytree': 0.8, 'learning_rate': 0.02, 'max_depth': 10, 'min_child_weight': 2, 'n_estimators': 700, 'reg_alpha': 1, 'reg_lambda': 0.001, 'subsample': 0.65, 'random_state': 30}    