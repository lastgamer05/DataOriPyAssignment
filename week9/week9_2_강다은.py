import info

list1 = ['A', 'B', 'C']
list2 = [1, 2]

listx = [] # 리스트 초기화

for i in list1: # 'A', 'B', 'C'
    for j in list2: # 1, 2 
        listx.append(i + str(j)) # 형변환 시켜주기

listy = [x+str(y) for x in list1 for y in list2] # List Comprehension 이용

info.print_info()

print("<첫번째 리스트>") # 결과값 출력
print(list1)
print("<두번째 리스트>")
print(list2)
print("<중첩for문을 이용한 조합>")
print(listx)
print("<List Comprehension을 이용한 조합>")
print(listy)
