class assignment:   # 수행평가 클래스 제작
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
            
class Stack:   # Stack 구현
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
for i in range(0, 10000):  # 수행평가 입력 코드
    Q = input('수행평가를 입력하세요: O or X : ')
    if Q == 'O':  # 만약 수행평가가 있다면
        k.append(assignment())  # assignment클래스 실행 결과를 k 리스트에 추가
    if Q == 'X':  # 만약 수행평가가 없다면 종료
        break
U = Stack()

def calen(n, items):   # 달력 구현 코드 : 요일과 날짜를 표시
    z = 0
    A = calendar.monthrange(2019,n)  # 2019년 n월의 1일이 무슨 요일에 있는지와 몇일 까지 있는지를 튜플 형태로 반환
    X = ['']*35
    Y = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7]
    D = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7]
    for i in range (0, A[1]):  # 해당 요일에 날짜 매칭
        X[i+A[0]] = i+1
    for i in range (0, 5):  # 가로로 정렬되어 있는 것을 달력 형식으로 배열
        for j in range(0, 7):
            Y[i][j] = X[7*i+j]
    for a in range(0, len(items)):  # 수행평가 일정 달력에 추가
         for i in range (0,5):
            for j in range (0, 7):
                if Y[i][j] == items[a].day:
                    for k in range(0, int(items[a].X)):
                        D[i][j-k] = D[i][j-k]+items[a].name
    
    cal = np.array([Y[0], D[0], Y[1], D[1], Y[2], D[2], Y[3], D[3], Y[4], D[4]])
    pd.DataFrame(cal)
    display(pd.DataFrame(data = cal, columns = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'], index = ['', '', '', '', '', '', '', '', '', '']))
    
calen(4, k)  # 4월의 달력을 구현. 숫자 4를 바꾸어 다른 달의 달력도 구현할 수 있다.
