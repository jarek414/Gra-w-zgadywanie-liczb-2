import random


def Gra_w_zgadywanie_liczb_2():
    while True:
        try:
            your_number = int(input(" Pomysl liczbe od 0 do 1000 a ja ja zgadne w max 10 probach: "))
            break
        except ValueError:
            print("to ni jest liczba")

    min = 0
    max = 1000
    set = 11
    for computers_turne in range(1, set):
        guess = int((max - min) / 2) + min
        print(guess)
        user_clue = input("""czy liczba podana przez komputer to toja liczba? """)
        if user_clue == "tak":
            break
        elif user_clue == "nie":
            user_clue_2 = input("""czy liczba podana przez komputer jest za mala? """)
            if user_clue_2 == "tak":
                min = guess
            elif user_clue_2 == "nie":
                user_clue_3 = input("""czy liczba podana przez komputer jest za duza? """)
                if user_clue_3 == "tak":
                    max = guess
                else:
                    print("nie oszukuj")
                    set += 1

    return f"wygrales moja liczba to {your_number} "



if __name__ == '__main__':
    print(Gra_w_zgadywanie_liczb_2())
