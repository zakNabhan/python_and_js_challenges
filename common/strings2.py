parrot ="Norwegian Blue"

print(parrot[0:6:2])

print(parrot[0:6:3])

number = "9,233;372:063 854,774;807"
seperators = number[1::4]

print(seperators)
'''
values = "".join(char if char not in seperators else "" for char in number).split()
print([int(val) for val in values])'''

values = ""
for char in number.split(" "):
    if char not in seperators:
        values.join(char)
        for val in values:
            print(int(val))

