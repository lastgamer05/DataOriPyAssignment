print("학과 : 사이버보안")
print("학번 : 2467001")
print("이름 : 강다은")

n = int(input("양의 정수 입력 (0이하 입력시 종료) : "))
maximum = n # 최대 최솟값 모두 입력 값으로 설정
minimum = n

while True: # 더 깔끔한 코드를 만드려면 n<=0 이라는 조건 만들면 됨

    if n <= 0: # 0이하 입력 시 종료
        break # 무한 루프 탈출

    n = int(input("양의 정수 입력 (0이하 입력시 종료) : "))

    if n <= 0: # 0이하 입력 시 종료
        break # 무한 루프 탈출

    if n > maximum: # 입력 값이 최댓값보다 크다면 입력값을 최댓값으로 설정
        maximum = n
    if n < minimum: # 입력 값이 최솟값보다 크다면 입력값을 최솟값으로 설정
        minimum = n

print("max : ", maximum)
print("min : ", minimum)
