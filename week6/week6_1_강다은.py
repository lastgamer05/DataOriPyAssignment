def print_name():
    print("학과 : 사이버보안")
    print("학번 : 2467001")
    print("이름 : 강다은")



def Max(a,b,c):
    maximum = a # 최대 변수 정하기

    if b > a: # 최댓값 찾는중
        maximum = b # 최댓값보다 크다면 b를 최댓값으로 설정

        if c>b:
            maximum = c
    elif c > a: # 다른 경우 생각해주기
        maximum = c

        if b>c:
            maximum = b

    return maximum # 함수를 호출하면 최댓값을 리턴해주기
print_name()

print("세 정수를 입력하세요")
n1 = int(input("n1 : ")) # 입력값 받기
n2 = int(input("n2 : "))
n3 = int(input("n3 : "))

print("%d, %d, %d 중 가장 큰 수는 %d입니다" %(n1, n2, n3, Max(n1, n2, n3)))
