# Chapter 3-1 파이썬 데이터 모델
## Special Method(Magic Method)
## 파이썬의 핵심 -> 시퀸스(Sequance), 반복(Iterator), 함수(Functions), Class(클래스)
## 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 기본형
print(int(10))
print(int, float)

# 모든 속성 및 메소드 출력
# print(dir(int))
# print(dir(float))

n = 10
# print(type(n))
# print(n.__doc__)
print(n+100, n.__add__(100))
print(n*100, n.__mul__(100))
print(n.__bool__(), bool(n)) # 0이면 False
print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        # 인스턴스변수
        self._name = name
        self._price = price

    def __str__(self):
        return "Fruit Class Info: {} , {}".format(self._name, self._price)
    
    # def __add__(self):
    #     return self._price + 
    def __add__(self, other):
        print("called >> __add__")
        return self._price + other._price
    
    def __sub__(self, other):
        print("Called >> __sub__")
        return self._price - other._price

    def __le__(self, other):
        print("Called >> __le__")
        if self._price <= other._price:
            return True
        else:
            return False
    
    def __ge__(self, other):
        print("Called >> __ge__")
        if self._price >= other._price:
            return True
        else:
            return False
    
# 인스턴스 생성
s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)

# print(s1._price + s2._price) # 코드양 늘어나고 가독성도 떨어지는 방식
print(s1 + s2)

# 매직메소드
print(s1 >= s2)
print(s2 - s1)
print(s1 <= s2)
print(s1)
print(s2)