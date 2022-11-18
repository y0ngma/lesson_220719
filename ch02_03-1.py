# 객체지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트 -> 함수중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리
# 간단한 프로젝트(크롤링 등)는 절차지향이 파이선 생산성을 살림

class Car():
    # Doctring : print(Car.__doc__) 해서 확인가능한 부분
    """
    Car classs
    Author : Jeong Yonghee
    Date : 2020.05.18
    Description : Class, Static, Instance Method
    """
    # 클래스변수(모든 인스턴스가 공유)
    price_per_raise = 1.0
    
    # 변수
    def __init__(self, company, details):
        self._company = company
        # self.car_count = 10
        self._details = details
    
    # 매소드
    def __str__(self): # 사용자레벨에서 정보확인 print
        return 'str : {} = {}'.format(self._company, self._details)
    
    def __repr__(self): # representation 개발자레벨에서 정보확인
        return 'repr : {} = {}'.format(self._company, self._details)
    
    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print("Current ID      : {}".format(id(self)))
        print("Car Detail Info : {}".format(self._company, self._details))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price')*Car.price_per_raise)

# Self 의미
car1 = Car('Ferrari', {'color':"White", 'horsepower':400, 'price': 5000})
car2 = Car('BMW', {'color':"Black", 'horsepower':200, 'price': 1000})

car1.detail_info()
car2.detail_info()

# 가격정보 - 이렇게 직접 접근하는것은 좋지 않음
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보(인상 전)
print(car1.get_price_culc())
print(car2.get_price_culc())




