'''
Write a Composer class that has three instance variables:

name
dob
country
Add an additional class variable
.count which counts the total number of instances created.
'''

class Composer:

    counter = 0
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.counter +=1


print(Composer.counter)

c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.counter)

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
print(Composer.counter)
