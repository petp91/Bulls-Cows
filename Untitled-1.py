"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Přibyl
email: petrpribyl91@outlook.com
"""
import random
import time

# Funkce na generování náhodného čísla
def generuj_cislo():
    cisla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        nahodna_cisla = random.sample(cisla, 4)
        nahodna_cisla = "".join(map(str, nahodna_cisla))
        if nahodna_cisla[0] != "0":  # Zajistíme, že číslo nezačíná 0
            return nahodna_cisla

# Funkce pro dynamické generování čáry
def generuj_caru(texty, minimalni_delka=47):
    nejdelsi_text = max(len(text) for text in texty)
    delka_cary = max(minimalni_delka, nejdelsi_text)
    return "-" * delka_cary

# Uchování statistik
statistiky = []

while True:
    # Texty pro generování čáry
    texty = [
        "Hi there!",
        "I've generated a random 4 digit number for you.",
        "Let's play a bulls and cows game.",
        "Enter a number:",
        "Correct, you've guessed the right number in 4 guesses!",
        "That's amazing!"
    ]
    cara = generuj_caru(texty)

    # Nastavení hry
    nahodna_cisla = generuj_cislo()
    pocet_odhadu = 0

    print("Hi there!")
    print(cara)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(cara)

    # Měření času
    start_cas = time.time()

    while True:
        # Uživatelský vstup
        vstup_uzivatele = input("Enter a number:\n" + cara + "\n>>> ")

        # Ověření platnosti vstupu
        if not vstup_uzivatele.isdigit() or len(vstup_uzivatele) != 4:
            print("Invalid input! Please enter a 4-digit number.")
            print(cara)
            continue

        # Počet odhadů
        pocet_odhadu += 1

        # Porovnání čísel
        bulls = 0
        cows = 0
        for i in range(4):
            if vstup_uzivatele[i] == nahodna_cisla[i]:
                bulls += 1
            elif vstup_uzivatele[i] in nahodna_cisla:
                cows += 1

        # Výstup výsledků
        if bulls == 1:
            bulls_text = "1 bull"
        else:
            bulls_text = f"{bulls} bulls"

        if cows == 1:
            cows_text = "1 cow"
        else:
            cows_text = f"{cows} cows"

        print(f"{bulls_text}, {cows_text}")
        print(cara)

        # Konec hry
        if bulls == 4:
            end_cas = time.time()
            cas_hry = end_cas - start_cas
            print(f"Correct, you've guessed the right number\nin {pocet_odhadu} guesses!")
            print(cara)
            if pocet_odhadu <= 5:
                print("That's amazing!")
            elif pocet_odhadu <= 10:
                print("Well done!")
            else:
                print("Good job!")

            # Ulož statistiku
            statistiky.append({"odhad": pocet_odhadu, "cas": round(cas_hry, 2)})
            break

    # Zobrazit statistiky
    print("\nGame Statistics:")
    for index, hra in enumerate(statistiky, start=1):
        print(f"Game {index}: {hra['odhad']} guesses, {hra['cas']} seconds")
    print(cara)

    # Dotaz na další hru
    dalsi_hra = input("Do you want to play again? (yes/no): ").strip().lower()
    if dalsi_hra != "yes":
        print("Thanks for playing! Goodbye!")
        break