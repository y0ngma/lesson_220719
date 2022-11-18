# 객체지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트 -> 함수중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리
# 간단한 프로젝트(크롤링 등)는 절차지향이 파이선 생산성을 살림

car_company_1 = "Ferrari"
car_detail_1 = [
        {'color':"White"},
        {'horsepower':400},
        {'price': 5000}
        ]
car_company_2 = "BMW"
car_detail_2 = [
        {'color':"White"},
        {'horsepower':200},
        {'price': 2000}
        ]
car_company_3 = 'Audi'
car_detail_3 = [
        {'color':"Red"},
        {'horsepower':300},
        {'price': 3000}
        ]

# 리스트 구조
# 관리가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color':"White", 'horsepower':400, 'price': 5000},
    {'color':"White", 'horsepower':200, 'price': 2000},
    {'color':"Red", 'horsepower':300, 'price': 3000},
]

del car_company_list[1]
del car_detail_list[1]


class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self): # 사용자레벨에서 정보확인 print
        return 'str : {} = {}'.format(self._company, self._details)
    
    def __repr__(self): # representation 개발자레벨에서 정보확인
        return 'repr : {} = {}'.format(self._company, self._details)
        
    def __reduce__(self):
        pass
        
car1 = Car('Ferrari', {'color':"White", 'horsepower':400, 'price': 5000})
car2 = Car('BMW', {'color':"Black", 'horsepower':200, 'price': 1000})
car3 = Car('Audi', {'color':"Red", 'horsepower':100, 'price': 800})

# print(car1)
# print(car2)
# print(car3)
print(car3.__dict__)

# print(dir(car1))

car_list = list()

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 반복(__str__)
for x in car_list:
    print(repr(x))
    