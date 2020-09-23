import random
from math import sqrt

if __name__ == '__main__':
    # 1.计算1~100求和
    sum1 = 0
    for i in range(0, 101):
        sum1 = sum1 + i
    print(sum1)
    # 2.1~100之间的偶数求和。
    sum2 = 0
    for i in range(0, 101, 2):
        sum2 = sum2 + i
    print(sum2)
    # 2.1~100之间的奇数求和。
    sum3 = 0
    for i in range(1, 101, 2):
        sum3 = sum3 + i
    print(sum3)
    '''
    计算机出一个1到100之间的随机数，玩家输入自己猜的数字，
    计算机给出对应的提示信息（大一点、小一点或猜对了），
    如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
    '''

    num = random.randint(1, 100)
    print('随机数字:%d' % num)
    flag = True
    i = 0
    while flag:
        printNum = int(input('请输入数字：'))
        if num < printNum:
            print('请输入小一点')
            i += 1
        elif num > printNum:
            i += 1
            print('请输入大一点')
        else:
            i += 1
            flag = False
            print('猜对了')
            print('一共猜了%d次' % i)
    '''
    输入一个正整数判断是不是素数
    '''
    inputNum = int(input('请输入一个正整数:'))
    end = int(sqrt(inputNum))
    flag = True
    while flag:
        if isinstance(inputNum, int) and inputNum > 1:
            for i in range(2, end + 1):
                if inputNum % i == 0:
                    print('%d不是素数' % inputNum)
                    flag = False
                    break
                # else:
                #     print('%d是素数' % inputNum)
                #     flag = False
        else:
            print('请输入正确的数字！')
