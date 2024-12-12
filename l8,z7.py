import itertools

def wypisz_kombinacje():
    ksiazki = [1, 2, 3, 4, 5]
    kombinacje = itertools.combinations(ksiazki, 3)

    for kombinacja in kombinacje:
        print(*kombinacja)

wypisz_kombinacje()