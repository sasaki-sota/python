d = {'x': 10, 'y': 20}
print(d)

d.keys()
# キーのみを参照することができる
d.values()
# ヴァリューのみが帰ってくる
d2 = {'x': 1000, 'y' : 500}
print(d2)

d.update(d2)
# updateで上書きをすることができる

d.get('x')
# ゲットを使って呼び出すこともできる
d.get('z')

del d['y']

'a' in d
# dの中にaが入っているか判定してくれる