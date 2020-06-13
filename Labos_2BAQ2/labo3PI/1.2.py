def add(a, b):
    return (a + b)

def call(f, *args):
    return f(*args)

print(call(add, 2, 9))