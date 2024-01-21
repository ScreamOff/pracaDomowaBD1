import sqlite3

# Otwórz plik z definicją struktury bazy danych
with open('struktura_bazy.txt', 'r') as file:
    sql_script = file.read()

# Utwórz połączenie do bazy danych (lub stwórz nową bazę danych)
connection = sqlite3.connect('moja_baza.db')

# Utwórz kursor
cursor = connection.cursor()

# Wykonaj zapytania SQL z pliku
cursor.executescript(sql_script)

# Zatwierdź zmiany
connection.commit()

# Zamknij kursor i połączenie
cursor.close()
connection.close()

print("Baza danych utworzona pomyślnie.")
