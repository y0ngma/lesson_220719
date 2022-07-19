# -*- coding: UTF-8 -*-
from multiprocessing.sharedctypes import Value
from practice_userinfo import UserInfo

class Display:
    """
    사용자가 보게되는 화면
    입력과 출력을 담당
    """
    def goQuestion(self):
        value = input('검색할 취미 입력하세요 : ')
        self.searchWithHobby(value)
        
    def nameorhobby(self):
        search_way = input("뭘로 하시겠습니까? (1:이름, 2:취미)")
        if search_way == "1":
            value = input('사용자 이름 입력 : ')
            self.searchWithName(value)
        elif search_way == "2":
            value = input('같은 성향의 사람을 찾아 드립니다. 관심사 입력 : ')
            self.searchWithHobby(value)

    def searchWithName(self, value):
        user = UserInfo()
        userinfo_list = user.getUserWithName(value)
        self.show(userinfo_list)
        
    def searchWithHobby(self, value):
        user = UserInfo()
        userinfo_list = user.getUserWithHobby(value)
        self.show(userinfo_list)

    def show(self, userinfo_list):
        for userinfo in userinfo_list:
            print("=====================================")
            for key, value in userinfo.items():
                if type(value) == dict: print("-------------------------------")
                print(key, value)

    def show_test(self):
        user = UserInfo()
        self.show(user.getUserWithHobby('여행'))

if __name__ == "__main__":
    display = Display()
    # display.goQuestion()
    # display.show_test()
    display.nameorhobby()