import info

info.print_info()

a = int(input("Input a number : "))

def isPrime(n): # 소수 판별 함수 선언
    for i in range(2, n): # 2부터 n-1까지 따져줌
        if n % i == 0: # 나눠지면 소수가 아니므로 False반환
            return False

    return True # for문이 끝날 때까지 나눠지는 수가 없으면 True반환

while a > 0: # a 가 0 이상일 때 계속 입력 받음
    if isPrime(a): # 소수면 소수라고 출력
        print("%d is a Prime number" %(a))
    else:
        print("%d is not a Prime number" %(a))
    print()
    a = int(input("Input a number : "))

print("Finished")
