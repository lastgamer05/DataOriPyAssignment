def print_name(): # 출력하는 함수
    print("학과 : 사이버보안")
    print("학번 : 2467001")
    print("이름 : 강다은")

def facto(n): # 팩토리얼 구현 함수
    if n>1:
        return n * facto(n-1) # 재귀함수
    else:
        return 1

print_name()

print("<while 조건문 사용>")

a = int(input("양수 입력(종료시 0 입력)"))

while a!= 0: # a가 0이 아닐때만 작동
    if a>0: # a가 0보다 크면 팩토리얼
        print("%d! = %d"%(a, facto(a)))
    else:
        print("음수가 입력되었습니다")

    a = int(input("양수 입력(종료시 0 입력)")) # 첫번째 입력후 바로 while문 돌리기 위해

print("0! = %d" %(facto(0))) # 0팩토리얼은 1
print("종료합니다")

print("<while True 사용>")
b = int(input("양수 입력(종료시 0 입력)"))

while True: # 무한루프
    if b > 0: # b가 0보다 크면 팩토리얼
        print("%d! = %d"%(b,facto(b)))
    elif b < 0:
        print("음수가 입력되었습니다")
    else: # 0이면 무한루프 나오기
        break
    b = int(input("양수 입력(종료시 0 입력)")) # 첫번째 입력후 바로 while문 돌리기 위해

print("0! = %d" %(facto(0))) # 0팩토리얼은 1
print("종료합니다")
