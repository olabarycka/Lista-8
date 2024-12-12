def oblicz_srednia():
    liczby = []

    while True:
        wejscie = input("Podaj liczbe rzeczywista lub wpisz 'end' aby zakonczyc): ")
        if wejscie.lower().strip() == 'end':
            if len(liczby) == 0:
                print("Błąd: 'end' nie może być pierwszą wprowadzoną wartością.")
                continue
            else:
                break

        try:
            liczba = float(wejscie)
            liczby.append(liczba)
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę rzeczywistą lub 'end'.")

    if len(liczby) > 0:
        srednia = sum(liczby) / len(liczby)
        print(f"Średnia arytmetyczna: {srednia}.")
    else:
        print("Brak liczb do obliczenia średniej.")

oblicz_srednia()