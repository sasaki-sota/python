def text_func(x, l=[]):
    l.append(x)
    return l

# 引数を定義しているので返り値が必要になっていく
y = [1, 2, 3]
r = text_func(100, y)
print(r)

y = [1, 2, 3]
r = text_func(200, y)
print(r)

r = text_func(100)
print(r)

