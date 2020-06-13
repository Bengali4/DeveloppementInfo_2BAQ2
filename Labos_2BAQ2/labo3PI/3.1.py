def conversion(n):
    q = -1
    res = ''
    while q != 0:
        q = n // 2
        r = n % 2
        res = str(r) + res
        n = q
    return res

def binrep(nbr):
    listBinaire = list(conversion(nbr))
    listBinaire.reverse()
    return iter(listBinaire)

b = binrep(12)
while True:
    try:
        print(next(b))
    except StopIteration:
        break