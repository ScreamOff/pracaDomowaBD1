import sqlite3

def delete_funkcjonariusz(id_funkcjonariusza):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń funkcjonariusza
    cursor.execute("DELETE FROM Funkcjonariusz WHERE id_funkcjonariusza=?", (id_funkcjonariusza,))

    connection.commit()
    connection.close()

def delete_jednostka(id_jednostki):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń jednostkę
    cursor.execute("DELETE FROM Jednostka WHERE id_jednostki=?", (id_jednostki,))

    connection.commit()
    connection.close()

def delete_sprawa(id_sprawy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń sprawę
    cursor.execute("DELETE FROM Sprawa WHERE id_sprawy=?", (id_sprawy,))

    connection.commit()
    connection.close()

def delete_dowod(id_dowodu):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń dowód
    cursor.execute("DELETE FROM Dowod WHERE id_dowodu=?", (id_dowodu,))

    connection.commit()
    connection.close()

def delete_przestepca(id_przestepcy):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń przestępcę
    cursor.execute("DELETE FROM Przestepca WHERE id_przestepcy=?", (id_przestepcy,))

    connection.commit()
    connection.close()

def delete_aresztowanie(id_aresztowania):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń aresztowanie
    cursor.execute("DELETE FROM Aresztowanie WHERE id_aresztowania=?", (id_aresztowania,))

    connection.commit()
    connection.close()

def delete_miejsce(id_miejsca):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń miejsce
    cursor.execute("DELETE FROM Miejsce WHERE id_miejsca=?", (id_miejsca,))

    connection.commit()
    connection.close()

def delete_patrol(id_patrolu):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń patrol
    cursor.execute("DELETE FROM Patrol WHERE id_patrolu=?", (id_patrolu,))

    connection.commit()
    connection.close()

def delete_wykroczenie(id_wykroczenia):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń wykroczenie
    cursor.execute("DELETE FROM Wykroczenie WHERE id_wykroczenia=?", (id_wykroczenia,))

    connection.commit()
    connection.close()

def delete_ofiara(id_ofiary):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń ofiarę
    cursor.execute("DELETE FROM Ofiara WHERE id_ofiary=?", (id_ofiary,))

    connection.commit()
    connection.close()

def delete_poszukiwany(id_poszukiwanego):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń poszukiwanego
    cursor.execute("DELETE FROM Poszukiwany WHERE id_poszukiwanego=?", (id_poszukiwanego,))

    connection.commit()
    connection.close()

def delete_nagroda(id_nagrody):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń nagrodę
    cursor.execute("DELETE FROM Nagroda WHERE id_nagrody=?", (id_nagrody,))

    connection.commit()
    connection.close()

def delete_interwencja(id_interwencji):
    connection = sqlite3.connect('moja_baza.db')
    cursor = connection.cursor()

    # Usuń interwencję
    cursor.execute("DELETE FROM Interwencja WHERE id_interwencji=?", (id_interwencji,))

    connection.commit()
    connection.close()

def delete_data(choice):
    if choice == '1':
        # Usuń funkcjonariusza
        id_funkcjonariusza = input("Podaj ID funkcjonariusza do usunięcia: ")
        delete_funkcjonariusz(id_funkcjonariusza)

    elif choice == '2':
        # Usuń jednostkę
        id_jednostki = input("Podaj ID jednostki do usunięcia: ")
        delete_jednostka(id_jednostki)

    elif choice == '3':
        # Usuń sprawę
        id_sprawy = input("Podaj ID sprawy do usunięcia: ")
        delete_sprawa(id_sprawy)

    elif choice == '4':
        # Usuń dowód
        id_dowodu = input("Podaj ID dowodu do usunięcia: ")
        delete_dowod(id_dowodu)

    elif choice == '5':
        # Usuń przestępcę
        id_przestepcy = input("Podaj ID przestępcy do usunięcia: ")
        delete_przestepca(id_przestepcy)

    elif choice == '6':
        # Usuń aresztowanie
        id_aresztowania = input("Podaj ID aresztowania do usunięcia: ")
        delete_aresztowanie(id_aresztowania)

    elif choice == '7':
        # Usuń miejsce
        id_miejsca = input("Podaj ID miejsca do usunięcia: ")
        delete_miejsce(id_miejsca)

    elif choice == '8':
        # Usuń patrol
        id_patrolu = input("Podaj ID patrolu do usunięcia: ")
        delete_patrol(id_patrolu)

    elif choice == '9':
        # Usuń wykroczenie
        id_wykroczenia = input("Podaj ID wykroczenia do usunięcia: ")
        delete_wykroczenie(id_wykroczenia)

    elif choice == '10':
        # Usuń ofiarę
        id_ofiary = input("Podaj ID ofiary do usunięcia: ")
        delete_ofiara(id_ofiary)

    elif choice == '11':
        # Usuń poszukiwanego
        id_poszukiwanego = input("Podaj ID poszukiwanego do usunięcia: ")
        delete_poszukiwany(id_poszukiwanego)

    elif choice == '12':
        # Usuń nagrodę
        id_nagrody = input("Podaj ID nagrody do usunięcia: ")
        delete_nagroda(id_nagrody)

    elif choice == '13':
        # Usuń interwencję
        id_interwencji = input("Podaj ID interwencji do usunięcia: ")
        delete_interwencja(id_interwencji)

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
