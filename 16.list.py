l = [1,34,5,6,7,8,76,]
# []で括ることでリストを作ることができる
print(l)
print(l[1])
print(l[-1])
print(l[2:5])
print(l[:2])

print(len(l))
print(type(l))
print(list('abcdefg'))

n = [1,2,3,4,5,6,7,8,9,]
print(n[::2])
# ::とすると指定したものを飛ばして出力してくれる

a = ['a', 'b', 'c']
n = [1,2,3]
x = [a, n]
print(x)
print(x[1])
print(x[0])
