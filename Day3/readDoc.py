def main():
    file = '456.txt'
    try:
        # t = open(file, 'r', encoding='utf-8')
        with open(file, 'r', encoding='utf-8') as t:
            print(t.read())
    except UnicodeDecodeError:
        print('编码错误')
    # finally:
    #     t.close()


if __name__ == '__main__':
    main()
