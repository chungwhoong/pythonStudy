PI=3.1415 #변수

class Circle:  #클래스
    def __init__(self, r):
        self.r=r
    
    def circumference(self): #원주 구하기
        return self.r*2*PI
    
    def circleArea(self): #원의 넓이 구하기
        return (self.r**2)*PI
        a