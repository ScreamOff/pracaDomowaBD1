import sqlite3

def append_funkcjonariusz(imie, nazwisko, stopien, numer_legitymacji):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nowego funkcjonariusza
    cursor.execute("INSERT INTO Funkcjonariusz (imie, nazwisko, stopien, numer_legitymacji) VALUES (?, ?, ?, ?)",
                   (imie, nazwisko, stopien, numer_legitymacji))

    connection.commit()
    connection.close()

def append_jednostka(nazwa, lokalizacja, id_funkcjonariusza):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nową jednostkę
    cursor.execute("INSERT INTO Jednostka (nazwa, lokalizacja, id_funkcjonariusza) VALUES (?, ?, ?)",
                   (nazwa, lokalizacja, id_funkcjonariusza))

    connection.commit()
    connection.close()

def append_sprawa(opis, status, id_jednostki):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nową sprawę
    cursor.execute("INSERT INTO Sprawa (opis, status, id_jednostki) VALUES (?, ?, ?)",
                   (opis, status, id_jednostki))

    connection.commit()
    connection.close()

def append_dowod(opis, id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nowy dowód
    cursor.execute("INSERT INTO Dowod (opis, id_sprawy) VALUES (?, ?)",
                   (opis, id_sprawy))

    connection.commit()
    connection.close()

def append_przestepca(imie_nazwisko, pseudonim, id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nowego przestępcę
    cursor.execute("INSERT INTO Przestepca (imie_nazwisko, pseudonim, id_sprawy) VALUES (?, ?, ?)",
                   (imie_nazwisko, pseudonim, id_sprawy))

    connection.commit()
    connection.close()

def append_aresztowanie(id_funkcjonariusza, id_przestepcy, id_sprawy, data_aresztowania):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nowe aresztowanie
    cursor.execute("INSERT INTO Aresztowanie (id_funkcjonariusza, id_przestepcy, id_sprawy, data_aresztowania) VALUES (?, ?, ?, ?)",
                   (id_funkcjonariusza, id_przestepcy, id_sprawy, data_aresztowania))

    connection.commit()
    connection.close()

def append_miejsce(nazwa_miejsca, opis):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nowe miejsce
    cursor.execute("INSERT INTO Miejsce (nazwa_miejsca, opis) VALUES (?, ?)",
                   (nazwa_miejsca, opis))

    connection.commit()
    connection.close()

def append_patrol(id_funkcjonariusza, data_patrolu):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nowy patrol
    cursor.execute("INSERT INTO Patrol (id_funkcjonariusza, data_patrolu) VALUES (?, ?)",
                   (id_funkcjonariusza, data_patrolu))

    connection.commit()
    connection.close()

def append_wykroczenie(opis, id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nowe wykroczenie
    cursor.execute("INSERT INTO Wykroczenie (opis, id_sprawy) VALUES (?, ?)",
                   (opis, id_sprawy))

    connection.commit()
    connection.close()

def append_ofiara(imie_nazwisko, id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nową ofiarę
    cursor.execute("INSERT INTO Ofiara (imie_nazwisko, id_sprawy) VALUES (?, ?)",
                   (imie_nazwisko, id_sprawy))

    connection.commit()
    connection.close()

def append_poszukiwany(imie_nazwisko, nagroda):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nowego poszukiwanego
    cursor.execute("INSERT INTO Poszukiwany (imie_nazwisko, nagroda) VALUES (?, ?)",
                   (imie_nazwisko, nagroda))

    connection.commit()
    connection.close()

def append_nagroda(id_poszukiwanego, kwota):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nową nagrodę
    cursor.execute("INSERT INTO Nagroda (id_poszukiwanego, kwota) VALUES (?, ?)",
                   (id_poszukiwanego, kwota))

    connection.commit()
    connection.close()

def append_interwencja(id_sprawy, id_funkcjonariusza, data_interwencji):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Dodaj nową interwencję
    cursor.execute("INSERT INTO Interwencja (id_sprawy, id_funkcjonariusza, data_interwencji) VALUES (?, ?, ?)",
                   (id_sprawy, id_funkcjonariusza, data_interwencji))

    connection.commit()
    connection.close()

def append_data(choice):
    if choice == '1':
        # Dodaj nowego funkcjonariusza
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        stopien = input("Podaj stopień: ")
        numer_legitymacji = input("Podaj numer legitymacji: ")
        append_funkcjonariusz(imie, nazwisko, stopien, numer_legitymacji)

    elif choice == '2':
        # Dodaj nową jednostkę
        nazwa = input("Podaj nazwę jednostki: ")
        lokalizacja = input("Podaj lokalizację: ")
        id_funkcjonariusza = input("Podaj ID funkcjonariusza przypisanego do jednostki: ")
        append_jednostka(nazwa, lokalizacja, id_funkcjonariusza)

    elif choice == '3':
        # Dodaj nową sprawę
        opis = input("Podaj opis sprawy: ")
        status = input("Podaj status sprawy: ")
        id_jednostki = input("Podaj ID jednostki przypisanej do sprawy: ")
        append_sprawa(opis, status, id_jednostki)

    elif choice == '4':
        # Dodaj nowy dowód
        opis = input("Podaj opis dowodu: ")
        id_sprawy = input("Podaj ID sprawy, do której przypisany jest dowód: ")
        append_dowod(opis, id_sprawy)

    elif choice == '5':
        # Dodaj nowego przestępcę
        imie_nazwisko = input("Podaj imię i nazwisko przestępcy: ")
        pseudonim = input("Podaj pseudonim przestępcy: ")
        id_sprawy = input("Podaj ID sprawy, do której przypisany jest przestępca: ")
        append_przestepca(imie_nazwisko, pseudonim, id_sprawy)

    elif choice == '6':
        # Dodaj nowe aresztowanie
        id_funkcjonariusza = input("Podaj ID funkcjonariusza: ")
        id_przestepcy = input("Podaj ID przestępcy: ")
        id_sprawy = input("Podaj ID sprawy: ")
        data_aresztowania = input("Podaj datę aresztowania (w formacie RRRR-MM-DD): ")
        append_aresztowanie(id_funkcjonariusza, id_przestepcy, id_sprawy, data_aresztowania)

    elif choice == '7':
        # Dodaj nowe miejsce
        nazwa_miejsca = input("Podaj nazwę miejsca: ")
        opis = input("Podaj opis miejsca: ")
        append_miejsce(nazwa_miejsca, opis)

    elif choice == '8':
        # Dodaj nowy patrol
        id_funkcjonariusza = input("Podaj ID funkcjonariusza: ")
        data_patrolu = input("Podaj datę patrolu (w formacie RRRR-MM-DD): ")
        append_patrol(id_funkcjonariusza, data_patrolu)

    elif choice == '9':
        # Dodaj nowe wykroczenie
        opis = input("Podaj opis wykroczenia: ")
        id_sprawy = input("Podaj ID sprawy, do której przypisane jest wykroczenie: ")
        append_wykroczenie(opis, id_sprawy)

    elif choice == '10':
        # Dodaj nową ofiarę
        imie_nazwisko = input("Podaj imię i nazwisko ofiary: ")
        id_sprawy = input("Podaj ID sprawy, do której przypisana jest ofiara: ")
        append_ofiara(imie_nazwisko, id_sprawy)

    elif choice == '11':
        # Dodaj nowego poszukiwanego
        imie_nazwisko = input("Podaj imię i nazwisko poszukiwanego: ")
        nagroda = input("Podaj nagrodę (w złotych): ")
        append_poszukiwany(imie_nazwisko, nagroda)

    elif choice == '12':
        # Dodaj nową nagrodę
        id_poszukiwanego = input("Podaj ID poszukiwanego: ")
        kwota = input("Podaj kwotę nagrody (w złotych): ")
        append_nagroda(id_poszukiwanego, kwota)

    elif choice == '13':
        # Dodaj nową interwencję
        id_sprawy = input("Podaj ID sprawy: ")
        id_funkcjonariusza = input("Podaj ID funkcjonariusza: ")
        data_interwencji = input("Podaj datę interwencji (w formacie RRRR-MM-DD): ")
        append_interwencja(id_sprawy, id_funkcjonariusza, data_interwencji)

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
