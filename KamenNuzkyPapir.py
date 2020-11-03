#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import modulu pro využití funkce random
import random

#Import modulu pro rozpoznání operačního systému
from os import system, name

# Nastavení počtu výher a proher při startu hry
vyhra = 0
prohra = 0
remiza = 0


# Vyčištění konzole
def uklid():
    if name == 'nt':        # Pro vyčištění windows konzole
        _ = system('cls')
    else:                   # Pro vyčištění Linux a MacOS konzole
        _ = system('clear')


#Zobrazení základního menu hry a nsáledné přesměrování dle vybrané volby
def menu_info():
    uklid()
    print("\nKámen nůžky papír")
    print("\n--------------------------")
    print(" 1. Zobrazit pravidla hry \n 2. Spustit hru \n 3. Ukončit program")
    print("--------------------------\n")
    try:
        menu = int(input("Vyberte si volbu: "))
    except:
        uklid()
        print("Byl zadán nesprávný výběr!")
        menu_info()
    if menu < 1 or menu > 3:
        uklid()
        print("Vyberte si prosím z možností 1-3!")
        menu_info()
    elif menu == 1:
        uklid()
        print("------------------------")
        print("Kámen otupí nůžky")
        print("Nůžky přestřihnou papír")
        print("Papír obalí kámen")
        print("------------------------\n")
        pokracovani = input("Přejete si hrát hru? (Ano/Ne): ")
        if pokracovani == "Ano":
            uklid()
            hra()
        elif pokracovani == "Ne":
            uklid()
            print("\nZavírám aplikaci...\n")
            ukonceni_hry()
        else:
            uklid()
            print("Byl zadán nesprávný výběr!")
            menu_info()

    elif menu == 2:
        uklid()
        hra()
    else:
        uklid()
        print("\nZavírám aplikaci...\n")
        ukonceni_hry()


# Ukončení hry
def ukonceni_hry():
    quit()


# Zobrazení dostupných voleb pro nástroj
def vyber_volby():
    print("\n 1.Kámen \n 2.Nůžky \n 3.Papír \n")


# Závěrečné menu po výhře/prohře
def zaver():
    hrat_znovu = input("Přejete si hrát znovu? (Ano/Ne): ")
    if hrat_znovu == "Ano":
        uklid()
        hra()
    elif hrat_znovu == "Ne":
        uklid()
        print("\nVaše výsledné skóre je:")
        print("----------------")
        print("Počet výher: " + str(vyhra))
        print("Počet proher: " + str(prohra))
        print("Počet remíz: " + str(remiza))
        print("----------------")
        print("\nZavírám aplikaci...\n")
        ukonceni_hry()
    else:
        uklid()
        print("Byl zadán nesprávný výběr!")
        zaver()


# Daný mechanismus hry
def hra():
    global vyhra
    global prohra
    global remiza
    vyber_volby()
    try:
        vyber = int(input("Zadejte vaší volbu: "))
    except:
        uklid()
        print("Byl zadán nesprávný výběr!")
        hra()
    if vyber < 1 or vyber > 3:
        print("Vyberte si prosím z možností 1-3!")
        hra()
    elif vyber == 1:
        nastroj = "kámen"
    elif vyber == 2:
        nastroj = "nůžky"
    else:
        nastroj = "papír"

    pocitac_vyber = random.randint(1, 3)
    if pocitac_vyber == 1:
        pocitac_nastroj = "kámen"
    elif pocitac_vyber == 2:
        pocitac_nastroj = "nůžky"
    else:
        pocitac_nastroj = "papír"

    uklid()
    print("\nVybral jste si " + nastroj)
    print("Počítač vybral " + pocitac_nastroj)

    if (vyber == 1 and pocitac_vyber == 3) or (vyber == 3 and pocitac_vyber == 1):
        vysledek = "papír"
    elif (vyber == 1 and pocitac_vyber == 2) or (vyber == 2 and pocitac_vyber == 1):
        vysledek = "kámen"
    else:
        vysledek = "nůžky"

    if vyber == pocitac_vyber:
        print("\n------")
        print("Remíza")
        print("------\n")
        remiza = remiza + 1
    else:
        if vysledek == nastroj:
            print("\n----------------------")
            print("Vyhrál jste, gratuluji")
            print("----------------------\n")
            vyhra = vyhra + 1
        else:
            print("\n-----------------------------------")
            print("Vyhrál počítač, hodně štěstí příště")
            print("-----------------------------------\n")
            prohra = prohra + 1
    zaver()


menu_info()