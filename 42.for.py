some_list = [1,2,3,4,5]

i = 0
while i < len(some_list):
    # インデックスの長さ
    print(some_list[i])
    i += 1


for i in some_list:
    # some_listからiに代入されている
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'nsme', 'is', 'mile']:
    if word == 'name':
        continue
    print(word)
    # continuは等しい時に飛ばす？
    