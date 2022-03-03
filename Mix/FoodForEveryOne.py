'''
Create a Person class which will have three properties:

Name
List of foods they like
List of foods they hate
In this class, create the method taste():

It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person's like list, add 'and loves it!' to the end.
If it is in the person's hate list, add 'and hates it!' to the end.
If it is in neither list, simply add an exclamation mark to the end.
Examples
'''

class Person:
    def __init__(self, name, love=[], hate=[]):
        self.name = name
        self.love = love
        self.hate = hate

    def taste(self, food):
        if food in self.love:
            return '{} likes the {}'.format(self.name, food)
        elif food in self.hate:
            return '{} hates the {}'.format(self.name, food)
        else:
            return '{} is not founded in the list'.format(food)

p1 = Person("Sam", ["ice 414"], ["carrots"])

print(p1.taste("ice 414"))