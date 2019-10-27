i = [1,2,3,4,5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1,2,3,4,5]
y = x.copy()
# コピーをすることができる
y[0] = 100
print('y = ', y)
# コピーを使わないとバグになる可能性がある
print('x = ', x)

x = 20
y = x 
y = 5
print(id(x))
print(id(y))
# 違うところになってしまう
print(x)
print(y)

x = [ 'a' , 'b']
y = x
print(id(x))
print(id(y))
print(y)
print(x)
