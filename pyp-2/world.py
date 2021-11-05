import sys
f = ""
sum = 0
for s in sys.argv:
    try:
        n = int(s)
        f += s + '+'
        sum += n
    except ValueError:
        try:
            n = float(s)
            f += s + '+'
            sum += n
        except:
            pass
print(f.strip('+'), '=', sum)