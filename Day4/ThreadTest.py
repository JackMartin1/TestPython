'''
    多线程
'''

import threading
import time


class MyThread(threading.Thread):
    var1 = '变量1'

    def run(self):
        for i in range(3):
            print('ThreadName {}, @numbers {}'.format(self.name, i))
            time.sleep(1)

    def fun1(self, var1):
        print('This is' + var1)


def main():
    print('Start MainThread')

    threads = [MyThread() for i in range(3)]
    for t in threads:
        t.start()
        t.join()
        t.setDaemon()
    # for t in threads:
    #     t.join()

    print('End MainThread')


if __name__ == '__main__':
    name = ['a', 1, 'b', 2, 'c']
    print(name[1:-1])
    name.append('ccc')
    print(name)
    name += 'a'
    del name[1]
    print(name)
    name.insert(0, 'NO.1')
    print(name)
    name.remove('a')
    print(name)
    name.pop()
    print(name)

    dic = {'a': 1, 2: 'b', 'c': 3}
    for a in dic:
        print(a, end=' ')
    iterator = iter(dic.values())
    for i in iterator:
        print(i)
    list1 = [(x, y) for x in range(3) for y in range(2)]
    print(list1)
    print(MyThread.fun1(var1='123'))
