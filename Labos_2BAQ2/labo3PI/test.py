def conversion(n):
    q = -1
    res = ''
    while q != 0:
        q = n // 2
        r = n % 2
        res = str(r) + res
        n = q
    return int(res)

def binrep(nbr):
    listBinaire = list(conversion(nbr))
    return listBinaire

print(binrep(12))