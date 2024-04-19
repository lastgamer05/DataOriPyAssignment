import info

    
def printNumber(n): # 숫자 쓰는 함수 정의
    for i in range(1, n+1):

        for j in range(1, i+1):
            print(j, end=' ') # 줄바꿈 하지 않기 위해 end씀
        print()


info.print_info()

a = int(input("양의 정수 입력 : "))

while a > 0: # a가 0보다 작거나 같으면 빠져나옴
    printNumber(a) # 함수 호출(print 안에 쓰면 none값 생김)

    a = int(input("양의 정수 입력 : "))

print("입력 오류")
