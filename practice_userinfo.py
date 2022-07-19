# -*- coding: UTF-8 -*-
'''
OOP(Object Oriented Programming)
프로그램을 명령어들의 목록이 아니라 여러개의 독립된 단위 "객체"들의 모임으로 생각하는 것입니다.
각각의 객체들은 데이터를 주고 받을 수 있고, 독자적으로 데이터를 처리할 수 있습니다.
장점은 객체들의 모임이기 때문에 수정, 삭제, 추가가 쉽습니다.
단점은 코드량이 증가합니다.
객체란?
객체를 설명하기 위한 파일 구성도
파일, 문서, 동영상 등등 파일 구성도에 있는 모든 사각형들은 객체입니다.
파일은 이름, 크기, 내용, 위치 값은 필수로 가져야 합니다.
문서는 파일의 내용을 그대로 유지하며 문서에 맞는 추가 정보를 가집니다. 
만약 pdf 문서 버전이 업데이트 되어 수정이 필요한 경우 우리는 pdf 객체만 수정하면 됩니다. 
만약에 mp3가 구조적인 문제로 인하여 사용하면 안되는 경우 발생 시 우리는 mp3만 제거하면 됩니다.
편리하게 수정, 삭제, 추가가 가능해 보이지만 이렇게 사용하기 위해서는 초기 설계가 아주 중요합니다.
Class 활용하기
'''


