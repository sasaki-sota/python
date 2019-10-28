days = ['MOn', 'tue', 'fri']
fruits = ['apple', 'banana', 'prange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    # zipを使うことで大量の情報をまとめて出力することができるようになる
    print(day, fruit, drink)

