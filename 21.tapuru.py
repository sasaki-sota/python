t = (1,2,3,4,1,2)
print(t)

type(t)
# listのようにタプルは代入することができない

t[0]

print(t.index(1,1))

t =([1,2,3,], [4,5,6])
print(t)

t[0][0] = 100
t = 1,2,3,
print(type(t))

t = 1,
# タプルの場合はカンマが勝手につく
t = ()
t = (1)
print(type(t))

t = ('test')
print(type(t))

t = 1