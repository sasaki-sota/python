x = 10
if x < 0:
    print('nefative')
elif x == 0:
    print('zero')
elif x == 10:
    print('ten')
elif x == 43:
    print('te')
else:
    print('positive')

a = 5
b = 10
if a > 0:
    # 後ろに':'を入れることに注意が必要
    print('positive')
    if b > 0:
        print('b is positive')
        # イフ文などはインテンドを綺麗に合わせる必要がある
        