from Day5 import InitTest as initest
import re
a = 'JavaC++C#PythonAndroidIOSPHPJavaScrip'
if __name__ == '__main__':
    test = initest.MyTest
    print(test.addtest(test, 2, 2))
    print(re.findall('[A-Za-z]{1,3}', a))
    print(re.findall('[A-Za-z]*', a))

