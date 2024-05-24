import string
import info
info.print_info()

f = open('Time is.txt', 'r') # 파일 열기
for i in f: # 파일 줄 가져와서 출력
    print(i, end='')

f = open('Time is.txt', 'r')
words = set() # 집합 선언
for line in f: # 줄 가져와서 출력
    line_words = line.split() # 단어 잘라서 리스트에 저장
    for word in line_words: # 단어 저장
        words.add(word)
words_list = list(words) # 리스트로 변환
words_list.sort() # 정렬

print("<Word List>")
print(words_list)

upper = 0 # 대문자 수
lower = 0 # 소문자 수
number = 0 # 숫자 수
etc = 0 # 기타문자 수

for w in words_list: # 단어 하나씩 쪼개기
    for i in w: # 한글자씩 확인
        if i in string.ascii_uppercase:
            upper += 1 # 수 증가
        elif i in string.ascii_lowercase:
            lower += 1
        elif i in string.digits:
            number += 1
        else:
            etc += 1

print("<단어 리스트에 포함된 문자 수>")
print("총 단어수 : ", len(words_list))
print("대문자 수 : ", upper)
print("소문자 수 : ", lower)
print("숫자 수 : ", number)
print("기타 : ", etc)
