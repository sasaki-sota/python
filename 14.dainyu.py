print('a is {}'.format('a'))
# aが{}の中に代入されている
print('a is {}'.format('test'))
print('a is {}'.format('1, 2, 3'))

print('my name is {1} {0}'.format('Souta', 'Sasaki'))
# {}の中に番号を入れて行のどの文字を入れるか指定をすることができる
print('my name is {name} {family}'.format(name = 'unti', family = 'osere'))
# 置き換えて出力することが可能

print(1)
print('1')
print(str(1))
# 文字列に変更することができるようになる（型）
x = str(1)
type(x)

