s = 'test'
print(s)

print('hello.\nHow are you?')

print("""
line1
line2
line3
""")
# ダブルコーデーションを３つ使うことで複数の文字を出力することができるようになる

print('Hi' * 3 + 'Mile.')
# 様々なものを組み合わせることが可能

word = 'python'

print(word[0])
# []に括られた番号の文字を出力（インデックス　index)
print(word[1])
print(word[-1])
# 最後の文字を出力する場合は-1を使う

print(word[0:2])
# スライスという機能（選択した場所を出力してくれる）
print(word[:2])
print(word[2:])
# 様々な短縮形が存在する

word = 'j' + word[1:]
print(word)
# このようにすることで簡単に文字の連結が可能

n = len(word)
# lenはlengthの略であり、文字の数を教えてくれる
print(n)