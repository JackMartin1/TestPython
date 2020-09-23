from Day4 import User as user
class User(object):
    var = 'aaa'
    def __init__(self, name, age, sex):
        self.name = name
        self.__age = age
        self._sex = sex

    @property
    def name(self):
        return self.name()

    @name.setter
    def name(self, name):
        self.name = name

    @name.getter
    def name(self):
        return self.name

    def _test(self):
        print('私有方法')

    @classmethod
    def mm(cls):
        return cls.var


if __name__ == '__main__':
    # user = User('我', 18, 'nv')
    # user.name = '1'
    # print(user.name)
    print(user.sumtest(1, 2))
    User.mm()
    # User.fun1(var='a')
    # print(user._User__age)
    # name = user.name
    # sex = user._sex
    # print(sex)
    # print(name)
    # age = user._User__age
    # print(age)