di = {
    'member' : 
        [
            {'name':'정재우','age':27,'address':'서울시 송파구 오금로61길',
            'job':'대학생','hobby':['운동','뉴스보기','게임'],
            'goal':'보다 나은 세상',
            'like':{
                'food':['삼겹살','치킨','회','장어'],
                'device':['컴퓨터','스마트폰','에어컨'],
                'nation':['대한민국','중국','동남아시아']
            }},
            {'name':'박지숙','age':44,'address':'서울시 용산구 새창로 도원래미안',
            'job':'프리랜서강사','hobby':['리폼','고양이쳐다보기','책읽기','교안만들기'],
            'goal':'딸 대학보내기',
            'like':{
                'food':['잔치국수','삼겹삽','자몽','팥빙수','치킨'],
                'device':['노트북','건조기','블루투스 스피커'],
                'nation':['대한민국','베트남','스위스']
            }},
            {'name':'이정은', 'age':0, 'address':'서울시 광진구 능동 143',
            'job':'편집자', 'hobby':['연기', '노래', '영화', '책', '여행'],
            'goal':'나와 내 이웃이 행복하게 사는 것',
            'like':{
                'food':['치킨','엄마표 고추장찌개', '연어', '체리', '포도'],
                'device':['아이폰', '노트북', '에어팟'],
                'nation':['대한민국', '독일', '캐나다']
            }},
            {'name':'이영은','age':26,'address':'인천',
            'job':'회사원','goal':'찾는중?', 'hobby':['여행','독서','사진'],
            'like':{
                'food':['떡볶이','빵','치킨'],
                'device':['노트북','카메라','핸드폰'],
                'nation':['한국','미국','대만']
            }},
            {'name':'정수철', 'age':0, 'address':'서울시 노원구',
            'job':'회사원', 'hobby':['야구', '수영', '대화'],
            'goal':'스포츠타운',
            'like':{
                'food':['냉면', '참치', '장어', '고기'],
                'device':['자동차','거꾸리','자이글'],
                'nation':['대한민국','뉴질랜드','우즈벡']
            }},
            {'name':'황용훈', 'age':38, 'address':'서울시',
            'job':'디자이너','hobby':['골프','독서','미술'],
            'goal':'자유',
            'like':{
                'food':['한식','중식','일식','양식','분식'],
                'device':['맥','피씨','모바일'],
                'nation':['한국','중국','미국']
            }},
            {'name':'류혜림', 'age':30, 'address':'경기도 파주시 번영로55', 
            'hobby':['netflix','영화보기','산책'],
            'goal':'하고 싶은거 하기',
            'like':{
                'food':['회','초밥','해산물','제철음식','갈비','삼겹살','냉면'],
                'program':['포토샵','일러스트','인디자인'],
                'nation':['한국','캐나다','코스타리카','터키','멕시코']
            }},
            {'name': '조영민', 'age':37, 'address':'서울 노원구 노원로 186-15', 
            'job':'faculty', 'hobby':['요리', '기타'], 'goal':'농부', 
            'like': {
                'food':['국수', '통닭', '초밥', '피자'],
                'device':['Toyota Car', 'Mobile Phone'],
                'nation': ['미국','독일','일본','프랑스']
            }},
            {'name':'이재권','age':26,'address':'경기도 의정부시 흥선로 98-1',
            'job':'예비창업자','hobby':['영화감상','젬베','음악감상','오토바이'],
            'goal':'신속배달만 고려하는 이륜차 시장을 넘어 안전을 고려하는 이륜차 시장을 만드는 것',
            'like':{
                'food':['닭','인도커리','양고기','소고기','회','배','포도','꿔바로우'],
                'device':['오토바이','스마트폰','카메라'],
                'nation':['대한민국','미국','북한','일본','중국','몽골','러시아']
            }},
            {'name':'홍성준', 'age':27, 'address':'경기도 광명시 하안동 하안주공 1008동',
            'job':'대학생', 'hobby':['사진촬영','비디오게임'],
            'goal':'데이터 분석 및 시각화',
            'like':{
                'food':['김치찌개', '삼겹살', '꽃등심'],
                'device':['컴퓨터','플레이스테이션','카메라'],
                'nation':['대한민국','일본','미국']
            }},
            {'name': '김대성', 'age':28, 'address':'서울시 관악로 12길 ',
            'join':'엔지니어', 'hobby': ['야구', '재즈공연', '게임'],
            'goal':'무료 기술 학교',
            'like':{
                'food':['참치찌게', '된장찌개', '치킨', '라면', '삼겹살'],
                'device': ['컴퓨터', '에어프라이', '오토바이'],
                'nation':['대한민국', '네덜란드','영국'] 
            }},
            {'name':'이진주', 'age':0, 'address':'경기도 평택시', 
            'job':0, 'hobby': ['자전거 타기', '여행', '러닝', '풍선아트'], 'goal':'노마드 개발자', 
            'like':{
                'food':['김치찌개', '삼겹살', '마라탕', '호떡'],
                'device':['노트북', '인덕션', '와인따개'],
                'nation':['대한민국','덴마크','필리핀','중국']
            }},
            {'name':'황희진', 'age':25, 'address':'인천광역시 계양구', 'job':'직장인', 
            'hobby':['고양이랑놀기', '웹서핑', '맛집탐방'],
            'goal':'코딩하는마케터',
            'like':{
                'food':['카레','만두','빵'],
                'device':['에어프라이어','이북리더기','미니빔프로젝터'],
                'nation':['중국','베트남','스웨덴']
            }},
            {'name': '정재윤', 'age':0, 'address':'서울시 마포구',
            'job':'프리랜서','hobby':['축구','파이썬','코딩'],
            'goal' : '투자가',
            'like':{
                'food':['떡볶이','삼겹살','스테이크','쌀국수'],
                'device':['자전거', '킥보드', '드론'],
                'nation':['대한민국','중국','싱가폴']
            }},
            {'name':'김마야','age':29,'address':'서울시 마포구 서교동', 
            'job':'사업기획자', 'hobby': ['복싱','수제맥주품평','중드/영드감상'],
            'goal':'디지털 노마드',
            'like':{
                'food':['곱창구이','막창구이','곱창전골','훠궈','양꼬치','떡볶이'],
                'device':['mac book','iphone','미니빔'],
                'nation':['대한민국','네덜란드','중국','호주']
            }},
            {'name':'김현석', 'age':00, 'address':'경기도 광명시','job': '자영업', 
            'hobby':'자전거', 'goal': '건물주',
            'like': {
                'food' : ['삼겹살', '김치찌개','곱창'],
                'device' : ['자전거', '커피머신', '스마트폰'],
                'nation' : ['몰디브', '대한민국', '스위스']
            }},
            {'name':'박미지','age': 30, 'address':'서울시 관악구 신림동',
            'job':'없음', 'hobby':['게임', '독서', '영화감상'], 'goal' : '취업', 
            'like': { 
                'food':['회', '치킨', '국수','삼겹살'], 
                'device':['iphone','컴퓨터','ps4pro'],
                'nation':['대한민국','캐나다','영국']
            }},
            {'name':'정명석','age':26,'address':'서울 용산구',
            'job':'student','hobby':['영화보기','중국어 공부'],'goal':'창업',
            'like':{
                'food':['삼겹살','스시'],
                'device':['컴퓨터','폰'],
                'nation':['대한민국','중국']}}
        ],
    'advisor' : [
         {'name':'김민철', 'age':38, 'address':'서울시 구로구 구로동 1129번지',
        'job':'개발자', 'hobby':['기타', '피아노', '게임'], 
        'goal':'무료 기술 학교',
        'like': {
            'food':['참치찌게', '된장찌게', '치킨', '라면', '삼겹살'],
            'device':['컴퓨터', '에어프라이', '오토바이'],
            'nation':['대한민국','네델란드','영국']
        }},
        {'name':'최원미', 'age':21, 'address':'서울시 강북구',
        'job':'학생', 'hobby':['요가', '웹툰', '영화'], 
        'goal':'부자 되기',
        'like': {
            'food':['오므라이스', '치킨', '새우', '삼겹살'],
            'device':['imac', '전동휠','스마트폰'],
            'nation':['대한민국','중국','프랑스','스위스','LA']
        }},
        {'name':'권상윤', 'age':44, 'address':'경기도 용인시',
        'job':'개발자', 'hobby':['독서', '자전거', '비디오게임'], 
        'goal':'잘먹고 잘살기',
        'like': {
            'food':['설렁탕', '치킨', '순대국', '순두부찌개'],
            'device':['XBOX one', 'Cervelo R3','Brompton', 'AWOL', 'Playstation4', 'Switch'],
            'nation':['대한민국','싱가폴','캐나다','아이슬란드']
        }}
    ]  
}
class UserInfo :
    """사용자 정보를 관리하는 UserInfo Class를 생성
    이름 또는 취미로 사용자 정보를 가져오는 함수를 만듭니다.
    """
    def getUserWithName(self, name):
        '''이름 검색으로 해당 유저의 정보를 가져옵니다.'''
        members = di.get('member')
        for member in members:
            if(member.get('name') == name) :
                return member    
        return 'None'

    def getUserWithHobby(self, hob):
        '''취미 검색으로 해당 유저의 정보를 가져옵니다.'''
        result = []
        members = di.get('member')
        for member in members:
            for hobby in member.get('hobby'):
                if(hobby == hob):
                    result.append(member)
                    break
        return result


if __name__ == "__main__":
    user = UserInfo()
    print(user.getUserWithName('김마야'))
    # print(user.getUserWithHobby('여행'))

    # def getHobby(input_hobby):
    #     results = list()
    #     members = di.get('member')
    #     for member in members:
    #         # print(member.get('name'))
    #         for hobby in member.get('hobby'):
    #             if hobby == input_hobby:
    #                 results.append(member)
    #                 break
    #     return results
    # results = getHobby('여행')
    # for person in results:
    #     print(person['name'])