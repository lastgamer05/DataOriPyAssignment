import numpy as np
import info

info.print_info()

a = int(input("* n x n 배열 행 크기(n은 홀수, 0이하 입력시 종료) : "))

while a > 0: # 입력값이 0 이상인지 판별
    if a % 2 == 1: # 홀수이면
        np_array = np.arange(a ** 2) # 1차원 배열 만들기 위해 제곱
        np_array_num = np_array % 2 # 0과 1로 만들기 위해 2로 나눔
        result = np_array_num.reshape(a, a) # a x a 배열로 변환
        print(result)
    else:
        print("홀수가 아님") # 짝수이면

    a = int(input("* n x n 배열 행 크기(n은 홀수, 0이하 입력시 종료) : "))
print("종료")
