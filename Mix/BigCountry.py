'''
A country can be said as being big if it is:

Big in terms of population.
Big in terms of area.
Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

Population is greater than 250 million.
Area is larger than 3 million square km.
Also, create a method which compares a country's population density to another country object. Return a string in the following format:

{country} has a {smaller / larger} population density than {other_country}

'''


class Country:
    is_big = False

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        if population > 250000000 or area > 3000000:
            self.is_big = True

    def compare_pd(self, other):
        if other.population > self.population:
            return '{} has  large popu.. than {}'.format(other.name, self.name)
        else:
            return '{} has  smaller popu.. than {}'.format(other.name,
                                                           self.name)


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
print(andorra.compare_pd(australia))
print(andorra.is_big)
