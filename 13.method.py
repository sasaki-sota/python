s = 'My name is Mike. Hi Mike.'
is_start = s.startswith('My')
# 変数の後に.を打つと様々なものを表示してくれる
print(s)
print(is_start)

print(s.find('Mike'))
# findは選択した文字を探してくれる
print(s.count('Mike'))
print(s.capitalize())
# capitalizeは最初のみを大文字で返しそれ以外は小文字で返す
print(s.title())
print(s.replace('Mike', 'Nancy'))
# replaceで文字を置き換えることが可能になる

