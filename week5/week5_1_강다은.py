print("학과 : 사이버보안")
print("학번 : 2467001")
print("이름 : 강다은")

a = int(input("양의 정수 입력 : ")) # 정수 입력 받음
j = 0

if a > 0:
    for i in range(1, a+1): # i 1부터 시작하게 반복
        j += 1/i # j에 계속 값을 더함
    print("결과값 : %.2f" %(j))
else: # 예외 판별
    print("입력값의 범위가 틀렸습니다")
