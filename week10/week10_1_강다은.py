import info

info.print_info()

n1Set = set() # 집합 초기화
n2Set = set()

while True: # 입력 받기
    n1 = int(input("양수 n1 입력 : "))
    if n1 > 0:
        break
while True: # 입력 받기
    n2 = int(input("양수 n2 입력 : "))
    if n2 > 0:
        break

for i in range(1, n1+1): # i를 나누기 위해 1부터 시작
    if n1 % i == 0:
        n1Set.add(i) # 집합에 약수 추가

for i in range(1, n2+1): # 위와 동일
    if n2 % i == 0:
        n2Set.add(i)

n12Set = n1Set & n2Set # 교집합
listN12set = sorted(n12Set) # 정렬
maxN12 = max(listN12set) # 최대공약수 찾기

print("<%d의 양수>" %(n1)) # 프린트
print(sorted(n1Set))

print("<%d의 양수>" %(n2)) # 프린트
print(sorted(n2Set))

print("<%d, %d의 공약수>" %(n1, n2))
print(listN12set)

print("<%d, %d의 최대공약수>" %(n1, n2))
print(maxN12)
