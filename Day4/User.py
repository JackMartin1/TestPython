def sumtest(n1, n2):
    return n1 + n2


class User(object):
    var = 'aaa'

    # 类函数
    @classmethod
    def fun(cls):
        return cls.var

    # 普通函数
    def fun1(a):
        return a.var

    # 静态函数
    @staticmethod
    def fun2(self):
        return self


user = User
print(User.fun2('fun2'))
print(user.fun())
print(user.fun2('fun2---'))
print(sumtest(1, 2))
print(user.fun1)
