import info


def longname(a): # 긴 이름 길이 구하는 함수
    p = 0 # 리스트 자르기 위한 변수 초기화
    max = 0 # 최댓값 초기화
    for i in a:

        if len(a[p]) > max: # 최댓값보다 크다면 대입
            max = len(a[p]) 
        p += 1 # 리스트 번호 증가
    return max

def longnamePrint(a, max): # 프린트하는 함수
    p = 0 # 리스트 자르기 위한 변수 초기화
    for i in a:

        if len(a[p]) == max: # 최댓값과 같은 길이 출력
            print(a[p])
        p += 1

info.print_info()

x = ['banana', 'kiwi', 'apple', 'orange']
print(x)
n = longname(x)
print("과일명 최대길이 : %d" %(n))
longnamePrint(x, n)
