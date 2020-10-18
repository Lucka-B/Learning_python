for i in range(5):
    kandidat = int(input("Zadej prosím číslo: "))
    if i == 0 or kandidat < minimum:
        minimum = kandidat

print("Nejmenší číslo je", minimum)
