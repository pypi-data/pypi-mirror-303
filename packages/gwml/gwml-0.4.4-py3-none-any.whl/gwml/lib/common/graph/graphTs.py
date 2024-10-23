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
import sys
import math
import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose


basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(basePath)
sys.path.append(os.path.join(basePath, "decorator"))
from logger.WedaLogDecorator import WedaLogDecorator


class graphTs:
    # @WedaLogDecorator(text="graphInit", logLevel="info")
    def __init__(self, param, classes, log):
        self.param = param
        self.classes = classes
        self.nClasses = 0
        if classes is not None:
            self.nClasses = len(self.classes)
        self.log=log
        self.feDateFormat = param["dataInfo"]["feDateFormat"]

    
    def timeDecomposeGraph(self, xTrain, yTrain, xTest, yTest, yPred, log):
      seriesList = []
      
      xTrain = xTrain.tolist()
      yTrain = yTrain.tolist()
      xTest = xTest.tolist()
      yTest = yTest.tolist()
      yPred = yPred.tolist()
      
      orgDf = pd.DataFrame()
      orgDf["x"] = xTrain+xTest # date
      orgDf["y"] = yTrain+yTest
      orgDf.index = pd.to_datetime(orgDf["x"])
      
      prdDf = pd.DataFrame()
      prdDf["x"] = xTest # date
      prdDf["y"] = yPred  
      prdDf.index = pd.to_datetime(prdDf["x"])
      
      try:
        deTrain = seasonal_decompose(orgDf["y"], model='additive')
      except:
        deTrain = seasonal_decompose(orgDf["y"], model='additive', period=7)
        
      try:
        deTest = seasonal_decompose(prdDf["y"], model='additive')
      except:
        deTest = seasonal_decompose(prdDf["y"], model='additive', period=7)
      
      trainTrend = deTrain.trend.dropna().values.tolist()
      testTrend = deTest.trend.dropna().values.tolist()
      
      trainData = list(map(list, zip(orgDf["x"].values.tolist(), trainTrend)))
      testData = list(map(list, zip(prdDf["x"].values.tolist(), testTrend)))
    
      
      seriesList.append({
          "seriesName": "Trend(train)",
          "seriesType": "line",
          "seriesData": trainData,
      })
      
      seriesList.append({
          "seriesName": "Trend(test)",
          "seriesType": "line",
          "seriesData": testData,
      })
      
      
      # trainSeasonal = deTrain.seasonal.dropna().values.tolist()
      # trainData = list(map(list, zip(orgDf["x"].values.tolist(), trainSeasonal)))
      
      # testSeasonal = deTest.seasonal.dropna().values.tolist()
      # testData = list(map(list, zip(prdDf["x"].values.tolist(), testSeasonal)))
      
      # seriesList.append({
      #     "seriesName": "Seasonal(train)",
      #     "seriesType": "line",
      #     "seriesData": trainData,
      # })
      
      # seriesList.append({
      #     "seriesName": "Seasonal(test)",
      #     "seriesType": "line",
      #     "seriesData": testData,
      # })            
      
      output = {
            "chartName": "Trend",
            "dateFormat": self.feDateFormat,
            "desc": "",
            "chartType": "timeDecomposition",
            "legendX": "Date",
            "legendY": "Value",
            "series": seriesList
      }
      return output
  
  
    # @WedaLogDecorator(text="forecastChart...", logLevel="info")    
    def forecastChart(self, xTrain, yTrain, xTest, yTest, forecast, log):
      yhat = forecast["yhat"].values
      yhat_lower = forecast["yhat_lower"].values
      yhat_upper = forecast["yhat_upper"].values
      
      yTrainList = list(map(list, zip(xTrain, yTrain)))
      yTestList = list(map(list, zip(xTest, yTest)))
      yhatList = list(map(list, zip(xTest, yhat)))
      yhat_lowerList = list(map(list, zip(xTest, yhat_lower)))
      yhat_upperrList = list(map(list, zip(xTest, yhat_upper)))
      
      
      
      seriesList = []
      
      seriesList.append({
                "seriesName": "yTrain",
                "seriesType": "line",
                "seriesData": yTrainList,
            })
      
      seriesList.append({
                "seriesName": "yTest",
                "seriesType": "line",
                "seriesData": yTestList,
            })
      
      seriesList.append({
          "seriesName": "yPred",
          "seriesType": "line",
          "seriesData": yhatList,
      })
      
      seriesList.append({
          "seriesName": "yPred_lower",
          "seriesType": "line",
          "area" : True,
          "seriesData": yhat_lowerList,
      })
      
      seriesList.append({
          "seriesName": "yPred_upper",
          "seriesType": "line",
          "area" : True,
          "seriesData": yhat_upperrList,
      })      
      
      output = {
            "chartName": "Forecast Chart",
            "desc": "",
            "chartType": "forecastChart",
            "legendX": "Date",
            "legendY": "Value",
            "series": seriesList
        }
      
      return output
    
    
    
    # @WedaLogDecorator(text="actualPredictChart", logLevel="info")
    def actualPredictChart(self, xTest, yTest, yPred, log):
        seriesList = []
        testList = list(map(list, zip(xTest, yTest)))
        predictList = list(map(list, zip(xTest, yPred)))

        residual = list(map(lambda x,y : abs(x-y), yTest, yPred))
        residualList = list(map(list, zip(xTest, residual)))
        
        
        seriesList.append({
                        "seriesName": "yTest",
                        "seriesData": testList,
                    })
        
        seriesList.append({
                    "seriesName": "yPred",
                    "seriesData": predictList,

                })
        
        seriesList.append({
                  "seriesName": "잔차",
                  "seriesType": "bar",
                  "seriesData": residualList
                })
        
        output = {
                    "chartName": "실제와 예측 비교",
                    "desc": "",
                    "chartType": "actualPredictChart",
                    "legendX": "Date",
                    "legendY": "Target",
                    "series": seriesList
                }
        
        return output

    
    # @WedaLogDecorator(text="regPlot", logLevel="info")
    def regPlot(self, yTest, yPred, log):
        chartList = []

        m, b = np.polyfit(yTest, yPred, 1)
        pt = m * yTest + b
        xMin = min(yTest)
        xMax = max(yTest)
        yMin = min(pt)
        yMax = max(pt)

        for i in range(len(yTest)):
            if (not math.isnan(float(yTest[i]))) and (not math.isnan(float(yPred[i]))):
                chartList.append(
                    
                    [float('{:.4f}'.format(yTest[i])), float('{:.4f}'.format(yPred[i]))]

                )

        output =  {

                "chartName": "Reg Plot",
                "desc": "",
                "chartType": "Reg Plot",
                "legendX": "yLabel",
                "legendY": "yPred",
                "series": [{
                      "seriesName": "Reg Plot",
                      "seriesType": "scatter",
                      "seriesData": chartList,
                    },
                    {
                        "seriesName": "baseLine",
                        "seriesType": "line",
                        "seriesData": [
                            
                            [float('{:.4f}'.format(xMin)),float('{:.4f}'.format(yMin)) ],
                            [float('{:.4f}'.format(xMax)) ,float('{:.4f}'.format(yMax)) ]
                    ]
      
                    }       
                ]

            }

        return output

    # @WedaLogDecorator(text="distributionPlot", logLevel="info")
    def distributionPlot(self, yTest, yPred, log):
        yTestchartList = []
        yPredchartList = []
        chartList = []

        for i in range(len(yTest)):
            if not math.isnan(float(yTest[i])):
                yTestchartList.append(
                    
                    [float('{:.4f}'.format(i)), float('{:.4f}'.format(yTest[i]))]
 
                )

        chartList.append(
 
                # "chartName": "Distribution Plot of yTest Data",
                {
                    "seriesName": "Distribution Plot of yTest Data",
                    "seriesData": yTestchartList,
                }

        )

        for i in range(len(yPred)):
            if not math.isnan(float(yPred[i])):
                yPredchartList.append(
                    
                    [float('{:.4f}'.format(i)), float('{:.4f}'.format(yPred[i]))]

                )

        chartList.append(
                {
                    "seriesName": "Distribution Plot of yPred Data",
                    "seriesData": yPredchartList
                }
        )

        output = {
                "chartName": "Distribution Plot of yPred Data",
                "chartType": "Distribution Plot",
                "legendX": "Amount of Test Dataset",
                "legendY": "yTest and yPred",
                "desc": "",
                "series": chartList
            }
        
        return output

