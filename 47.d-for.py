d = {'x':100, 'y': 200}

print(d.items())

for k, v in d.items():
    # itemsを使うとinの前に定義しているものに代入することができるようになる
    print(k, ':', v)
