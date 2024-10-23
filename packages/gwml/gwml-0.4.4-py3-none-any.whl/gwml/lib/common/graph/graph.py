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

from sklearn import metrics
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt


basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(basePath)
sys.path.append(os.path.join(basePath, "decorator"))
from logger.WedaLogDecorator import WedaLogDecorator


class graph:
    # @WedaLogDecorator(text="graphInit", logLevel="info")
    def __init__(self, param, classes, log):
        self.param = param
        self.classes = classes
        self.nClasses = 0
        if classes is not None:
            self.nClasses = len(self.classes)
        self.log=log

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
                "chartType": "Reg Plot",
                "series": [{
                    "seriesName": "Reg Plot",
                    "seriesType": "scatter",
                    "legendX": "yLabel",
                    "legendY": "yPred",
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
                # "chartName": "Distribution Plot of yPred Data",
                {
                    "seriesName": "Distribution Plot of yPred Data",
                    "legendX": "Amount of Test Dataset",
                    "legendY": "yTest and yPred",
                    "seriesData": yPredchartList
                }
        )

        output = {
                "chartType": "Distribution Plot",
                "series": chartList
            }
        
        return output

    # @WedaLogDecorator(text="roc", logLevel="info")
    def roc(self, yTest, yPred, log):
        fpr = dict()
        tpr = dict()
        roc_auc = dict()

        fpr["micro"], tpr["micro"], _ = metrics.roc_curve(yTest.ravel(), yPred.ravel())
        roc_auc["micro"] = metrics.auc(fpr["micro"], tpr["micro"])

        microROCPosition = []
        for i in range(len(fpr['micro'])):
            microROCPosition.append(
                
                [float('{:.4f}'.format(fpr['micro'][i])), float('{:.4f}'.format(tpr['micro'][i]))]

            )

        output = {
                    "chartName": "ROC Curve",
                    "chartType": "ROC Curve",
                    "area": '{:.4f}'.format(roc_auc["micro"]),
                    "series": [{
                        "seriesName": "ROC Curve",
                        "seriesData": microROCPosition,
                        "legendX": "False Positive Rate",
                        "legendY": "True Positive Rate"
                    }]
                }
       

        return output

    # @WedaLogDecorator(text="precisionRecall", logLevel="info")
    def precisionRecall(self, yTest, yPred, log):
        precision = dict()
        recall = dict()
        average_precision = dict()

        precision["micro"], recall["micro"], _ = metrics.precision_recall_curve(yTest.ravel(), yPred.ravel())
        average_precision["micro"] = metrics.average_precision_score(yTest, yPred, average="micro")

        microPRPosition = []
        for i in range(len(precision['micro'])):
            microPRPosition.append(
                
                [float('{:.4f}'.format(recall['micro'][i])), float('{:.4f}'.format(precision['micro'][i]))]

            )
 
        output = {
                    "chartName": "Precision Recall Curve",
                    "chartType": "Precision Recall Curve",
                    "area": '{:.4f}'.format(average_precision["micro"]),
                    "series": [{
                        "seriesName": "Precision Recall Curve",
                        "seriesData": microPRPosition,
                        "legendX": "recall",
                        "legendY": "precision"
                    }]
                }

        return output

    # @WedaLogDecorator(text="confusionMatrix", logLevel="info")
    def confusionMatrix(self, yTest, yPred, classes, log):
        if type(yTest[0]) != str:
            labels = range(0, len(classes))
        else:
            labels = classes

        cm = metrics.confusion_matrix(yTest, yPred, normalize="all", labels=labels)
        cm = cm.tolist()
        newCm = []

        for data in cm:
            tmpCm = []
            for tmp in data:
                tmpCm.append(float('{:.4f}'.format(tmp)))
            newCm.append(tmpCm)

        output = {
                "chartName": "Confusion Matrix",
                "chartType": "Confusion Matrix",
                "series": [{
                    "seriesName": "Confusion Matrix",
                    "seriesData": newCm,
                    "legendX": classes,
                    "legendY": classes[::-1]
                    }]
            }
        return output

    # @WedaLogDecorator(text="featureImportance", logLevel="info")
    def featureImportance(self, columnNms, fiValue, log):
        fImp = list(fiValue)
        fImpAll = 0
        featureImp = []

        for i in range(len(columnNms)):
            fImpAll += fImp[i]

        for j in range(len(fImp)):
            fImp[j] = float(fImp[j] / fImpAll)

        dictFi = dict(zip(columnNms, fImp))
        dictFi = sorted(dictFi.items(), reverse=True, key=lambda item: item[1])

        
        seriesCategory = []
        seriesData = []
        for k in range(len(dictFi)):
            seriesCategory.append('{}'.format(dictFi[k][0]),)
            seriesData.append('{:.4f}'.format(dictFi[k][1]))
        
        output = {
                "chartName": "Feature Importance",
                "chartType": "Feature Importance",
                "seriesCategory": seriesCategory,
                "series": [
                {   
                    "seriesName": "Feature Importance",
                    "seriesData": seriesData
                }]
            }
        return output

    # @WedaLogDecorator(text="permutationImportance", logLevel="info")
    def permutationImportance(self, model, xTest, yTest, columnNms, n_repeats, log):
        pImp = permutation_importance(model, xTest, yTest, n_repeats=n_repeats, random_state=42)
        pImp_mean = pImp.importances_mean
        pImpAll = 0

        permutationImp = []
        for i in range(len(columnNms)):
            if pImp_mean[i] < 0:
                pImp_mean[i] = 0.0
            pImpAll += pImp_mean[i]

        for j in range(len(pImp_mean)):
            if pImpAll == 0:
                pImp_mean[j] = float(1/len(pImp_mean))
            else:
                pImp_mean[j] = float(pImp_mean[j] / pImpAll)

        dictPi = dict(zip(columnNms, pImp_mean))
        dictPi = sorted(dictPi.items(), reverse=True, key=lambda item: item[1])

        seriesCategory = []
        seriesData = []
        for k in range(len(dictPi)):
            seriesCategory.append('{}'.format(dictPi[k][0]))
            seriesData.append('{:.4f}'.format(dictPi[k][1]))


        output = {
                "chartName": "Feature Importance",
                "chartType": "Feature Importance",
                "seriesCategory": seriesCategory,
                "series": [{
                    "seriesName": "Feature Importance",
                    "seriesData" : seriesData
                    
                    }]
            }

        return output

    # @WedaLogDecorator(text="barChart", logLevel="info")
    def barChart(self, yTest, yPred, log):
        correctCount = 0
        failCount = 0

        yTest = list(yTest)
        yPred = list(yPred)

        for i in range(len(yPred)):
            if yTest[i] == yPred[i]:
                correctCount += 1
            else:
                failCount += 1

        correctRate = correctCount/(correctCount+failCount)

        yTestCount = []
        yPredCount = []
        for classNm in self.classes:
            yTestCount.append(yTest.count(self.classes.index(classNm)))
            yPredCount.append(yPred.count(self.classes.index(classNm)))

        yTestInfo = {
            "legendX": "Classes", 
            "legendY": "Count",
            "seriesName": "yTestCount",
            "seriesData": yTestCount
        }

        yPredInfo = {
            "seriesName": "yPredCount",
            "seriesData": yPredCount
        }

        output = {
                "chartName": "Bar Chart",
                "chartType": "Bar Chart",
                "classList": self.classes,
                "correctCount": correctCount,
                "failCount": failCount,
                "correctRate": correctRate,
                "series": [yTestInfo, yPredInfo]
            }

        return output

    # @WedaLogDecorator(text="noLabelBarChart", logLevel="info")
    def noLabelBarChart(self, yPred, log):
        predictClass = []
        barInfo = {}

        yPred = list(yPred)
        for pred in yPred:
            predictClass.append(self.classes[pred])

        classNms = list(set(predictClass))
        
        yPredCount = []
        for classNm in classNms:
            classCount = predictClass.count(classNm)
            yPredCount.append(classCount)

        yPredInfo = {
            "legendX": "Classes",
            "legendY": "Count",
            "seriesName": "yPredCount",
            "seriesData": yPredCount
        }

        output = {
                "chartName": "Bar Chart(noLabel)",
                "chartType": "Bar Chart(noLabel)",
                "classList": classNms,
                "series": [yPredInfo],
            }

        return output
      
    def featureEffect(self, xTest, yTest, yPred, columnNms, partialDict, target, columnFlag, log): # purposeType이 regression인 경우
      
      chartList = []
      dataframe = pd.DataFrame(xTest, columns=columnNms)
      dataframe["y_test"] = yTest
      dataframe["y_pred"] = yPred
      
      for index, col in enumerate(columnNms):
      
        series = []
        if col not in ["y_test", "y_pred"]:
            
          if columnFlag[col]=="pass":
            continue
          
          elif columnFlag[col] == "int64": # 정수일 때
            
            # partial depencence
            series.append({"seriesName": "partial depencence", "seriesType": "line", "seriesData": partialDict[col]}) 
            
            # Actual
            newDf = dataframe[[col, "y_test"]]
            groupyResult = newDf.groupby(col).agg({"y_test": ["mean"]})
            groupyResult = groupyResult.reset_index()
            groupyResult = groupyResult.round(4)
            series.append({"seriesName": "Actual", "seriesType": "line","seriesData": groupyResult.values.tolist()})
            
            # Predict
            newDf = dataframe[[col, "y_pred"]]
            groupyResult = newDf.groupby(col).agg({"y_pred": ["mean"]})
            groupyResult = groupyResult.reset_index()
            groupyResult = groupyResult.round(4)
            series.append({"seriesName": "Predict", "seriesType": "line", "seriesData": groupyResult.values.tolist()})
            # chartList.append({"chartName": col, "legendX" : col, "legendY": f"Target ({target})", "series":series})
              
            newDf = dataframe[[col]]
            groupyResult = newDf.groupby(col).agg({col: ["count"]})
            groupyResult = groupyResult.reset_index()
            groupyResult = groupyResult.round(4)
            series.append({"seriesName": "Histogram", "seriesType": "bar", "seriesData": groupyResult.values.tolist()})
            
            chartList.append({"chartName": col, "xMin": float(dataframe[col].min()), "xMax": float(dataframe[col].max()), "legendX" : col, "legendY": f"Target ({target})", "series":series})

          else:
            if columnFlag == "float64-20":
              hist, bins = np.histogram(dataframe[col], bins=20)
            else:
              hist, bins = np.histogram(dataframe[col])
              
            hist = hist.tolist()
            bins = bins.tolist()
            
            # partial depencence
            series.append({"seriesName": "partial dependence", "seriesType": "line", "seriesData": partialDict[col]})
            
            # Actual
            seriesData = []
            newDf = dataframe[[col, "y_test"]]
            
            for i in range(len(bins)-1):
              tmp1 = newDf[col] >= bins[i]
              tmp2 = newDf[col] < bins[i+1]
              meanYTest = newDf[tmp1 & tmp2].mean()["y_test"]
              if not np.isnan(meanYTest):
                seriesData.append([round(np.median([bins[i], bins[i+1]]),4), round(meanYTest, 4), bins[i], bins[i+1]])
              
            series.append({"seriesName": "Actual", "seriesType": "line", "seriesData": seriesData})
            
            # Predicted
            seriesData = []
            newDf = dataframe[[col, "y_pred"]]

            for i in range(len(bins)-1):
              tmp1 = newDf[col] >= bins[i]
              tmp2 = newDf[col] < bins[i+1]
              meanYPred = newDf[tmp1 & tmp2].mean()["y_pred"]
              if not np.isnan(meanYPred):
                seriesData.append([round(np.median([bins[i], bins[i+1]]),4), round(meanYPred, 4), bins[i], bins[i+1]])
            series.append({"seriesName": "Predict", "seriesType": "line", "seriesData": seriesData})
            
            # histogram
            seriesData = []    
            for i in range(len(bins)-1): 
              seriesData.append([round(np.median([bins[i], bins[i+1]]),4), hist[i], bins[i], bins[i+1]])
            series.append({"seriesName": "histogram", "seriesType": "bar", "seriesData": seriesData})
            
            chartList.append({"chartName": col, "xMin": float(dataframe[col].min()), "xMax": float(dataframe[col].max()), "binsCount": len(bins)-1, "binsRange": round(bins[1]-bins[0], 4), "legendX" : col, "legendY": f"Target ({target})", "series":series})
          
      output = {
          "chartTitle": "Feature Effect",
          "chartType" : "Feature Effect",
          "chartList": chartList
        }
      return output
  
  
    # def featureEffect(self, xTest, yTest, yPred, columnNms, partialDict, target, columnFlag, log): # purposeType이 regression인 경우
    #   chartList = []
      
    #   dataframe = pd.DataFrame(xTest, columns=columnNms)
    #   dataframe["y_test"] = yTest
    #   dataframe["y_pred"] = yPred

    #   for col in dataframe.columns:
    #     series = []
    #     if col not in ["y_test", "y_pred"]:
            
    #       if columnFlag[col]=="pass":
    #         continue
          
    #       elif columnFlag[col] == "int64": # 정수일 때
    #         # partial depencence
    #         series.append({"seriesName": "partial depencence", "seriesType": "line", "seriesData": partialDict[col]}) 
            
    #         dataframe = pd.DataFrame(xTest, columns=columnNms)
    #         dataframe["y_test"] = yTest
    #         dataframe["y_pred"] = yPred

    #         # Actual
    #         newDf = dataframe[[col, "y_test"]]
    #         groupyResult = newDf.groupby(col).agg({"y_test": ["mean"]})
    #         groupyResult = groupyResult.reset_index()
    #         groupyResult = groupyResult.round(4)
    #         series.append({"seriesName": "Actual", "seriesType": "line","seriesData": groupyResult.values.tolist()})
            
    #         # Predict
    #         newDf = dataframe[[col, "y_pred"]]
    #         groupyResult = newDf.groupby(col).agg({"y_pred": ["mean"]})
    #         groupyResult = groupyResult.reset_index()
    #         groupyResult = groupyResult.round(4)
    #         series.append({"seriesName": "Predict", "seriesType": "line", "seriesData": groupyResult.values.tolist()})
    #         # chartList.append({"chartName": col, "legendX" : col, "legendY": f"Target ({target})", "series":series})
              
    #         # bar (= histogram)
    #         newDf = dataframe[[col]]
    #         groupyResult = newDf.groupby(col).agg({col: ["count"]})
    #         groupyResult = groupyResult.reset_index()
    #         groupyResult = groupyResult.round(4)
    #         series.append({"seriesName": "Histogram", "seriesType": "bar", "seriesData": groupyResult.values.tolist()})
            
    #         chartList.append({"chartName": col, "xMin": float(dataframe[col].min()), "xMax": float(dataframe[col].max()), "legendX" : col, "legendY": f"Target ({target})", "series":series})

    #       else:
    #         # partial depencence
    #         series.append({"seriesName": "partial dependence", "seriesType": "line", "seriesData": partialDict[col]})
            
    #         hist = plt.hist(dataframe[col])
    #         bins = sorted(hist[1])
    #         if len(bins) > 20:
    #             hist = plt.hist(dataframe[col], bins=20)
    #             bins = sorted(hist[1])

    #         bins = list(map(lambda x: round(x, 4), bins))
            
    #         # Actual
    #         seriesData = []
    #         newDf = dataframe[[col, "y_test"]]
            
    #         for i in range(len(bins)-1):
    #           tmp1 = newDf[col] >= bins[i]
    #           tmp2 = newDf[col] < bins[i+1]
    #           meanYTest = newDf[tmp1 & tmp2].mean()["y_test"]
    #           if not np.isnan(meanYTest):
    #             seriesData.append([round(np.median([bins[i], bins[i+1]]),4), round(meanYTest, 4), bins[i], bins[i+1]])
              
    #         series.append({"seriesName": "Actual", "seriesType": "line", "seriesData": seriesData})
            
    #         # Predicted
    #         seriesData = []
    #         newDf = dataframe[[col, "y_pred"]]

    #         for i in range(len(bins)-1):
    #           tmp1 = newDf[col] >= bins[i]
    #           tmp2 = newDf[col] < bins[i+1]
    #           meanYPred = newDf[tmp1 & tmp2].mean()["y_pred"]
    #           if not np.isnan(meanYPred):
    #             seriesData.append([round(np.median([bins[i], bins[i+1]]),4), round(meanYPred, 4), bins[i], bins[i+1]])
    #         series.append({"seriesName": "Predict", "seriesType": "line", "seriesData": seriesData})
            
    #         # histogram
    #         seriesData = []    
    #         for i in range(len(bins)-1): 
    #           seriesData.append([round(np.median([bins[i], bins[i+1]]),4), hist[0][i], bins[i], bins[i+1]])
    #         series.append({"seriesName": "histogram", "seriesType": "bar", "seriesData": seriesData})
            
    #         chartList.append({"chartName": col, "xMin": float(dataframe[col].min()), "xMax": float(dataframe[col].max()), "binsCount": len(bins)-1, "binsRange": round(bins[1]-bins[0], 4), "legendX" : col, "legendY": f"Target ({target})", "series":series})
          
          
    #   output = {
    #       "chartTitle": "Feature Effect",
    #       "chartType" : "Feature Effect",
    #       "chartList": chartList
    #     }
    #   return output
  
    def clfFeatureEffect(self, xTest, yTest, yPred, columnNms, labelColumnNms, target, columnTypeDict, log): # purposeType이 classification인 경우 ㅜㅜ
          chartList = []
          dataframe = pd.DataFrame(xTest, columns=columnNms)
          
          dataframe["y_test"] = yTest
          dataframe["y_pred"] = yPred
          
          for col in dataframe.columns:
            series = []
            if col not in ["y_test", "y_pred"]:
              if columnTypeDict[col] == "object":
                continue
              
              elif columnTypeDict[col] in ["Numeric", "int64", "float64"]: # 정수일 때
                
                # Actual
                newDf = dataframe[[col, "y_test"]]
                groupbyDf = newDf.groupby("y_test").agg({col: "mean"})
                groupbyList = groupbyDf[col].values.tolist()
                  
                series.append({"seriesName": "Actual", "seriesType": "bar", "seriesData": groupbyList})
                
                # Predicted
                newDf = dataframe[[col, "y_pred"]]
                groupbyDf = newDf.groupby("y_pred").agg({col: "mean"})
                groupbyList = groupbyDf[col].values.tolist()

                series.append({"seriesName": "Predict", "seriesType": "bar", "seriesData": groupbyList})
                chartList.append({"chartName": col, "chartType" : "Feature Effect", "legendX" : f"Target ({target})", "legendY": col, "seriesCategory": labelColumnNms, "series":series})
              
              
          output = {
              "chartTitle": "Feature Effect",
              "chartType" : "Feature Effect",
              "chartList": chartList
            }
          
          return output
