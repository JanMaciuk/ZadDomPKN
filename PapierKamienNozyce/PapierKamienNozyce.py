from random import randint

iloscWygranych = 0
remis = "Remis! zagraj jeszcze raz"
wygrana = "Wygrales!!! zagraj jeszcze raz"
przegrana = "Przeglajes ;( sproboj ponownie"
mozliwosci = ["papier","kamien","nozyce"]

komputer = mozliwosci[randint(0,2)]
gracz = False
while gracz == False:
    gracz = input("papier, kamien lub nozycze")
    if gracz == komputer:
        print(remis)
        print("ilosc wygranych: ")
        print(iloscWygranych)
    elif gracz == "kamien":
        if komputer == "papier":
            print(przegrana)
            iloscWygranych -= 1
            print("ilosc wygranych: ")
            print(iloscWygranych)
        else: 
            print(wygrana)
            iloscWygranych += 1
            print("ilosc wygranych: ")
            print(iloscWygranych)
    elif gracz == "papier":
        if komputer == "nozyczki":
            print(przegrana)
            iloscWygranych -= 1
            print("ilosc wygranych: ")
            print(iloscWygranych)
        else:
            print(wygrana)
            iloscWygranych += 1
            print("ilosc wygranych: ")
            print(iloscWygranych)
    elif gracz == "nozycze":
        if komputer == "kamien":
            print(przegrana)
            iloscWygranych -= 1
            print("ilosc wygranych: ")
            print(iloscWygranych)
        else:
            print(wygrana)
            iloscWygranych += 1
            print("ilosc wygranych: ")
            print(iloscWygranych)
    else:
        print("No miszczu, cus zes zwalil, pewnie literowka, masz tylko trzy opcje: papier , kamien , nozycze")
    if iloscWygranych < 3:
        gracz = False
        komputer = mozliwosci[randint(0,2)]
    elif iloscWygranych == 3:
        print("brawo, wygrales z komputerem przewaga 3 punktow") 
