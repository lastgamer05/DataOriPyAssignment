import info
import math

info.print_info()

class Point: # 클래스
    def __init__(self, id, x, y): # 생성자
        self.id = id # 인수를 필드에 넣음
        self.x = x   # == 초기화
        self.y = y

    def getX(self): # 인스턴스의 x좌표값 반환
        return self.x

    def getY(self):
        return self.y

    def print_point(self): # 프린트하는 함수
        print("%s : (%d, %d)" %(self.id, self.x, self.y))


x1 = int(input("p1의 x좌표 : "))
y1 = int(input("p1의 y좌표 : "))
x2 = int(input("p2의 x좌표 : "))
y2 = int(input("p2의 y좌표 : "))

p1 = Point('p1', x1, y1) # 인스턴스 생성
p2 = Point('p2', x2, y2)

p1.print_point()
p2.print_point()

def distance(x1, y1, x2, y2): # 거리 구하는 함
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("{} , {} 사이의 거리 : {:.2f}".format(p1.id, p2.id, distance(p1.getX(), p1.getY(), p2.getX(), p2.getY())))
