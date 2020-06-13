import time

def sleep(f):
    def wrapper(*args):
        time.sleep(1)
        f(*args)
    return wrapper

@sleep
def printnum(i):
    print(i)

cnt = 3
while cnt > 0:
    printnum(cnt)
    cnt -= 1
print("KA-BOOM!")