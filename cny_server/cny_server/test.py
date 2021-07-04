import role


user = role.user('LJG', '13636363366', 'test')


# print(user)
user.del_user('13636363366')
del user
print(user)