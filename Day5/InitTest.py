class MyTest:
    def __init__(self):
        print('初始化方法')

    def __del__(self):
        print('删除了')

    def addtest(self, a, b):
        return a + b


if __name__ == '__main__':
    my_test = MyTest()
    print(my_test.addtest(2, 2))
    del my_test
    print(dir(MyTest()))

