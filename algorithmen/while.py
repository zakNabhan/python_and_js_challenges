#while
i = 1
while i<6:
    print(i)
    i+=1
print("___________________")
# the break statement
x = 1
while x<6:
    print(x)
    if x==3:
        break
    x=x+1


# continue statement
# continue to the next iteration if y is 3
print("___________________")

y = 0
while y < 6:
    y +=1
    if y==3:
        continue
    print(y)



# while example to choice a function
#define first the functions

def printname():
    print("my namen ist zakaria")


def printalter():
    print("my alter ist 25")

def printnote():
    print("my adresse ist Frankfurt")


def printadresse():
    print("my Note ist 1")

#set an initial value for choice other
#than the value for "beenden" (be)
choice = ""
while choice !="be":
    # Give all the choices in a series of print statements.
    print("\n Geben Sie 1 deine Name auszugeben: ")
    print("\n Geben Sie 2 deine Alter auszugeben: ")
    print("\n Geben Sie 3 deine Adresse auszugeben: ")
    print("\n Geben Sie 4 deine Note auszugeben: ")

    # Respond to the user's choice.

    # Ask for the user's choice.
    choice = input("\nWas haben Sie Vor? ")
    if choice == '1':
        printname()
    elif choice == '2':
        printalter()
    elif choice == '3':
        printnote()
    elif choice == '4':
        printadresse()
    elif choice == 'be':
        print("\nVielen Danke.\n")
    else:
        print("\nVersuchen es nochmal.\n")
