#수행평가 class를 구현하자
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
        #난이도는 1~5, 수행평가를 하는데 걸리는 시간(단위:일)과 같음
        if X in ['1', '2', '3', '4', '5']: 
            self.X = X
            
#Stack과 Stack에 이용되는 함수들 정의            
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
    
#달력에 수행평가를 입력하는 코드 
from pandas import Series
import numpy as np
import pandas as pd
import calendar #python에서 달력을 불러오는 코드 
from IPython.display import display
k = [] #리스트 생성
#'수행평가를 입력하세요'에 X를 누를 때까지 계속 과제를 입력할 수 있음 
for i in range(0, 10000):
    Q = input('수행평가를 입력하세요: O or X : ')
    if Q == 'O':
        k.append(assignment()) #리스트에 입력한 과제 추가
    if Q == 'X':
        break
U = Stack()

#달력을 만들어보자
def calen(n, items):
    z = 0
    #monthrange: 그 연도(2019년)와 입력한 달(n월)에 대해 그 달의 1일이 무슨 요일인지, 며칠까지 있는지를 불러옴 
    A = calendar.monthrange(2019,n)
    X = ['']*35 #하나의 달에 최대 5주까지 있으므로 35개 
    Y = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7] #X에 대응하는 표의 칸(5행 7열)
    D = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7] #Y 아래에 과제가 입력될 칸
    for i in range (0, A[1]): #n월의 1일부터 마지막 일
        X[i+A[0]] = i+1
    for i in range (0, 5): #행(5주)
        for j in range(0, 7): #열(일주일;7일)
            Y[i][j] = X[7*i+j] #X를 Y에 들어갈 표 칸의 형태로 바꾸어줌 
    for a in range(0, len(items)): #입력한 과제들
         for i in range (0,5):
            for j in range (0, 7):
                if Y[i][j] == items[a].day: #날짜와 과제의 기한이 일치하면 과제의 이름을 날짜 아래 입력하는 코드 
                    for k in range(0, int(items[a].X)):
                        D[i][j-k] = D[i][j-k]+items[a].name
    
    cal = np.array([Y[0], D[0], Y[1], D[1], Y[2], D[2], Y[3], D[3], Y[4], D[4]])
    pd.DataFrame(cal)
    display(pd.DataFrame(data = cal, columns = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'], index = ['', '', '', '', '', '', '', '', '', '']))
    
calen(4, k) #단점: 4월이면 4 처럼 코드를 그 달마다 매번 수정해야 함
