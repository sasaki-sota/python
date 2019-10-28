count = 0 

while count < 5:
    # 5より小さい時に繰り返す
    print(count)
    count += 1
    # +1をしないと無限ループになってしまいカウントされていない状態となる

count = 0

while True:
    if count >= 5:
        break
    # break文は途中で抜けることができるようになる
    print(count)
    count += 1

    if count == 2:
        count += 1
        continue
# コンテニューすると次のプリント文にいかずにスキップして次のループに行く
    print(count)
    count += 1