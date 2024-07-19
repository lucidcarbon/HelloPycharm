weight = input("What is your weight: ")
units = input ("(K)g or (L)bs? ")

if units.upper() == "K":
    ## do the stuff to convert kg to lbs
    pounds = float(weight) * 2.2
    print ("Your weight in pounds is " + str(pounds))
    print ("right here")
elif units.upper() == "L":
    kilos = float(weight) / 2.2
    print("Your weight in kilos: " + str(kilos))
    ## do the convert lbs to kg
else:
    print("Incorrect unit choice.")