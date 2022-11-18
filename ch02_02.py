# 인스턴스 변수
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
    """
    # 클래스변수(모든 인스턴스가 공유)
    car_count = 0
    
    
    # 변수
    def __init__(self, company, details):
        self._company = company
        # self.car_count = 10
        self._details = details
        Car.car_count += 1
    
    # 매소드
    def __str__(self): # 사용자레벨에서 정보확인 print
        return 'str : {} = {}'.format(self._company, self._details)
    
    def __repr__(self): # representation 개발자레벨에서 정보확인
        return 'repr : {} = {}'.format(self._company, self._details)
    
    def detail_info(self):
        print("Current ID      : {}".format(id(self)))
        print("Car Detail Info : {}".format(self._company, self._details))
        
    def __del__(self):
        print('del?')
        Car.car_count -= 1
        

car1 = Car('Ferrari', {'color':"White", 'horsepower':400, 'price': 5000})
car2 = Car('BMW', {'color':"Black", 'horsepower':200, 'price': 1000})
car3 = Car('Audi', {'color':"Red", 'horsepower':100, 'price': 800})

# 아이디 확인 - 클래스(붕어빵틀은 하나지만 붕어빵들은 다르다)
print(id(car1))
print(id(car2))
print(id(car3))

print(car1 is car2) # 아이디 값을 기준으로 비교
print(dir(car1))
print(dir(car2)) # 상속받는 매직메소드 모든것을 표시

print(car1.__dict__)

# Doctring
print(Car.__doc__)

# 실행
Car.detail_info(car2)
print()
car1.detail_info()
print()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__),id(car2.__class__),id(car3.__class__))

### 클래스 변수 공유 확인
print(Car.car_count)
print(car1.car_count)

# 삭제확인
del car2
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능( 인스턴스 검색후 -> 없으면 클래스변수, 부모클래스 검색함)