import info

info.print_info()

ans = input("문자열 입력 : ") # 문자열 입력 받기

def first(input): # 리스트 pop 이용 함수
    ans_list = list(input) # 리스트로 선언
    output1 = '' # 출력할 문자열 생성
    for i in input: # 문자열 차례로 이용하기 위해
        output1 += ans_list.pop() # pop이용해서 하나씩 반대로 붙임
    return output1

def second(input): # reverse 후 join이용하는 함수
    ans_list = list(input) 
    ans_list.reverse() # reverse() 는 객체 자체를 변환시킴
    output2 = ''.join(ans_list) # join이용
    return output2

def third(input): # 문자 떼서 앞에 붙이는 함수
    output3 = '' # 문자열 선언
    for i in input:
        output3 = i + output3 # 앞에 붙이기
    return output3


print("<리스트 pop 이용>")
print(first(ans))
print("<리스트 reverse 후 join 이용>")
print(second(ans))
print("<문자를 하나씩 앞에 붙이기>")
print(third(ans))
print("<문자열 슬라이싱 이용>")
print(ans[::-1]) # 문자열 슬라이싱 이용
