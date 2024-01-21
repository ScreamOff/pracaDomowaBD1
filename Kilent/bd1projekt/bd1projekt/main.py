from append import *
from bd1projekt.wyswietlanie import *
from update import *
from delete import *

def display_menu():
    print("Wybierz opcję:")
    print("(A)ppend")
    print("(U)pdate")
    print("(D)elete")
    print("(W)yświetl")
    print("(Q)uit")

def display_wyswietl_options():
    print("Wybierz opcję do wyświetlenia:")
    print("(1) Lista Funkcjonariuszy")
    print("(2) Lista Jednostek")
    print("(3) Lista Spraw")
    print("(4) Lista Dowodów")
    print("(5) Lista Przestępców")
    print("(6) Lista Aresztowań")
    print("(7) Lista Miejsc")
    print("(8) Lista Patroli")
    print("(9) Lista Wykroczeń")
    print("(10) Lista Ofiar")
    print("(11) Lista Poszukiwanych")
    print("(12) Lista Nagród")
    print("(13) Lista Interwencji")

def display_append_options():
    print("Wybierz opcję do dodania:")
    print("(1) dodaj Funkcjonariuszy")
    print("(2) dodaj Jednostek")
    print("(3) dodaj Spraw")
    print("(4) dodaj Dowodów")
    print("(5) dodaj Przestępców")
    print("(6) dodaj Aresztowań")
    print("(7) dodaj Miejsc")
    print("(8) dodaj Patroli")
    print("(9) dodaj Wykroczeń")
    print("(10) dodaj Ofiar")
    print("(11) dodaj Poszukiwanych")
    print("(12) dodaj Nagród")
    print("(13) dodaj Interwencji")

def display_delete_options():
    print("Wybierz opcję do dodania:")
    print("(1) usun Funkcjonariuszy")
    print("(2) usun Jednostek")
    print("(3) usun Spraw")
    print("(4) usun Dowodów")
    print("(5) usun Przestępców")
    print("(6) usun Aresztowań")
    print("(7) usun Miejsc")
    print("(8) usun Patroli")
    print("(9) usun Wykroczeń")
    print("(10) usun Ofiar")
    print("(11) usun Poszukiwanych")
    print("(12) usun Nagród")
    print("(13) usun Interwencji")

def display_update_options():
    print("Wybierz opcję do dodania:")
    print("(1) zmien Funkcjonariuszy")
    print("(2) zmien Jednostek")
    print("(3) zmien Spraw")
    print("(4) zmien Dowodów")
    print("(5) zmien Przestępców")
    print("(6) zmien Aresztowań")
    print("(7) zmien Miejsc")
    print("(8) zmien Patroli")
    print("(9) zmien Wykroczeń")
    print("(10) zmien Ofiar")
    print("(11) zmien Poszukiwanych")
    print("(12) zmien Nagród")
    print("(13) zmien Interwencji")
def main():
    while True:
        display_menu()
        choice = input("Twój wybór: ").upper()

        if choice == 'A':
            # Menu append
            print("Wybrałeś opcję (A)ppend.")
            display_append_options()
            display_choice = input("Twój wybór: ")
            append_data(display_choice)
        elif choice == 'U':
            # Menu update
            print("Wybrałeś opcję (U)pdate.")
            display_update_options()
            display_choice = input("Twój wybór: ")
            update_data(display_choice)

        elif choice == 'D':
            # Menu delete
            print("Wybrałeś opcję (D)elete.")
            display_delete_options()
            display_choice = input("Twój wybór:")
            delete_data(display_choice)
        elif choice == 'W':
            # Menu wyświetl
            print("Wybrałeś opcję (W)yświetl.")
            display_wyswietl_options()
            display_choice = input("Twój wybór: ")
            display_list(display_choice);
            break
        elif choice == 'Q':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
