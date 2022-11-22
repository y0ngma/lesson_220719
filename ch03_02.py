# Chapter 3-2 파이썬 데이터 모델
## Special Method(Magic Method)
## 파이썬의 핵심 -> 시퀸스(Sequance), 반복(Iterator), 함수(Functions), Class(클래스)
## 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 클래스 예제2: 수학을 쓰는 개발자에게 도움이 되는 프로그램을 개발해라!
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# (5, 10) 의 최대값은? -> 10

class Vector(object):
    """
     The following methods can be defined to emulate numeric objects. 
    These methods are called to implement the binary arithmetic(산수) 
    operations (+,-,*...). For instance, to evaluate the expression "x+y",
    where "x" is an instance of a class that has an __add__() method, 
    type(x).__add__(x, y) is called. 
    출처: https://docs.python.org/3/reference/datamodel.html#special-method-names
    """
    # def __init__(self, x, y):
    #     self._x, self._y = ...
    def __init__(self, *args):
        """
        Create a vector. For example : v=Vector(5, 10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """return the vector informations."""
        return "Vector({},{})".format(self._x, self._y)
        # return "Vector(%r, %r)" % (self._x, self._y)

    def __add__(self, other):
        """Return the vector addition of self and other"""
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        """Return the vector mulition of self and other"""
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        """원점인지 판별하기. bool(0) -> False"""
        if not bool(max(self._x, self._y)):
            print(self._x, self._y, "는 원점입니다")
        return bool(max(self._x, self._y))

print(Vector.__doc__)

v1 = Vector(1,2)
v2 = Vector(15,22)
v3 = Vector()

print(v1.__init__.__doc__)
print(v1.__repr__.__doc__)
print(v1.__mul__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v2 * 10)
# print(bool(v1), bool(v2), bool(v3))
print(bool(v2))
print(bool(v3))
# if bool(v2):
#     print("ok")