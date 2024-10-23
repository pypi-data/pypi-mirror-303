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
import json
import requests
import traceback


rootPath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir), os.path.pardir))
basePath = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__))))
sys.path.append(basePath)
sys.path.append(rootPath)
sys.path.append(os.path.join(rootPath, "sender"))


class WedaErrorDecorator(Exception):
    def __init__(self, func):
        self.output = {
          "status": 200,
          "message": "",
          "result": ""
        }
        self.func = func
        self.error = self.initErrorMsg()
        self.funcOutput = None

    def initErrorMsg(self):
        errorJson = None
        errorJsonPath = os.path.join(basePath, "wedaError.json")

        if os.path.isfile(errorJsonPath):
            with open(errorJsonPath, "r") as jsonFile:
                errorJson = json.load(jsonFile)
                errorJson = errorJson["error"]

        return errorJson

    def __call__(self, *args, **kwargs):
        try:
            self.funcOutput = self.func(*args, **kwargs)

        except Exception as e:
            print(traceback.format_exc())
            errKey = str(type(e).__name__)
            errDict = self.error[errKey]

            self.funcOutput["status"] = errDict["status"]
            self.funcOutput["message"] = "[{}/{}] : {}".format(errDict["errNo"], str(errKey), errDict["errMsg"])
            self.funcOutput["result"] = {
                "detail": str(e),
                "trace": str(traceback.format_exc())
            }

        finally:
            return self.funcOutput