def say_something():
    # defで関数名を定義している
    print('hi')

say_something()

print(type(say_something))

f = say_something
f()
# このように置き換えも可能

def say_something():
    s = 'hi'
    return s
    # returnをつける必要がある

result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'greengds'
    else:
        return 'i dont konw'
        # 今までのようにprintではなく関数なのでreturnを返す

# colorが引数
    print(color)

what_is_this('red')
# colorにredが入っている状態
# 何回も呼び出すコードに使う