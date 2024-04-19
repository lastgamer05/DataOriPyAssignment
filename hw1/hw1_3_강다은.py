import random
import info


ans = random.randint(1, 6) # 무작위 수 선택
i = 0

def isRight(ans, guess): # 답과 입력값을 비교
    if ans == guess:
        return True # 같다면 True 반환
    else:
        return False # 다르면 False 반환

info.print_info()
print("주사위를 던졌습니다")

while True: # 무한 루프
    i += 1 # 시도 횟수

    guess = int(input("주사위 눈을 맞혀보세요"))
    if 0 < guess < 7: # 1과 6사이의 수 판별
        if isRight(ans, guess):
            print("%d 번 만에 맞혔습니다" %(i))
            break


    else: # 예외 판별
        print("(범위를 벗어난 값입니다)")
