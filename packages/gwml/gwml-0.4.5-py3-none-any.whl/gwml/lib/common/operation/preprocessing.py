import pandas as pd
import numpy as np


class preprocessing():
    def __init__(self, data):
        self.data = data

    def sumColumnData(self, column1, column2):
        sumColumn = self.data[[column1, column2]].sum()
        return sumColumn

    def run(self):
        # self.resize(100, 100)
        # self.flip('h')
        # self.sumColumnData("column1", "column2")
        return self.data
