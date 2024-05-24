import info

info.print_info()

student1 = [('123', 'Tom', '010-111-1111', 'Seoul'), ('124', 'Jane', '010-222-2222', 'Busan'), ('125', 'Candy', '010-333-3333', 'Incheon')]
dic = {} # 딕셔너리 초기화
dic2 = {}
person = [] # 리스트 초기화
for a, b, c, d in student1: # 리스트에서 정보 받기
    dic[a] = b # 학번 이름 키 밸류로 설정
    dic2[a] = a, b, c, d # 학번과 사람 정보 매치

print("<학생명단>")
for i in dic:
    print(i, ":", dic[i]) # 딕셔너리 따라 출력

ans = input("조회할 학번은? (종료시 0 입력)")

while ans != '0': # 0아니면 계속 실행

    if ans in dic2: # 있는 학번인지 판별
        for i in range(4):
            person.append(dic2[ans][i]) # 리스트에 학생 정보 넣기
        print("id : %s" %(person[0]))
        print("name : %s" % (person[1]))
        print("phone : %s" % (person[2]))
        print("address : %s" % (person[3]))
    else: # 예외 처리
        print("해당 학번은 없음")

    person = [] # 초기화
    ans = input("조회할 학번은? (종료시 0 입력)")

print("종료")
