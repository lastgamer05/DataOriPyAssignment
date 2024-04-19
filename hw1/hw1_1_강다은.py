import info


def sumEven(a, b): # 좀 더 깔끔한 코드를 위해 짝수만 더하는 함수를 정의

    result = 0

    for i in range(a, b+1): # a와 b사이의 수
        if i % 2 == 0: # 짝수 판별
            result += i # 짝수이면 result에 더하기

    return result


info.print_info() # 인적사항 출력

a = int(input("시작 정수 입력(0 이상) : "))
b = int(input("끝 정수 입력(0 이상) : "))

'''else에 주된 코드를 짜는 것보다 if에 짜는 것이 더 가독성이 좋을 것이라 생각해서
모든 조건을 만족하는 것을 먼저 따져줌'''

if a >= 0 and b >= 0 and (b-a) >= 0: 
    print(sumEven(a, b)) # 함수 실행

elif a < 0 or b < 0: # 예외 판별
    print("입력된 값에 음수가 포함되어 있습니다")
else:
    print("끝 정수가 시작 정수보다 작습니다")
