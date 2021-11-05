f = open('hello.txt', 'r', encoding='gbk')
for r in f:
    print(r.strip())
# s1 = f.readline()
# s2 = f.readline()
# print(s1.strip())
# print(s2.strip())
# print(f.read())
# l = list(f)
# print(l[0].strip())
f.close()

