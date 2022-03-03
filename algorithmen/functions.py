# to get the functions of python in console
# first step python eingeben
#second step dir()
#third step dir("")

print("a simple function")

def happybirthday():
    print("alles gute zum Geburtstag")
    print("alles gute zum Geburtstag")
    print("alles gute zum Geburtstag")

#call the function now
happybirthday()

def printname(str):
    print(str)

print("successfull")

# call function with arguments
def myfunction(name, alter):
    print("___________________")
    print("your name: ", name)
    print("your alter: ", alter)
    print("___________________")

myfunction("Zakaria", 25)
myfunction("Test", 25)

# if you do not know how many arguments that will be passed
# into your function, add a * before the paramter name in the function
# Arbitrary Argument, *args

def mykinder(*kinder):
    print("the youngest Kind: "+ kinder[1])
    for k in kinder:
        print("name "+ k)


mykinder("zakaria", "test", "ahmed", "test2")


# Keywords arguments
# you can also send argument with the Key=Value syntax

def function(note_1, note_2, note_3):
    print("schlicht "+note_3)

function(note_1="sehr gut",note_2="gut",note_3="befriedigung")


# if the number of  keyword arguments is onknown, add a
# double ** before the parameter Name

def myfunc(**noten):
    print("beste note "+ noten["note_1"])

myfunc(note_1="sehr gut",note_2="gut",note_3="befriedigung")


# the following example shows how to
# use a defaut paramter Value
# if we call the function without argument,
#it use the default Value

def my_fuc(name="default"):
    print("my name: "+ name)

my_fuc("Zakaria")
my_fuc()
my_fuc("test")

# you can send any data types of argument to function
#(string, number, list, Dictionary)

def mydata(myinfo):
    for x in myinfo:
        print(x)
info = ["zakaria", "nabhan", "Student"]
mydata(info)

#return values
# to let a function return a value,
#use the return statement

def rechnen(x):
    return 3+x

print("Ergbinis: ", rechnen(4))


# the pass statement
# function cant be empty
# we have to use pass in thee function
# to avoid getting an error

def testpass():
    pass

# recursion
def tri_recursion(k):
    if(k>0):
        result= k+ tri_recursion(k-1)
        print(result)
        #print(tri_recursion(k-1))
    else:
        result=0
    return result

print("\n\n Ergbnis:")
tri_recursion(6)
