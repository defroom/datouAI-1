try: raise

    raise Exception('例外', '错误')

except Exception as e:
    a1, a2 = e.args
    print('a1 =', a1, 'a2 =', a2)