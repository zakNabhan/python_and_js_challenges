#print("for schleife")

# print each name in the list

namen = ["zakaria", "test1", "test2"]

for name in namen:
    print(name)

# looping through a string

text = "ich bin 22 alt"

for x in text:
    print(x)

print("_________________")
# oder
for arg in "ich bin 2020":
    print(arg)

print("____________________")
#break statement
namen_list = ["zakaria", "nabhan", "max"]

for x in namen_list:
    print(x)
    if x=="nabhan":
        break;

#break statement
namen_list = ["test", "test2", "test4"]

for x in namen_list:
    if x=="test2":
        break;
    print(x)
# continue statement

myliste = ["test1", "test2", "test3", "test4"]
for x in myliste:
    if x == "test3":
        continue
    print(x)


# the range fuunction
# returnss a squence of nummber
# starting from 0 be default
#  output 0,1,2,3,4
for x in range(5):
    print(x)

print("______________")

# oder
i = 10
for x in range(i):
    print(x)

print("______________")
# using  a start parameter
# print between 2 and 6 also 2,3,4,5
for x in range(2, 6):
    print(x)

# else in for loop

for x in range(6):
    print(x)
else:
    print("finshed")

print("______________")

# nested loops
# a nested loop is a loop in a loop
# print each adjective for every fruit
adj = ["red", "big", "tasty"]
fruit = ["apple", "banna", "cherry"]

for x in adj:
    for y in fruit:
        print(x, y)
