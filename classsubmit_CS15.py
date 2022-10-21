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
course='Course-CS15'
password1='discover'
password2='world'
password3='tropical'
password4='fantasy'
password5='document'

import time


classclient = pymongo.MongoClient(f"mongodb+srv://{user}:{p0}@cluster0.hjfuv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
classDb = classclient.classDb


classDb[course].create_index([("name", pymongo.ASCENDING),("email", pymongo.ASCENDING),('qn', pymongo.ASCENDING)],unique=True)

def submitAnswer(id,qn,answer):
  try:
    classDb[course].delete_many({'email':id,'qn':qn})
  except:
    0
  classDb[course].insert_one({'email':id,'qn':qn,'answer':answer})
  print(f'Your answer for {qn} is: ')
  print(answer)


def reviewAnswers(id,module):
  return pd.DataFrame(classDb[course].find({'email':id,'qn':{'$regex':f'^{module}'}}))


# Using this check_password, you should be able
# to crack the full password.
def check_password(user, guess):
    actual = password1
    if len(guess) != len(actual):
        return False

    for i in range(len(actual)):
        if guess[i] != actual[i]:
            return False
        time.sleep(0.00001)
    return True
 
import random

def randomBot1(board,mysymbol):
  n=len(board)
  open=[]
  for i in range(n):
    for j in range(n):
      if board[i][j]=='_':
        open.append((i,j))
  return random.choice(open)


def firstBot1(board,mysymbol):
  n=len(board)
  for i in range(n):
    for j in range(n):
      if board[i][j]=='_':
        return (i,j)
  return randomBot1(board,mysymbol)


def lastBot1(board,mysymbol):
  n=len(board)
  for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
      if board[i][j]=='_':
        return (i,j)
  return randomBot1(board,mysymbol)

def diagBot1(board,mysymbol):
  n=len(board)
  d1=[(i,i) for i in range(n)]
  d2=[(i,n-i-1) for i in range(n)]

  #Diagonals first
  for i,j in d1+d2:
    if board[i][j]=='_':
      return (i,j)

  #Then pick first
  for i in range(n):
    for j in range(n):
      if board[i][j]=='_':
        return (i,j)
  return randomBot1(board,mysymbol)

def profX(board,mysymbol): 
  n=len(board)
  d1=[(i,i) for i in range(n)]
  d1=d1[n//2:]+d1[:n//2]
  d2=[(i,n-i-1) for i in range(n)]
  d2=d2[n//2:]+d2[:n//2]

  #Diagonals first from middle
  for i,j in d1+d2:
    if board[i][j]=='_':
      return (i,j)
  #Then middle row
  for i in [n//2]:
    for j in range(n):
      if board[i][j]=='_':
        return (i,j)

  #Then middle col
  for i in range(n):
    for j in [n//2]:
      if board[i][j]=='_':
        return (i,j)

  #Then pick random
  return randomBot1(board,mysymbol)

def dumbledore(board,mysymbol): 
  n=len(board)
  score=[[0]*n for j in range(n)]
  for i in range(n):
    for j in range(n):
      score[i][j]=3.0/max(abs(n/2-i-0.5)*abs(n/2-j-0.5),1)
      if board[i][j]!='_':
        score[i][j]=0
      else:
        if i>=2:
          if board[i-1][j]==board[i-2][j] and board[i-1][j]!='_':
            score[i][j]+=0.1
        if i<=n-3:
          if board[i+1][j]==board[i+2][j] and board[i+1][j]!='_':
            score[i][j]+=0.1
        if j>=2:
          if board[i][j-1]==board[i][j-2] and board[i][j-1]!='_':
            score[i][j]+=0.1
        if j<=n-3:
          if board[i][j+1]==board[i][j+2] and board[i][j+1]!='_':
            score[i][j]+=0.1
        if i>=2 and j>=2:
          if board[i-1][j-1]==board[i-2][j-2] and board[i-1][j-1]!='_':
            score[i][j]+=0.1
        if i<=n-3 and j<=n-3:
          if board[i+1][j+1]==board[i+2][j+2] and board[i+1][j+1]!='_':
            score[i][j]+=0.1
        if i>=2 and j<=n-3:
          if board[i-1][j+1]==board[i-2][j+2] and board[i-1][j+1]!='_':
            score[i][j]+=0.1
        if i<=n-3 and j>=2:
          if board[i+1][j-1]==board[i+2][j-2] and board[i+1][j-1]!='_':
            score[i][j]+=0.1


  maxscore=0
  for i in range(n):
    for j in range(n):
      if score[i][j]>maxscore:
        maxscore=score[i][j]

  choices=[]
  for i in range(n):
    for j in range(n):
      if score[i][j]==maxscore:
        choices.append((i,j))

  return random.choice(choices)

def phoenix(board,mysymbol): 
  n=len(board)
  score=[[0]*n for j in range(n)]
  for i in range(n):
    for j in range(n):
      score[i][j]=3.0/max(abs(n/2-i-0.5)*abs(n/2-j-0.5),1)
      if board[i][j]!='_':
        score[i][j]=0

  maxscore=0
  for i in range(n):
    for j in range(n):
      if score[i][j]>maxscore:
        maxscore=score[i][j]

  choices=[]
  for i in range(n):
    for j in range(n):
      if score[i][j]==maxscore:
        choices.append((i,j))

  return random.choice(choices)

