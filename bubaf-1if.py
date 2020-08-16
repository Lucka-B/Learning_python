for x in range(1,101):
    if (x % 3 == 0) and (x % 5 == 0):
        print("bu baf")
    elif (x % 3 == 0):
        print("bu")
    elif (x % 5 == 0):
        print("baf")
    else:
        print(x)
