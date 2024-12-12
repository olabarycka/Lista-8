def zgadywanie_liczby():
    szukana_liczba = 47
    licznik_prob = 0

    print("Witaj w grze zgadywanka liczbowa! Odgadnij liczbę z przedziału od 1 do 100!")

    while True:
        liczba_gracza = int(input("Podaj swoją liczbę: "))
        licznik_prob += 1
        if liczba_gracza > szukana_liczba:
            print("Szukana liczba jest mniejsza.")
        elif liczba_gracza < szukana_liczba:
            print("Szukana liczba jest większa.")
        else:
            print(f"Gratulacje! Udało ci się odgadnąć liczbę ({szukana_liczba}) po tylu próbach: {licznik_prob}!")
            break

zgadywanie_liczby()