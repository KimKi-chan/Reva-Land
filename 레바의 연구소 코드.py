class assignment:
    def __init__(self):
        name = input("수행평가의 이름: ") #코드 사용자가 수행평가 이름 입력
        teacher = input("수행평가 담당 선생님: ") #코드 사용자가 담당 선생님 이름 입력
        month, day = input("제출 기한: ").split("/") #코드 사용자가 제출기한 입력
        X = input("난이도: ") #코드 사용자가 난이도 입력
        self.name = name 
        self.teacher = teacher
        self.month = month
        self.day = int(day)
        if X in ['1', '2', '3', '4', '5']: #몇일전부터 수행평가를 시작할지를 정해줌
            self.X = X
            
class Stack: #코드에 쓰이는 클래스 구현
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
    
from pandas import Series #달력에 수행평가 표현하기 
import numpy as np
import pandas as pd
import calendar
from IPython.display import display
k = []
for i in range(0, 10000):
    Q = input('수행평가를 입력하세요: O or X : ') #수행평가 입력 여부 확인
    if Q == 'O': #수행평가 입력
        k.append(assignment())
    if Q == 'X': #수행평가 입력 안함 - 앞서 입력한데까지만 입력
        break
U = Stack()

def calen(n, items): #달력 구현 - 일정을 상세히 알려줌 - 달력을 표의 형태로 만듦
    z = 0 
    A = calendar.monthrange(2019,n) #해당 년도,달 설정
    X = ['']*35 #5주 - 7 X 5 = 35
    Y = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7] #표의 달력 구성 요소에 숫자(날짜) 입력  - 리스트 이용
    D = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7] #표의 달력 구성 요소에 숫자(날짜) 입력  - 리스트 이용
    for i in range (0, A[1]):
        X[i+A[0]] = i+1
    for i in range (0, 5):
        for j in range(0, 7):
            Y[i][j] = X[7*i+j] #다음 주
    for a in range(0, len(items)): #날짜 밑에 있는 칸에 수행평가 일정 표현하기 
         for i in range (0,5):
            for j in range (0, 7):
                if Y[i][j] == items[a].day:
                    for k in range(0, int(items[a].X)):
                        D[i][j-k] = D[i][j-k]+items[a].name
    
    cal = np.array([Y[0], D[0], Y[1], D[1], Y[2], D[2], Y[3], D[3], Y[4], D[4]]) #1,2,3,4 주 달력 표현
    pd.DataFrame(cal)
    display(pd.DataFrame(data = cal, columns = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'], index = ['', '', '', '', '', '', '', '', '', ''])) #맨 위에 요일 표현
    
calen(4, k) #사용자가 월을 입력해야 함 - 이 코드에는 4월
