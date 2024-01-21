import string
import random
from datetime import datetime
from append import *
def imie():
    a = ""
    for i in range(10):
        a +=(random.choice(string.ascii_uppercase))
    return a

def stopien():
    stopien = ["sierżant","major","general"]
    return random.choice(stopien)

def random_status():
    status = ["w trakcie","zakonczona"]
    return random.choice(status)
def miejsce():
    miasto = ["Warszawa", "Krakow", "Kielce", "Gdansk", "Poznan"]
    return random.choice(miasto)

def random_date():
    # Losowo wybieramy rok z zakresu 2000-2022
    year = random.randint(2000, 2024)
    # Losowo wybieramy miesiąc
    month = random.randint(1, 12)
    # Losowo wybieramy dzień
    day = random.randint(1, 28)  # Zakładamy, że każdy miesiąc ma maksymalnie 28 dni

    date_obj = datetime(year, month, day)
    sqlite_date = date_obj.strftime("%Y-%m-%d")
    return sqlite_date;

def random_numer():
    return random.randint(1000000, 99999999)

def random_nagroda():
    nagroda = random.randint(100,5000)
    return nagroda


#print(random_nagroda())

#alphabet = "qwertyuiopasdfghjklzxcvbnm"



for i in range(1,11):

    append_funkcjonariusz(imie(), imie(), stopien(), random_date())
    append_jednostka(imie(), miejsce(), i)
    append_sprawa(imie(), random_status(), i)
    append_dowod(imie(), i)
    append_przestepca(imie(), imie(), i)
    append_aresztowanie(i, i, i, random_date())
    append_miejsce(miejsce(), imie())
    append_patrol(i, random_date())
    append_wykroczenie(imie(), i)
    append_poszukiwany(imie(), random_nagroda())
    append_interwencja(i, i, random_date())
    append_nagroda(i, random_nagroda())