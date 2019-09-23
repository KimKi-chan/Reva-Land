class assignment:
    def __init__(self):
        name = input("수행평가의 이름: ")
        teacher = input("수행평가 담당 선생님: ")
        month, day = input("제출 기한: ").split("/")
        X = input("난이도: ") # 밑의 코드는 난이도를 1~5 로 나타낸 코드이다.
        self.teacher = teacher
        self.name = name
        self.month = month
        self.day = int(day)
        if X in ['1', '2', '3', '4', '5']:
            self.X = X
            
class Stack:
    def __init__(self, k = []) : #초기화
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
    
from pandas import Series # pandas 에서 Seies를 불러온다.
import numpy as np # numpy는 엑셀 형식으로 이루어진 데이터를 효과적으로 이용할 수 있게 만든 것이다.
import pandas as pd # pandas를 pd로 부른다.
import calendar #캘린더라는 저장 함수를 불러온다.
from IPython.display import display 
k = []
for i in range(0, 10000): #범위 설정
    Q = input('수행평가를 입력하세요: O or X : ') # input
    if Q == 'O':
        k.append(assignment())
    if Q == 'X':
        break
U = Stack() #수행 평가를 입력하는 코드이다.

def calen(n, items): 
    z = 0
    A = calendar.monthrange(2019,n)
    X = ['']*35
    Y = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7]
    D = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7]
    for i in range (0, A[1]):
        X[i+A[0]] = i+1 # 1씩 더한다.
    for i in range (0, 5):
        for j in range(0, 7):
            Y[i][j] = X[7*i+j] #날짜의 행과 열 설정 결과물은 표의 형태로 나온다.
    for a in range(0, len(items)):
         for i in range (0,5): #열
            for j in range (0, 7): #행
                if Y[i][j] == items[a].day:
                    for k in range(0, int(items[a].X)):
                        D[i][j-k] = D[i][j-k]+items[a].name
    
    cal = np.array([Y[0], D[0], Y[1], D[1], Y[2], D[2], Y[3], D[3], Y[4], D[4]])
    pd.DataFrame(cal)
    display(pd.DataFrame(data = cal, columns = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'], index = ['', '', '', '', '', '', '', '', '', '']))
    # 월부터 일까지룰  맨 윗 행을 나타내었다. 
calen(4, k) # 코드 사용자가 직접 설정해야 한다.
