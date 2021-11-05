try:
    f = open('foo.txt', 'r')
    for r in f:
        print(r.strip())
    f.close()
except FileNotFoundError:
    print('找不到文件')
except Exception as e:
    print(e.args)