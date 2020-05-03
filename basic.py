import numpy as np #numpy 라이브러리를 불러오는데, np로 부르겠다고 명명.
import pandas as pd
import tensorflow as tf
import torch

arr1 = np.array([1,2,3,4]) # 1차 배열 생성. np.array이라는건 np 라이브러리의 array함수를 이용한다는 것.
arr2 = np.zeros(4) # 0으로 이루어진 1차 배열
arr3 = np.ones(4) # 1로 이루어진 1차 배열
print(arr1, arr2, arr3)

arr4 = np.array([3 : 9]) # 3부터 '8'까지 어레이를 만듦.
arr5 = arr4[arr4 < 5] # 조건도 넣을 수 있음.
arr6 = [arr4%2 == 1] # arr4를 2로 나누었을 때, 나머지가 1인 것들.
print(len(arr6)) # arr6의 길이(개수)

#응용
count = 0
for i in range(len(arr4)):
    if arr[i] % 2 == 1:
        count = count + 1
print(count)

#---------
def det(a,b,c): # def함수선언 det함수이름 (a,b,c)패러미터
    if a != 0:
        D = b**2 - 4*a*c
        if D > 0:
            print("서로 다른 두 실근")
        elif D == 0:
            print("서로 같은 두 실근")
        else:
            print("서로 다른 두 허근")
    else:
        print("2차 방정식이 아닙니다.")
det(0.2.4)

#-----------------

import module as ms # 파일을 만들고 그 안에 다양한 함수를 넣는다. 그리고 그것을 라이브러리처럼 가져다 씀.
ms.sum
from module import sum, mean # module의 함수만 가져다 쓰고 싶을 경우
mean(x)

#----------------
class Base:
    def __init__(self,a,b): # 나는 클래스를 생성할 때, a, b라는 값을 갖겠다. self는 인스턴스(밑에 m = Base(1,5)의 m)를 지칭하는 것.
        self.a = a #class 안의 모든 a,b 값을 지정 
        self.b = b

    def operator1(self):
        print(self.a+self.b) # 다음과 같이 사용.
    def operator2(self):
        print(self.a*self.b)
    def operator3(self,c):
        self.operator1() # 만약 operator3에서 operator1을 사용하고 싶을 경우
        print(c)

class Cal(Base): #상속. Cal이 Base의 모든 기능을 상속받음.
    def cal(self):
        self.operator1()
        self.operator2()

c = Cal(1,5) #단, Base를 상속받고 있는 것이기 때문에 Base처럼 a,b에 대한 변수를 받아야한다.

if __name__="__main__":
    m = Base(1, 5)
    m.operator1() # 6이 나옴
    m.operator2() # 5가 나옴
    m.operator3(3) # 3이 나옴