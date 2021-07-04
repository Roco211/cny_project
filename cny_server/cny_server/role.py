# 角色


class worker:
    # 做单人
    # property: 做单人, 做单字典
    #
    #
    def __init__(self,nick):
        self.__nick__ = nick # 做单人
        self.__user_list__ = {} # 做单字典


    def add_user(self, phone, name):
        # 增加
        self.__user_list__[phone] = name

    def del_user(self, phone):
        # 删除
        del(self.__user_list__[phone])

    def get_users(self):
        return self.__user_list__



class user:
    # 用户

    # 初始化对象
    def __init__(self, leader, phone, name):
        self.__leader__ = leader # 归属做单人
        self.__phone__ = phone # 用户手机号
        self.__uname__ = name # 用户名字

    # 删除用户
    def del_user(self, phone):
        del self


    def __str__(self):
        return str(self.__leader__)+str(self.__phone__)+str(self.__uname__)


