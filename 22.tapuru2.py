num_tuple = (10,20)
print(num_tuple)

x,y = num_tuple
print(x,y)
# アンパッキングと言って代入をしてくれる
x,y = 10,20
print(x,y)

min, max = 0,100
print(min , max)

# この記述のやり過ぎには注意が必要になってくる

i = 10
j = 20
tmp = i
i =j
j =tmp
print(i, j)


a = 100
b = 200

a,b = b, a
# この記述で中身を入れ替えることが可能

print(a,b)

