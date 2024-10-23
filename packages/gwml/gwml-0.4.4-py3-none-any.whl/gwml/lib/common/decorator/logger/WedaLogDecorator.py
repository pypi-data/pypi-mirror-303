 # -*- coding:utf-8 -*-
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


from time import time

class WedaLogDecorator():
    def __init__(self, text, logLevel):
        self.text = str(text)
        self.logLevel = logLevel
        self.funcOutput = None
    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            startTime = time()
            log = kwargs["log"]

            if self.logLevel == "info":
                log.info(self.text)
                self.funcOutput = func(*args, **kwargs)
                finishTime = time()
                totalTime = float(finishTime - startTime)
                log.info("Finish {} - Elapsed time : {:.4f}sec".format(self.text, totalTime))

            elif self.logLevel == "debug":
                log.debug(self.text)
                self.funcOutput = func(*args, **kwargs)
                finishTime = time()
                totalTime = float(finishTime - startTime)
                log.debug("Finish {} - Elapsed time : {:.4f}sec".format(self.text, totalTime))

            elif self.logLevel == "error":
                log.error(self.text)
                self.funcOutput = func(*args, **kwargs)
                finishTime = time()
                totalTime = float(finishTime - startTime)
                log.error("Finish {} - Elapsed time : {:.4f}sec".format(self.text, totalTime))

            return self.funcOutput
        return wrapper