day = 'Saturday'
temp = 30
raining = True

if (day == 'Saturday' and temp > 23) or not raining:
    print("Go swimming")
else:
    print("learn python")

# checkingin

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
