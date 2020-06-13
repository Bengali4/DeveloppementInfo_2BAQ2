def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def call(f, *args, **kwargs):
    return f(*args, **kwargs)

def compute(*args, **kwargs):
    try:
        if kwargs["op"] == sub:
            return sub(*args)
    except:
        return add(*args)

print(call(compute, 2, 9))
print(call(compute, 2, 9, op=sub))