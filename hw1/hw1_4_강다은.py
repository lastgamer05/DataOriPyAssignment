import info
info.print_info()

password = input("암호 설정(관리자) : ") # 암호 입력
inp = input("로그인하려면 암호를 입력하세요 : ")

tryNumber = 1

while tryNumber < 3:

    if password == inp: # 패스워드와 입력값이 같으면 로그인 성공
        print("%d 번만에 로그인 성공" %(tryNumber))
        break

    tryNumber += 1 # 시도 횟수 증가
    inp = input("로그인하려면 암호를 입력하세요 : ")

if tryNumber == 3: # 시도 횟수 3번 되면 while문 빠져나와서 출력
    print("3회 이상 실패하여 더 이상 시도할 수 없습니다")
