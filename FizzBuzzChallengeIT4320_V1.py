for testVar in range(1,101):
    if testVar % 3 == 0 and testVar % 5 == 0:
        print("fizzbuzz")
    elif testVar % 3 == 0:
        print("fizz")
    elif testVar % 5 == 0:
        print("buzz")
    else:
        print(testVar)
