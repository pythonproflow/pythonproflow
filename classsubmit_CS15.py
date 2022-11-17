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



def boxsu(board,mysymbol): 
  def boxsu_init(n):
    global boxsuXYZ
    width=n//6
    boxsuXYZ=[(3.0/max(abs(n/2-i-0.5)*abs(n/2-j-0.5),1),(i,j)) for i in range(n) for j in range(n) if i==width or j==width or i==n-1-width or j==n-1-width]
    boxsuXYZ=[c[1] for c in sorted(boxsuXYZ,reverse=True)]
    boxsuXYZ=[(i,j) for i in range(n) for j in range(n) if (i<width or i>n-1-width) and j==n//2] + [(j,i) for i in range(n) for j in range(n) if (i<width or i>n-1-width) and j==n//2] + boxsuXYZ

  global boxsuXYZ
  global boxsuXYZ_n

  n=len(board)
  try:
    if boxsuXYZ_n!=n:
      boxsu_init(n)
      boxsuXYZ_n=n
  except:
    boxsu_init(n)
    boxsuXYZ_n=n

  #Box first
  for i,j in boxsuXYZ:
    if board[i][j]=='_':
      return (i,j)

  possibles=[]
  for i in range(n):
    for j in range(n):
      if board[i][j]=='_':
        possibles.append((i,j))

  return random.choice(possibles)

def voldemort(board,mysymbol): 
  n=len(board)
  score=[[0]*n for j in range(n)]
  m0=-0.3
  m1=0.1
  hi=3.0

  if n>6:
    m0=-0.2
    m1=+0.1
    hi=3.0

  #8x8 or higher, use dumbledore
  if n>8:
    m0=+0.2 #inverted
    m1=+0.1
    hi=9.0


  for i in range(n):
    for j in range(n):
      score[i][j]=hi/max(abs(n/2-i-0.5)*abs(n/2-j-0.5),1)
      if board[i][j]!='_':
        score[i][j]=0
      else:

        for i2 in [i-2,0,i+2]:
          for j2 in [j-2,0,j+2]:
            if i2<0 or i2>=n or j2<0 or j2>=n:
              continue
            if board[i2][j2]=='x':
              score[i][j]+=m0

        for i2 in [i-1,0,i+1]:
          for j2 in [j-1,0,j+1]:
            if i2<0 or i2>=n or j2<0 or j2>=n:
              continue
            if board[i2][j2]!='x': #Want room to grow
              score[i][j]+=m1

        # if i>=2:
        #   if board[i-1][j]==board[i-2][j] and board[i-1][j]=='x':
        #     score[i][j]-=0.1
        # if i<=n-3:
        #   if board[i+1][j]==board[i+2][j] and board[i+1][j]=='x':
        #     score[i][j]-=0.1
        # if j>=2:
        #   if board[i][j-1]==board[i][j-2] and board[i][j-1]=='x':
        #     score[i][j]-=0.1
        # if j<=n-3:
        #   if board[i][j+1]==board[i][j+2] and board[i][j+1]=='x':
        #     score[i][j]-=0.1
        # if i>=2 and j>=2:
        #   if board[i-1][j-1]==board[i-2][j-2] and board[i-1][j-1]=='x':
        #     score[i][j]-=0.1
        # if i<=n-3 and j<=n-3:
        #   if board[i+1][j+1]==board[i+2][j+2] and board[i+1][j+1]=='x':
        #     score[i][j]-=0.1
        # if i>=2 and j<=n-3:
        #   if board[i-1][j+1]==board[i-2][j+2] and board[i-1][j+1]=='x':
        #     score[i][j]-=0.1
        # if i<=n-3 and j>=2:
        #   if board[i+1][j-1]==board[i+2][j-2] and board[i+1][j-1]=='x':
        #     score[i][j]-=0.1

        # if i>=3:
        #   if board[i-2][j]==board[i-3][j] and (board[i-1][j]=='_' or board[i-1][j]==board[i-2][j]) and board[i-2][j]=='x':
        #     score[i][j]-=0.1
        # if i<=n-4:
        #   if board[i+2][j]==board[i+3][j] and (board[i+1][j]=='_' or board[i+1][j]==board[i+2][j]) and board[i+2][j]=='x':
        #     score[i][j]-=0.1
        # if j>=3:
        #   if board[i][j-2]==board[i][j-3] and (board[i][j-1]=='_' or board[i][j-1]==board[i][j-2]) and board[i][j-2]=='x':
        #     score[i][j]-=0.1
        # if j<=n-4:
        #   if board[i][j+2]==board[i][j+3] and (board[i][j+1]=='_' or board[i][j+1]==board[i][j+2]) and board[i][j+2]=='x':
        #     score[i][j]-=0.1

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

def prof1(board,mysymbol): 

  def mybot_init(n):
    global mybot_h
    global mybot_v
    global mybot_s

    mybot_h=[[(i,j) for j in range(n)] for i in range(n)]
    mybot_v=[[(i,j) for i in range(n)] for j in range(n)]

    diagonal_slashs=[]
    for j in range(2*n-1):
      jth_slash=[]
      for i in range(n):
        if j-i<0:
          break
        if j-i>=n:
          continue
        jth_slash.append((i,j-i))
      if len(jth_slash)>n*0.4:
        diagonal_slashs.append(jth_slash)

    diagonal_backslashs=[]
    for j in range(2*n-1):
      jth_slash=[]
      for i2 in range(n):
        i=n-1-i2
        if j-i2<0:
          break
        if j-i2>=n:
          continue
        jth_slash.append((i,j-i2))
      if len(jth_slash)>n*0.4:
        diagonal_backslashs.append(jth_slash)

    mybot_s=diagonal_slashs+diagonal_backslashs
    
  global mybot_boardsize
  global mybot_focal_row
  global mybot_focal_col
  global mybot_row_block
  global mybot_col_block
  global mybot_slash_block
  global mybot_block_inertia
  global mybot_h
  global mybot_v
  global mybot_s

  n=len(board)
  try:
    if n!=mybot_boardsize:
      mybot_init(n)
      mybot_boardsize=n
  except:
    mybot_init(n)
    mybot_boardsize=n
  
  if random.random()>0.4:
    return randomBot1(board,mysymbol)
   
  mybot_focal_row,mybot_focal_col,mybot_row_block,mybot_col_block,mybot_slash_block,mybot_block_inertia=[1, 1, 1, 1, 1, 0.5]
  mybot_focal_row=max(min(mybot_focal_row,1.0),0.0)  
  mybot_focal_col=max(min(mybot_focal_col,1.0),0.0)  
  mybot_row_block=max(min(mybot_row_block,1.0),0.0)  
  mybot_col_block=max(min(mybot_col_block,1.0),0.0)  
  mybot_slash_block=max(min(mybot_slash_block,1.0),0.0)
  mybot_block_inertia=max(min(mybot_block_inertia,1.0),0.0)  

  score=[[0]*n for j in range(n)]
  for i in range(n):
    for j in range(n):
      depthi=1-abs(n/2-i)/(n/2) 
      depthj=1-abs(n/2-j)/(n/2) 
      errori=abs(mybot_focal_row-depthi)+1
      errorj=abs(mybot_focal_col-depthj)+1
      score[i][j]=3.0/(errori*errorj)

  # make line copy
  #for sym in x, o
  # fill forward m, fill backwards m, count consecutive
  # add score by consecutive count times center of the range  times center of the line

  fillsides=1
  for block,dir in [(mybot_row_block,mybot_h),
              (mybot_col_block,mybot_v),
              (mybot_slash_block,mybot_s),
              ]:
    for line in dir:
      cumscore=0
      bonus=0

      lst=[]
      for idx,(i,j) in enumerate(line):
        lst.append(board[i][j])
      lstx=lst.copy()
      lsty=lst.copy()

      lastx=0
      lasty=0
      for idx in range(len(lst)):
        c=lst[idx]
        if lastx>0 and c=='_':
          lstx[idx]='x'
          lastx-=1
        if lasty>0 and c=='_':
          lsty[idx]='o'
          lasty-=1
        if c=='x':  
          lastx=fillsides
          lasty=0
        elif c=='o':
          lasty=fillsides
          lastx=0

      lastx=0
      lasty=0
      for idx in range(len(lst)-1,-1,-1):
        c=lst[idx]
        if lastx>0 and c=='_':
          lstx[idx]='x'
          lastx-=1
        if lasty>0 and c=='_':
          lsty[idx]='o'
          lasty-=1
        if c=='x':  
          lastx=fillsides
          lasty=0
        elif c=='o':
          lasty=fillsides
          lastx=0

      idx=0
      while idx<len(lst):
        if lstx[idx]=='x':
          count=0
          start=idx
          while idx<len(lst) and lstx[idx]=='x':
            count+=1
            idx+=1
          for idx2 in range(start,idx):
            lstx[idx2]=count
        else:
          lstx[idx]=0
          idx+=1

      idx=0
      while idx<len(lst):
        if lsty[idx]=='o':
          count=0
          start=idx
          while idx<len(lst) and lsty[idx]=='o':
            count+=1
            idx+=1
          for idx2 in range(start,idx):
            lsty[idx2]=count
        else:
          lsty[idx]=0
          idx+=1
          
      # print(lst)
      # print(lstx)
      # print(lsty)
      # print()
      m=len(line)/2
      for idx,(i,j) in enumerate(line):
        if lstx[idx]>mybot_block_inertia*n:
          score[i][j]+=lstx[idx]*0.9**(abs(idx-m))*block
        if lsty[idx]>mybot_block_inertia*n:
          score[i][j]+=lsty[idx]*0.9**(abs(idx-m))*block

  for i in range(n):
    for j in range(n):
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


def prof2(board,mysymbol): 

  def mybot_init(n):
    global mybot_h
    global mybot_v
    global mybot_s

    mybot_h=[[(i,j) for j in range(n)] for i in range(n)]
    mybot_v=[[(i,j) for i in range(n)] for j in range(n)]

    diagonal_slashs=[]
    for j in range(2*n-1):
      jth_slash=[]
      for i in range(n):
        if j-i<0:
          break
        if j-i>=n:
          continue
        jth_slash.append((i,j-i))
      if len(jth_slash)>n*0.4:
        diagonal_slashs.append(jth_slash)

    diagonal_backslashs=[]
    for j in range(2*n-1):
      jth_slash=[]
      for i2 in range(n):
        i=n-1-i2
        if j-i2<0:
          break
        if j-i2>=n:
          continue
        jth_slash.append((i,j-i2))
      if len(jth_slash)>n*0.4:
        diagonal_backslashs.append(jth_slash)

    mybot_s=diagonal_slashs+diagonal_backslashs
    
  global mybot_boardsize
  global mybot_focal_row
  global mybot_focal_col
  global mybot_row_block
  global mybot_col_block
  global mybot_slash_block
  global mybot_block_inertia
  global mybot_h
  global mybot_v
  global mybot_s

  n=len(board)
  try:
    if n!=mybot_boardsize:
      mybot_init(n)
      mybot_boardsize=n
  except:
    mybot_init(n)
    mybot_boardsize=n
  
  if random.random()>0.6:
    return randomBot1(board,mysymbol)
   
  mybot_focal_row,mybot_focal_col,mybot_row_block,mybot_col_block,mybot_slash_block,mybot_block_inertia=[1, 1, 1, 1, 1, 0.5]
  mybot_focal_row=max(min(mybot_focal_row,1.0),0.0)  
  mybot_focal_col=max(min(mybot_focal_col,1.0),0.0)  
  mybot_row_block=max(min(mybot_row_block,1.0),0.0)  
  mybot_col_block=max(min(mybot_col_block,1.0),0.0)  
  mybot_slash_block=max(min(mybot_slash_block,1.0),0.0)
  mybot_block_inertia=max(min(mybot_block_inertia,1.0),0.0)  

  score=[[0]*n for j in range(n)]
  for i in range(n):
    for j in range(n):
      depthi=1-abs(n/2-i)/(n/2) 
      depthj=1-abs(n/2-j)/(n/2) 
      errori=abs(mybot_focal_row-depthi)+1
      errorj=abs(mybot_focal_col-depthj)+1
      score[i][j]=3.0/(errori*errorj)

  # make line copy
  #for sym in x, o
  # fill forward m, fill backwards m, count consecutive
  # add score by consecutive count times center of the range  times center of the line

  fillsides=1
  for block,dir in [(mybot_row_block,mybot_h),
              (mybot_col_block,mybot_v),
              (mybot_slash_block,mybot_s),
              ]:
    for line in dir:
      cumscore=0
      bonus=0

      lst=[]
      for idx,(i,j) in enumerate(line):
        lst.append(board[i][j])
      lstx=lst.copy()
      lsty=lst.copy()

      lastx=0
      lasty=0
      for idx in range(len(lst)):
        c=lst[idx]
        if lastx>0 and c=='_':
          lstx[idx]='x'
          lastx-=1
        if lasty>0 and c=='_':
          lsty[idx]='o'
          lasty-=1
        if c=='x':  
          lastx=fillsides
          lasty=0
        elif c=='o':
          lasty=fillsides
          lastx=0

      lastx=0
      lasty=0
      for idx in range(len(lst)-1,-1,-1):
        c=lst[idx]
        if lastx>0 and c=='_':
          lstx[idx]='x'
          lastx-=1
        if lasty>0 and c=='_':
          lsty[idx]='o'
          lasty-=1
        if c=='x':  
          lastx=fillsides
          lasty=0
        elif c=='o':
          lasty=fillsides
          lastx=0

      idx=0
      while idx<len(lst):
        if lstx[idx]=='x':
          count=0
          start=idx
          while idx<len(lst) and lstx[idx]=='x':
            count+=1
            idx+=1
          for idx2 in range(start,idx):
            lstx[idx2]=count
        else:
          lstx[idx]=0
          idx+=1

      idx=0
      while idx<len(lst):
        if lsty[idx]=='o':
          count=0
          start=idx
          while idx<len(lst) and lsty[idx]=='o':
            count+=1
            idx+=1
          for idx2 in range(start,idx):
            lsty[idx2]=count
        else:
          lsty[idx]=0
          idx+=1
          
      # print(lst)
      # print(lstx)
      # print(lsty)
      # print()
      m=len(line)/2
      for idx,(i,j) in enumerate(line):
        if lstx[idx]>mybot_block_inertia*n:
          score[i][j]+=lstx[idx]*0.9**(abs(idx-m))*block
        if lsty[idx]>mybot_block_inertia*n:
          score[i][j]+=lsty[idx]*0.9**(abs(idx-m))*block

  for i in range(n):
    for j in range(n):
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

def prof3(board,mysymbol): 

  def mybot_init(n):
    global mybot_h
    global mybot_v
    global mybot_s

    mybot_h=[[(i,j) for j in range(n)] for i in range(n)]
    mybot_v=[[(i,j) for i in range(n)] for j in range(n)]

    diagonal_slashs=[]
    for j in range(2*n-1):
      jth_slash=[]
      for i in range(n):
        if j-i<0:
          break
        if j-i>=n:
          continue
        jth_slash.append((i,j-i))
      if len(jth_slash)>n*0.4:
        diagonal_slashs.append(jth_slash)

    diagonal_backslashs=[]
    for j in range(2*n-1):
      jth_slash=[]
      for i2 in range(n):
        i=n-1-i2
        if j-i2<0:
          break
        if j-i2>=n:
          continue
        jth_slash.append((i,j-i2))
      if len(jth_slash)>n*0.4:
        diagonal_backslashs.append(jth_slash)

    mybot_s=diagonal_slashs+diagonal_backslashs
    
  global mybot_boardsize
  global mybot_focal_row
  global mybot_focal_col
  global mybot_row_block
  global mybot_col_block
  global mybot_slash_block
  global mybot_block_inertia
  global mybot_h
  global mybot_v
  global mybot_s

  n=len(board)
  try:
    if n!=mybot_boardsize:
      mybot_init(n)
      mybot_boardsize=n
  except:
    mybot_init(n)
    mybot_boardsize=n
  
  if random.random()>0.8:
    return randomBot1(board,mysymbol)
   
  mybot_focal_row,mybot_focal_col,mybot_row_block,mybot_col_block,mybot_slash_block,mybot_block_inertia=[1, 1, 1, 1, 1, 0.5]
  mybot_focal_row=max(min(mybot_focal_row,1.0),0.0)  
  mybot_focal_col=max(min(mybot_focal_col,1.0),0.0)  
  mybot_row_block=max(min(mybot_row_block,1.0),0.0)  
  mybot_col_block=max(min(mybot_col_block,1.0),0.0)  
  mybot_slash_block=max(min(mybot_slash_block,1.0),0.0)
  mybot_block_inertia=max(min(mybot_block_inertia,1.0),0.0)  

  score=[[0]*n for j in range(n)]
  for i in range(n):
    for j in range(n):
      depthi=1-abs(n/2-i)/(n/2) 
      depthj=1-abs(n/2-j)/(n/2) 
      errori=abs(mybot_focal_row-depthi)+1
      errorj=abs(mybot_focal_col-depthj)+1
      score[i][j]=3.0/(errori*errorj)

  # make line copy
  #for sym in x, o
  # fill forward m, fill backwards m, count consecutive
  # add score by consecutive count times center of the range  times center of the line

  fillsides=1
  for block,dir in [(mybot_row_block,mybot_h),
              (mybot_col_block,mybot_v),
              (mybot_slash_block,mybot_s),
              ]:
    for line in dir:
      cumscore=0
      bonus=0

      lst=[]
      for idx,(i,j) in enumerate(line):
        lst.append(board[i][j])
      lstx=lst.copy()
      lsty=lst.copy()

      lastx=0
      lasty=0
      for idx in range(len(lst)):
        c=lst[idx]
        if lastx>0 and c=='_':
          lstx[idx]='x'
          lastx-=1
        if lasty>0 and c=='_':
          lsty[idx]='o'
          lasty-=1
        if c=='x':  
          lastx=fillsides
          lasty=0
        elif c=='o':
          lasty=fillsides
          lastx=0

      lastx=0
      lasty=0
      for idx in range(len(lst)-1,-1,-1):
        c=lst[idx]
        if lastx>0 and c=='_':
          lstx[idx]='x'
          lastx-=1
        if lasty>0 and c=='_':
          lsty[idx]='o'
          lasty-=1
        if c=='x':  
          lastx=fillsides
          lasty=0
        elif c=='o':
          lasty=fillsides
          lastx=0

      idx=0
      while idx<len(lst):
        if lstx[idx]=='x':
          count=0
          start=idx
          while idx<len(lst) and lstx[idx]=='x':
            count+=1
            idx+=1
          for idx2 in range(start,idx):
            lstx[idx2]=count
        else:
          lstx[idx]=0
          idx+=1

      idx=0
      while idx<len(lst):
        if lsty[idx]=='o':
          count=0
          start=idx
          while idx<len(lst) and lsty[idx]=='o':
            count+=1
            idx+=1
          for idx2 in range(start,idx):
            lsty[idx2]=count
        else:
          lsty[idx]=0
          idx+=1
          
      # print(lst)
      # print(lstx)
      # print(lsty)
      # print()
      m=len(line)/2
      for idx,(i,j) in enumerate(line):
        if lstx[idx]>mybot_block_inertia*n:
          score[i][j]+=lstx[idx]*0.9**(abs(idx-m))*block
        if lsty[idx]>mybot_block_inertia*n:
          score[i][j]+=lsty[idx]*0.9**(abs(idx-m))*block

  for i in range(n):
    for j in range(n):
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

def prof4(board,mysymbol): 

  def mybot_init(n):
    global mybot_h
    global mybot_v
    global mybot_s

    mybot_h=[[(i,j) for j in range(n)] for i in range(n)]
    mybot_v=[[(i,j) for i in range(n)] for j in range(n)]

    diagonal_slashs=[]
    for j in range(2*n-1):
      jth_slash=[]
      for i in range(n):
        if j-i<0:
          break
        if j-i>=n:
          continue
        jth_slash.append((i,j-i))
      if len(jth_slash)>n*0.4:
        diagonal_slashs.append(jth_slash)

    diagonal_backslashs=[]
    for j in range(2*n-1):
      jth_slash=[]
      for i2 in range(n):
        i=n-1-i2
        if j-i2<0:
          break
        if j-i2>=n:
          continue
        jth_slash.append((i,j-i2))
      if len(jth_slash)>n*0.4:
        diagonal_backslashs.append(jth_slash)

    mybot_s=diagonal_slashs+diagonal_backslashs
    
  global mybot_boardsize
  global mybot_focal_row
  global mybot_focal_col
  global mybot_row_block
  global mybot_col_block
  global mybot_slash_block
  global mybot_block_inertia
  global mybot_h
  global mybot_v
  global mybot_s

  n=len(board)
  try:
    if n!=mybot_boardsize:
      mybot_init(n)
      mybot_boardsize=n
  except:
    mybot_init(n)
    mybot_boardsize=n
  
  
  mybot_focal_row,mybot_focal_col,mybot_row_block,mybot_col_block,mybot_slash_block,mybot_block_inertia=[1, 1, 1, 1, 1, 0.5]
  mybot_focal_row=max(min(mybot_focal_row,1.0),0.0)  
  mybot_focal_col=max(min(mybot_focal_col,1.0),0.0)  
  mybot_row_block=max(min(mybot_row_block,1.0),0.0)  
  mybot_col_block=max(min(mybot_col_block,1.0),0.0)  
  mybot_slash_block=max(min(mybot_slash_block,1.0),0.0)
  mybot_block_inertia=max(min(mybot_block_inertia,1.0),0.0)  

  score=[[0]*n for j in range(n)]
  for i in range(n):
    for j in range(n):
      depthi=1-abs(n/2-i)/(n/2) 
      depthj=1-abs(n/2-j)/(n/2) 
      errori=abs(mybot_focal_row-depthi)+1
      errorj=abs(mybot_focal_col-depthj)+1
      score[i][j]=3.0/(errori*errorj)

  # make line copy
  #for sym in x, o
  # fill forward m, fill backwards m, count consecutive
  # add score by consecutive count times center of the range  times center of the line

  fillsides=1
  for block,dir in [(mybot_row_block,mybot_h),
              (mybot_col_block,mybot_v),
              (mybot_slash_block,mybot_s),
              ]:
    for line in dir:
      cumscore=0
      bonus=0

      lst=[]
      for idx,(i,j) in enumerate(line):
        lst.append(board[i][j])
      lstx=lst.copy()
      lsty=lst.copy()

      lastx=0
      lasty=0
      for idx in range(len(lst)):
        c=lst[idx]
        if lastx>0 and c=='_':
          lstx[idx]='x'
          lastx-=1
        if lasty>0 and c=='_':
          lsty[idx]='o'
          lasty-=1
        if c=='x':  
          lastx=fillsides
          lasty=0
        elif c=='o':
          lasty=fillsides
          lastx=0

      lastx=0
      lasty=0
      for idx in range(len(lst)-1,-1,-1):
        c=lst[idx]
        if lastx>0 and c=='_':
          lstx[idx]='x'
          lastx-=1
        if lasty>0 and c=='_':
          lsty[idx]='o'
          lasty-=1
        if c=='x':  
          lastx=fillsides
          lasty=0
        elif c=='o':
          lasty=fillsides
          lastx=0

      idx=0
      while idx<len(lst):
        if lstx[idx]=='x':
          count=0
          start=idx
          while idx<len(lst) and lstx[idx]=='x':
            count+=1
            idx+=1
          for idx2 in range(start,idx):
            lstx[idx2]=count
        else:
          lstx[idx]=0
          idx+=1

      idx=0
      while idx<len(lst):
        if lsty[idx]=='o':
          count=0
          start=idx
          while idx<len(lst) and lsty[idx]=='o':
            count+=1
            idx+=1
          for idx2 in range(start,idx):
            lsty[idx2]=count
        else:
          lsty[idx]=0
          idx+=1
          
      # print(lst)
      # print(lstx)
      # print(lsty)
      # print()
      m=len(line)/2
      for idx,(i,j) in enumerate(line):
        if lstx[idx]>mybot_block_inertia*n:
          score[i][j]+=lstx[idx]*0.9**(abs(idx-m))*block
        if lsty[idx]>mybot_block_inertia*n:
          score[i][j]+=lsty[idx]*0.9**(abs(idx-m))*block

  for i in range(n):
    for j in range(n):
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

