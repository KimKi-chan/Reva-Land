class assignment:
    def __init__(self):
        name = input("수행평가의 이름: ")
        teacher = input("수행평가 담당 선생님: ")
        month, day = input("제출 기한: ").split("/")
        X = input("난이도: ")
        self.name = name
        self.teacher = teacher
        self.month = month
        self.day = int(day)
        if X in ['1', '2', '3', '4', '5']:
            self.X = X
            
class Stack:
    def __init__(self, k = []) :
        self.items = k
    def isEmpt(self) :
        return self.items == []
    def push(self, item) :
        self.items.append(item)
    def pop(self) :
        return self.items.pop()
    def peek(self) :
        return self.items[-1]
    def size(self) :
        return len(self.items)
    
from pandas import Series
import numpy as np
import pandas as pd
import calendar
from IPython.display import display
k = []
for i in range(0, 10000):
    Q = input('수행평가를 입력하세요: O or X : ')
    if Q == 'O':
        k.append(assignment())
    if Q == 'X':
        break
U = Stack()

def calen(n, items):
    print('')
    print( n ,'월 시간표')
    z = 0
    A = calendar.monthrange(2019,n)
    X = ['']*35
    Y = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7]
    D = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7]
    for i in range (0, A[1]):
        X[i+A[0]] = i+1
    for i in range (0, 5):
        for j in range(0, 7):
            Y[i][j] = X[7*i+j]
    for a in range(0, len(items)):
         for i in range (0,5):
            for j in range (0, 7):
                if Y[i][j] == items[a].day:
                    for k in range(0, int(items[a].X)):
                        D[i][j-k] = D[i][j-k]+items[a].name
    
    cal = np.array([Y[0], D[0], Y[1], D[1], Y[2], D[2], Y[3], D[3], Y[4], D[4]])
    pd.DataFrame(cal)
    display(pd.DataFrame(data = cal, columns = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'], index = ['', '', '', '', '', '', '', '', '', '']))
    
calen(4, k)
