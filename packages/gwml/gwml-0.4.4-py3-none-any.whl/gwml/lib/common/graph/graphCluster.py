import os
import json
import sys
import pandas as pd
import numpy as np
import joblib

from sklearn.decomposition import PCA
from collections import defaultdict
from scipy.cluster.hierarchy import dendrogram, linkage

basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(basePath)
sys.path.append(os.path.join(basePath, "decorator"))
from logger.WedaLogDecorator import WedaLogDecorator

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) # FutureWarning 제거

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))
  
class graph:
  def __init__(self, param, originColumnNms, clusterList, log):
    self.param = param
    self.clusterList = clusterList
    self.nClasses = 0
    self.originColumnNms = originColumnNms
    self.log=log
  
  def clusterTable(self, graphDf, clusterDf, columnTypeDict, log):

    seriesList = []
    clusterList = []
    tableDict = defaultdict(dict)
    yPred = clusterDf.values
    clusterInfo = clusterDf.value_counts()
  
    for i, j in zip(clusterInfo.index, clusterInfo):
      clusterList.append({str(i):round(j/len(graphDf)*100, 3)})
      
    clusterInfo.index = clusterInfo.index.astype(str)
    clusterInfo = clusterInfo.to_dict()

    pca = PCA(n_components=2)
    pca_transformed = pca.fit_transform(graphDf)
    pca_x = pca_transformed[:, 0]  # x좌표
    pca_y = pca_transformed[:, 1]  # y좌표
    
    pcaDf = pd.DataFrame()
    pcaDf["pca_x"] = pca_x
    pcaDf["pca_y"] = pca_y
    pcaDf["cluster"] = yPred.tolist()

    for cluster in self.clusterList:
      indexList = []
      indexList = np.where(yPred == cluster)[0]
      indexList = [*indexList]
      tmp = graphDf.loc[indexList]

      seriesList.append(
            {
              "seriesName": cluster, 
              "seriesData": round(pcaDf[pcaDf["cluster"]==cluster], 3).values.tolist()
            }
          )
      

      aggDf = round(tmp.agg(["count", "min", "max","mean","std"]), 3)
      aggDf.loc["avg"] = aggDf.loc["mean"]
      aggDf = aggDf.fillna('nan')
      aggDf = aggDf.drop("mean")
      aggDf = aggDf.to_dict()

      for column in aggDf:
        if not tableDict[column]:
          tableDict[column]["columnName"] =  column
          tableDict[column]["type"] = columnTypeDict[column]
          
        if columnTypeDict[column] in ["int64", "float64"]:
          tableDict[column][str(cluster)] = aggDf[column]
          
          
        else:
          leDict = joblib.load('label_encoder.joblib')
          tmp[column] = leDict[column].inverse_transform(tmp[column].astype(int))
          tableDict[column][str(cluster)] = tmp[column].value_counts().sort_values(ascending=False).to_dict()

    newTableList = []
    for column in tableDict:
      tableDict[column]["columnName"] = column
      newTableList.append(tableDict[column])
      
    output = {
        "chartName": "클러스터 분석 결과",
        "desc": "",
        "chartType": "clusterResult",
        "clusterList": clusterList,
        "table": newTableList,
        "legendX": "PCA1",
        "legendY": "PCA2",
        "series": seriesList
      }
    
    return output
        
  def clusterBarChart(self, graphDf, yPred, log):
    allDf = pd.DataFrame(graphDf, columns=self.originColumnNms)
    allDf["cluster"] = yPred

    tmp = []
    for i in self.clusterList:
      tmp.append(len(allDf[allDf["cluster"]==i]))

    output = {
            "chartName": "Cluster Count Chart",
            "desc": "",
            "chartType": "clusterBarChart",
            "seriesCategory": self.clusterList,
            "series": [
              {
                "legendX": "Cluster", 
                "legendY": "Count",
                "seriesName": "Cluster Count",
                "seriesData": tmp
              }
            ]
        }

    return output

  def dendrogram(self, graphDf, yPred, clusterList, log):
    allDf = pd.DataFrame(graphDf, columns=self.originColumnNms)
    allDf["cluster"] = yPred
      
    yPred = allDf["cluster"].values
    
    Z = linkage(allDf, method="ward")
    values = dendrogram(Z, labels=yPred, no_plot=True, truncate_mode="lastp")
    leafNameList = values["ivl"]
    for i in range(len(leafNameList)):
      leafNameList[i] = str(leafNameList[i]).replace("(", "")
      leafNameList[i] = str(leafNameList[i]).replace(")", "")
    
    seriesList = []
    cnt = 0
    
    seriesData = list(zip(values["icoord"], values["dcoord"], values["leaves_color_list"]))
    sorted_list = list(map(list, seriesData))
    sorted_list.sort(key=lambda x: x[0][0])

    for i, value in enumerate(sorted_list):
      data = []
      for j in range(4):
        tmp = [value[0][j], value[1][j]]
        if tmp[1] == 0.0:
          tmp.append(leafNameList[cnt])
          cnt += 1
        data.append(tmp)

      seriesList.append({"seriesName" : i, "seriesData": data, "color": value[2]})
    
    output = {
        "chartName": "덴드로그램",
        "desc": "",
        "chartType": "dendrogram",
        "ivl": leafNameList,
        "series": seriesList
    }
    return output


  def hubertChart(self, modelOutput, log):
    seriesData = []
    inertiaDict = modelOutput["inertiaDict"]
    
    for i in inertiaDict:
      seriesData.append([i, round(inertiaDict[i], 2)])
    
    valueList = list(inertiaDict.values())
    
    max = 0
    value = 0
    for i in range(len(valueList)-1):
      tmp = abs(valueList[i+1] - valueList[i]) 
      if max < tmp:
        max = tmp
        value = i+1
        
    output = {
        "chartName": "휴버트 지수",
        "desc": "",
        "chartType": "hubertChart",
        "xLine": value+2,
        "legendX": "Cluster",
        "legendY": "Total Whthin Sum of Square",
        "series": [{"seriesName" : "all", "seriesData": seriesData}]
    }
    
    return output
  
  
  def clusterValueChart(self, modelOutput, log):
    seriesList = []
    
    for name in modelOutput: # {"AIC": {0:0.23456}}
      seriesData = []
      tmp = modelOutput[name]
      for cluster in tmp:
        seriesData.append([cluster, tmp[cluster]])
      
      seriesList.append({"seriesName" : name, "seriesData": seriesData})
        
      output = {
          "chartName": "",
          "desc": "",
          "chartType": "clusterScore",
          "legendX": "Cluster",
          "legendY": "Score",
          "series": seriesList
      }
    
    return output
  

  def clusterHeatmap(self, graphDf, yPred, log):
    seriesList = []
    allDf = pd.DataFrame(graphDf, columns=self.originColumnNms)
    allDf["cluster"] = yPred
    groupbyDf = allDf.groupby(["cluster"]).mean()
    cluster_mean = groupbyDf.transpose()

    # 데이터 스케일 -> 상대적으로 특징차이가 보이도록
    # 모든변수의 최소가 0이 되도록 조절
    
    mean_table = cluster_mean.div(cluster_mean.max(axis=1), axis=0)
    mean_table = mean_table.fillna(0)
    seriesList.append({"seriesName": "heatmap", "legendX": mean_table.columns.tolist(), "legendY": mean_table.index.tolist()[::-1], "seriesData": mean_table.values.tolist()})

    output = {
        "chartName": "Cluster Heatmap",
        "desc": "",
        "chartType": "clusterHeatmap",
        "series": seriesList
      }
    return output