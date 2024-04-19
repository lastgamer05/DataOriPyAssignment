import info

info.print_info()

class Dog: # 클래스 정의


    def __init__(self, name, age, weight): # 초기화
        self.name = name 
        self.age = age
        self.weight = weight
        self.sound = '' # 멤버변수 선언


    def bark(self): # 짖는 함수 정의
        if self.weight >= 20: # 경우 나누기
            Dog.sound = '컹컹' # sound에 값 넣기
        elif self.weight >= 10:
            Dog.sound = '멍멍'
        else:
            Dog.sound = '캥캥'

        print("{0}가 {1} 짖습니다. {2}살, {3}kg입니다".format(self.name, Dog.sound, self.age, self.weight))

d1 = Dog("바둑이", 3, 25) # 인스턴스 생성
d2 = Dog("메리", 7, 12)
d3 = Dog("순심이", 1, 5)

d1.bark() # 함수 호출
d2.bark()
d3.bark()
