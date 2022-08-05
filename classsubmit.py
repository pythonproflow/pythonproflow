import pymongo
from pymongo import MongoClient
import numpy as np
import pandas as pd

#Don't change anything in this cell; Just run it.

user='pythonclass'
p1='qmHPwT#y'.replace('#','e')
n=301*2
p2=f'qQtRp{n}'
p0=p1+p2
course='Course-XYZ'

classclient = pymongo.MongoClient(f"mongodb+srv://{user}:{p0}@cluster0.hjfuv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
classDb = classclient.classDb


classDb[course].create_index([("name", pymongo.ASCENDING),("email", pymongo.ASCENDING)],unique=True)

def submitAnswer(id,qn,answer):
  try:
    classDb[course].delete_many({'email':id,'qn':qn})
  except:
    0
  classDb[course].insert_one({'email':id,'qn':qn,'answer':answer})
  print(f'Your answer for {qn} is: ')
  print(answer)
