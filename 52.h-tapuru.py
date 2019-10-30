def say_something(*args):
    print(args)
    # *argsを使うとタプルに入れていくれるようになる
    for arg in args:
        print(arg)

say_something('hi', 'mike', 'nance')
# ここの行を揃えないと出力されない

t = ('Mike', 'Nancy')
say_something('hi', *t)

