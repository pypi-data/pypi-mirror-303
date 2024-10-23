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


import os
import sys
import logging
import logging.handlers
from pytz import timezone
from datetime import datetime

class Logger():
    def __new__(self, logPath, logLevel=None):
        self.logPath = logPath
              
        os.makedirs(os.path.abspath(os.path.join(self.logPath, "../")), exist_ok=True)
        
        self.logLevel = logLevel if logLevel is not None else "info"
        self.logger = logging.getLogger(logPath)
        self.logger.setLevel(logging.INFO) if self.logLevel == "info" else self.logger.setLevel(logging.DEBUG)

        if len(self.logger.handlers) > 0:
            # Logger already exists
            return self.logger

        self.fileHandler = logging.FileHandler(self.logPath, mode="a")
        self.logger.addHandler(self.fileHandler)
        
        KST = datetime.now(timezone('Asia/Seoul'))
        logging.Formatter.converter = lambda *args:(KST.now()).timetuple()

        self.formatter = logging.Formatter('[%(asctime)s] [%(levelname)5s] [%(filename)20s] : %(message)s', "%Y-%m-%d %H:%M:%S")
        self.fileHandler.setFormatter(self.formatter)

        return self.logger