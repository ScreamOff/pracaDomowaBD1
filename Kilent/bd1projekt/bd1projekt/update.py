import sqlite3

def update_funkcjonariusz(id_funkcjonariusza, imie, nazwisko, stopien, numer_legitymacji):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj funkcjonariusza
    cursor.execute("UPDATE Funkcjonariusz SET imie=?, nazwisko=?, stopien=?, numer_legitymacji=? WHERE id_funkcjonariusza=?",
                   (imie, nazwisko, stopien, numer_legitymacji, id_funkcjonariusza))

    connection.commit()
    connection.close()

def update_jednostka(id_jednostki, nazwa, lokalizacja, id_funkcjonariusza):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj jednostkę
    cursor.execute("UPDATE Jednostka SET nazwa=?, lokalizacja=?, id_funkcjonariusza=? WHERE id_jednostki=?",
                   (nazwa, lokalizacja, id_funkcjonariusza, id_jednostki))

    connection.commit()
    connection.close()

def update_sprawa(id_sprawy, opis, status, id_jednostki):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj sprawę
    cursor.execute("UPDATE Sprawa SET opis=?, status=?, id_jednostki=? WHERE id_sprawy=?",
                   (opis, status, id_jednostki, id_sprawy))

    connection.commit()
    connection.close()

def update_dowod(id_dowodu, opis, id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj dowód
    cursor.execute("UPDATE Dowod SET opis=?, id_sprawy=? WHERE id_dowodu=?",
                   (opis, id_sprawy, id_dowodu))

    connection.commit()
    connection.close()

def update_przestepca(id_przestepcy, imie_nazwisko, pseudonim, id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj przestępcę
    cursor.execute("UPDATE Przestepca SET imie_nazwisko=?, pseudonim=?, id_sprawy=? WHERE id_przestepcy=?",
                   (imie_nazwisko, pseudonim, id_sprawy, id_przestepcy))

    connection.commit()
    connection.close()

def update_aresztowanie(id_aresztowania, id_funkcjonariusza, id_przestepcy, id_sprawy, data_aresztowania):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj aresztowanie
    cursor.execute("UPDATE Aresztowanie SET id_funkcjonariusza=?, id_przestepcy=?, id_sprawy=?, data_aresztowania=? WHERE id_aresztowania=?",
                   (id_funkcjonariusza, id_przestepcy, id_sprawy, data_aresztowania, id_aresztowania))

    connection.commit()
    connection.close()

def update_miejsce(id_miejsca, nazwa_miejsca, opis):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj miejsce
    cursor.execute("UPDATE Miejsce SET nazwa_miejsca=?, opis=? WHERE id_miejsca=?",
                   (nazwa_miejsca, opis, id_miejsca))

    connection.commit()
    connection.close()

def update_patrol(id_patrolu, id_funkcjonariusza, data_patrolu):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj patrol
    cursor.execute("UPDATE Patrol SET id_funkcjonariusza=?, data_patrolu=? WHERE id_patrolu=?",
                   (id_funkcjonariusza, data_patrolu, id_patrolu))

    connection.commit()
    connection.close()

def update_wykroczenie(id_wykroczenia, opis, id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj wykroczenie
    cursor.execute("UPDATE Wykroczenie SET opis=?, id_sprawy=? WHERE id_wykroczenia=?",
                   (opis, id_sprawy, id_wykroczenia))

    connection.commit()
    connection.close()

def update_ofiara(id_ofiary, imie_nazwisko, id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj ofiarę
    cursor.execute("UPDATE Ofiara SET imie_nazwisko=?, id_sprawy=? WHERE id_ofiary=?",
                   (imie_nazwisko, id_sprawy, id_ofiary))

    connection.commit()
    connection.close()

def update_poszukiwany(id_poszukiwanego, imie_nazwisko, nagroda):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj poszukiwanego
    cursor.execute("UPDATE Poszukiwany SET imie_nazwisko=?, nagroda=? WHERE id_poszukiwanego=?",
                   (imie_nazwisko, nagroda, id_poszukiwanego))

    connection.commit()
    connection.close()

def update_nagroda(id_nagrody, id_poszukiwanego, kwota):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj nagrodę
    cursor.execute("UPDATE Nagroda SET id_poszukiwanego=?, kwota=? WHERE id_nagrody=?",
                   (id_poszukiwanego, kwota, id_nagrody))

    connection.commit()
    connection.close()

def update_interwencja(id_interwencji, id_sprawy, id_funkcjonariusza, data_interwencji):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Zaktualizuj interwencję
    cursor.execute("UPDATE Interwencja SET id_sprawy=?, id_funkcjonariusza=?, data_interwencji=? WHERE id_interwencji=?",
                   (id_sprawy, id_funkcjonariusza, data_interwencji, id_interwencji))

    connection.commit()
    connection.close()

def update_data(choice):
    if choice == '1':
        # Aktualizuj funkcjonariusza
        id_funkcjonariusza = input("Podaj ID funkcjonariusza do aktualizacji: ")
        imie = input("Nowe imię: ")
        nazwisko = input("Nowe nazwisko: ")
        stopien = input("Nowy stopień: ")
        numer_legitymacji = input("Nowy numer legitymacji: ")
        update_funkcjonariusz(id_funkcjonariusza, imie, nazwisko, stopien, numer_legitymacji)

    elif choice == '2':
        # Aktualizuj jednostkę
        id_jednostki = input("Podaj ID jednostki do aktualizacji: ")
        nazwa = input("Nowa nazwa: ")
        lokalizacja = input("Nowa lokalizacja: ")
        id_funkcjonariusza = input("Nowe ID funkcjonariusza: ")
        update_jednostka(id_jednostki, nazwa, lokalizacja, id_funkcjonariusza)

    elif choice == '3':
        # Aktualizuj sprawę
        id_sprawy = input("Podaj ID sprawy do aktualizacji: ")
        opis = input("Nowy opis sprawy: ")
        status = input("Nowy status sprawy: ")
        id_jednostki = input("Nowe ID jednostki: ")
        update_sprawa(id_sprawy, opis, status, id_jednostki)

    elif choice == '4':
        # Aktualizuj dowód
        id_dowodu = input("Podaj ID dowodu do aktualizacji: ")
        opis = input("Nowy opis dowodu: ")
        id_sprawy = input("Nowe ID sprawy: ")
        update_dowod(id_dowodu, opis, id_sprawy)

    elif choice == '5':
        # Aktualizuj przestępcę
        id_przestepcy = input("Podaj ID przestępcy do aktualizacji: ")
        imie_nazwisko = input("Nowe imię i nazwisko przestępcy: ")
        pseudonim = input("Nowy pseudonim przestępcy: ")
        id_sprawy = input("Nowe ID sprawy: ")
        update_przestepca(id_przestepcy, imie_nazwisko, pseudonim, id_sprawy)

    # Kontynuuj dla pozostałych tabel...

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
