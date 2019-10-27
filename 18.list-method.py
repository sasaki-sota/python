r = [1,2,3,4,5,1,2,3]
print(r.index(3,  3))
# indexのどの場所に入っているかを教えてくれる
print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
# 綺麗に順番通りにしてくれる
r.sort(reverse=True)
print(r)
# 逆側にならば帰る

s = 'My name is Mike'
to_split = s.split(' ')
# スペースに分けて出力してくれる(''の中にスペースを一つ入れる)
print(to_split)

x = ' '.join(to_split)
# joinを使うて繋げる
print(x)

help(list)
