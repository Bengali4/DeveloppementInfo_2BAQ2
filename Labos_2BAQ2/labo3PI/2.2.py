import time

def sleep(i):
    def decorator(f):
        def wrapper(*args):
            time.sleep(i)
            return f(*args)
        return wrapper
    return decorator

@sleep(5)
def printnum(i):
    print(i)

cnt = 3
while cnt > 0:
    printnum(cnt)
    cnt -= 1
print("KA-BOOM!")