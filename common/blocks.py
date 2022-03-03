for i in range(1, 13):
    print("No. {} squared is {} and cuded is{:4} ".format(i, i ** 2, i ** 3))
    # print("*" * 80)

print("*" * 80)

name = input("please enter your name: ".upper())
age = int(input("How old are you, {0}:? ".format(name).upper()))

if age < 18:
    print("Please come back in {} years".format(18 - age))
elif age == 900:
    print("Sorry, {} , you die in Return of ...".format(name))
else:
    print("you are old enough to vote")
    print("pleas put an X in the box")

# conditon example
age = int(input("How old are you? "))

if age >= 16 and age <= 65:
    print("Have a good day at work")


# or

if 16 <= age <= 65:
    print("have a good day at work")
else:
    print("enjoy free time")

print("-"*60)
