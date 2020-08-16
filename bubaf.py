for x in range(1,101):
    if (x % 3 == 0):
        if (x % 5 == 0):
            print("bu baf")
        else:
            print("bu")
    elif (x % 5 == 0):
        print("baf")
    else:
        print(x)
