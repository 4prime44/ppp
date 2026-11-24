from silnik import generuj_kod
from sprawdzanie_mastermind import sprawdzenie

MAX_PROBA = 10
DLUGOSC_KODU = 4


def lista_na_liczbe(lista_cyfr):
    return int("".join(str(cyfra) for cyfra in lista_cyfr))


def wczytaj_probe(tura):
    while True:
        tekst = input(f"Tura {tura}/{MAX_PROBA} - podaj {DLUGOSC_KODU}-cyfrowy kod (cyfry 1-9): ").strip()

        if " " in tekst:
            elementy = tekst.split()
        else:
            elementy = list(tekst)

        if len(elementy) == DLUGOSC_KODU and all(x.isdigit() and 1 <= int(x) <= 9 for x in elementy):
            return [int(x) for x in elementy]
        
        print(f"Błąd! Podaj dokładnie {DLUGOSC_KODU} cyfry z zakresu 1-9.")


def main():
    sekretny_kod_lista = generuj_kod(dlugosc=DLUGOSC_KODU)
    sekretny_kod_liczba = lista_na_liczbe(sekretny_kod_lista)

    print(f"Zgadnij {DLUGOSC_KODU}-cyfrowy kod (cyfry od 1 do 9):")

    for tura in range(1, MAX_PROBA + 1):
        proba_lista = wczytaj_probe(tura)
        proba_liczba = lista_na_liczbe(proba_lista)

        wynik = sprawdzenie(proba_liczba, sekretny_kod_liczba)

        if wynik == "Zgadłeś sekretny kod":
            print(f"GRATULACJE! Zgadłeś kod w {tura}. próbie.")
            return
        else:
            print(f"Trafione na dobrych pozycjach: {wynik if wynik else 'brak'}")

    print(f"KONIEC GRY, wykorzystałeś wszystkie próby. Szukany kod to: {sekretny_kod_liczba}")


if __name__ == "__main__":
    main()