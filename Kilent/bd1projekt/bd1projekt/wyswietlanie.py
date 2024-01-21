import sqlite3

def get_all_funkcjonariusze():
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Funkcjonariusz")
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_jednostki():
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Jednostka")
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_sprawy():
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Sprawa")
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_dowody_by_sprawa(id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Dowod WHERE id_sprawy=?", (id_sprawy,))
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_przestepcy_by_sprawa(id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Przestepca WHERE id_sprawy=?", (id_sprawy,))
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_aresztowania():
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Aresztowanie")
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_miejsca():
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Miejsce")
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_patrole():
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Patrol")
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_wykroczenia_by_sprawa(id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Wykroczenie WHERE id_sprawy=?", (id_sprawy,))
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_ofiary_by_sprawa(id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Ofiara WHERE id_sprawy=?", (id_sprawy,))
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_poszukiwani():
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Poszukiwany")
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_nagrody_by_poszukiwany(id_poszukiwanego):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Nagroda WHERE id_poszukiwanego=?", (id_poszukiwanego,))
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_interwencje():
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Interwencja")
    result = cursor.fetchall()
    connection.close()
    return result

def display_list(choice):
    if choice == '1':
        # Wyświetl listę funkcjonariuszy
        funkcjonariusze = get_all_funkcjonariusze()
        print("\nLista Funkcjonariuszy:")
        for funkcjonariusz in funkcjonariusze:
            print(funkcjonariusz)

    elif choice == '2':
        # Wyświetl listę jednostek
        jednostki = get_all_jednostki()
        print("\nLista Jednostek:")
        for jednostka in jednostki:
            print(jednostka)

    elif choice == '3':
        # Wyświetl listę spraw
        sprawy = get_all_sprawy()
        print("\nLista Spraw:")
        for sprawa in sprawy:
            print(sprawa)

    elif choice == '4':
        # Wyświetl listę dowodów
        id_sprawy = input("Podaj ID sprawy: ")
        dowody = get_all_dowody_by_sprawa(id_sprawy)
        print("\nLista Dowodów:")
        for dowod in dowody:
            print(dowod)

    elif choice == '5':
        # Wyświetl listę przestępców
        id_sprawy = input("Podaj ID sprawy: ")
        przestepcy = get_all_przestepcy_by_sprawa(id_sprawy)
        print("\nLista Przestępców:")
        for przestepca in przestepcy:
            print(przestepca)

    elif choice == '6':
        # Wyświetl listę aresztowań
        aresztowania = get_all_aresztowania()
        print("\nLista Aresztowań:")
        for aresztowanie in aresztowania:
            print(aresztowanie)

    elif choice == '7':
        # Wyświetl listę miejsc
        miejsca = get_all_miejsca()
        print("\nLista Miejsc:")
        for miejsce in miejsca:
            print(miejsce)

    elif choice == '8':
        # Wyświetl listę patroli
        patrole = get_all_patrole()
        print("\nLista Patroli:")
        for patrol in patrole:
            print(patrol)

    elif choice == '9':
        # Wyświetl listę wykroczeń
        id_sprawy = input("Podaj ID sprawy: ")
        wykroczenia = get_all_wykroczenia_by_sprawa(id_sprawy)
        print("\nLista Wykroczeń:")
        for wykroczenie in wykroczenia:
            print(wykroczenie)

    elif choice == '10':
        # Wyświetl listę ofiar
        id_sprawy = input("Podaj ID sprawy:")
        ofiary = get_all_ofiary_by_sprawa(id_sprawy)
        print("\nLista Ofiar:")
        for ofiara in ofiary:
            print(ofiara)

    elif choice == '11':
        # Wyświetl listę poszukiwanych
        poszukiwani = get_all_poszukiwani()
        print("\nLista Poszukiwanych:")
        for poszukiwany in poszukiwani:
            print(poszukiwany)

    elif choice == '12':
        # Wyświetl listę nagród
        id_poszukiwanego = input("Podaj ID poszukiwanego")
        nagrody = get_all_nagrody_by_poszukiwany(id_poszukiwanego)
        print("\nLista Nagród:")
        for nagroda in nagrody:
            print(nagroda)

    elif choice == '13':
        # Wyświetl listę interwencji
        interwencje = get_all_interwencje()
        print("\nLista Interwencji:")
        for interwencja in interwencje:
            print(interwencja)

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
