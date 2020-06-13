class NaturalIterator:
    def __init__(self, nbr):
        self.__nbr = nbr
        self.__bitlist = []
        q = -1
        while q != 0:
            q = self.__nbr // 2
            r = self.__nbr % 2
            self.__bitlist.append(r)
            self.__nbr = q
        self.__next = 0

    def __iter__(self):
        return self


    def __next__(self):
        try:
            bit = self.__bitlist[self.__next]
        except IndexError:
            raise StopIteration()
        self.__next += 1
        return bit

class Natural:
    def __init__(self, nbr):
        self.__nbr = nbr

    def __iter__(self):
        return NaturalIterator(self.__nbr)

N = Natural(4)
for i in N:
    for j in N:
        print(i, j)