# controllers.py
from flask import jsonify, request
# from db import Database # no need of db
import pandas as pd
from config import USERNAME

#-------------- main class ------------

class backendModel:
    def __init__(self):
        self.le = 0

    # add logical functions here     
     
    def say_hi(self):
        # data = read_csv_file("data/x.csv")
        msg = "hi " + USERNAME
        return msg

    
    def say_hi_to(self, name):
        msg = "hi " + name + " how are you "
        return msg
    
    
obj = backendModel()