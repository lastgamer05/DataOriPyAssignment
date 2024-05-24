import numpy as np
import info

info.print_info()

height = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73] # 주어진 리스트
weight = [86.0, 74.0, 59.0, 95.0, 80.0, 68.0]

np_height = np.array(height) # 배열 생성
np_weight = np.array(weight) # 배열 생성

np_bmi = np_weight / (np_height ** 2) # bmi 계산

print("<키>")
print(np_height) 

print("<몸무게>")
print(np_weight)

result = np.array([np_height, np_weight, np_bmi]) # 2차원 배열 생성
print("<결과>")
print(result)

trans_resurt = result.transpose() # 전치행렬 생성
print("<키, 체중, bmi 순서 배열>")
print(trans_resurt)
