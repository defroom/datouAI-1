f = open('hello.txt', 'a', encoding='gbk')
n = f.write('\n'+'再见'+'\n'+'李先生'+'\n')
f.close()