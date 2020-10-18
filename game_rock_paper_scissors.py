import random
random_word_list = ["kámen", "nůžky", "papír"]
tah_pocitace = random.choice(random_word_list) 
tah_hrace = input("Zadej svůj tah: ")
if tah_hrace == "kámen":
    if tah_pocitace == "kámen":
        print('Remíza!')
    if tah_pocitace == "nůžky":
        print('Vyhrála jsi!')
    if tah_pocitace == "papír":
        print('Prohrála jsi!')
elif tah_hrace == "nůžky":
    if tah_pocitace == "kámen":
        print('Prohrála jsi!')
    if tah_pocitace == "nůžky":
        print('Remíza!')
    if tah_pocitace == "papír":
        print('Vyhrála jsi!')
elif tah_hrace == "papír":
    if tah_pocitace == "kámen":
        print('Vyhrála jsi!')
    if tah_pocitace == "nůžky":
        print('Prohrála jsi!')
    if tah_pocitace == "papír":
        print('Remíza!')
else:
    print("Promiň, ale znám pouze slova: kámen, nůžky, papír.")
