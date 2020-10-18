from random import randrange
skore = 0
while skore <= 21:
    print("Tvoje skóre je:", skore)
    odpoved = input("Chceš pokračovat? Odpověz ano/ne: ")
    if (odpoved == "ano") or (odpoved == "Ano"):
        karta = randrange(2,11)
        print("Přišla ti karta s hodnotou", karta)
        skore = skore + karta
    else:
        break
print("Konec hry. Tvoje skóre je:", skore)
if skore > 21:
    print("Prohrál/a jsi.")
