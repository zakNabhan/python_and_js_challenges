'''
Create a function which takes a list
of objects from the class IceCream and
 returns the sweetness value of the sweetest icecream.
 Note that there is a class is provided for you in the Tests tab.

 Each sprinkle has a sweetness value of 1
Check below for the sweetness values of the different flavors.
Flavors	Sweetness Value
Plain	0
Vanilla	5
ChocolateChip	5
Strawberry	10
Chocolate	10
'''
class IceCream:
    def __init__(self, flavor, value):
        self.flavor = flavor
        self.value = value

    def sweetest_icecream(lst):
        lst_value = []
        for ic in lst:
            if ic.flavor == "Plain":
                lst_value.append(ic.num_sprinkles)
            elif ic.flavor == "Vanilla":
                lst_value.append(5 + ic.num_sprinkles)
            elif ic.flavor == "ChocolateChip":
                lst_value.append(5 + ic.num_sprinkles)
            elif ic.flavor == "Strawberry":
                lst_value.append(10 + ic.num_sprinkles)
            elif ic.flavor == "Chocolate":
                lst_value.append(10 + ic.num_sprinkles)
        return max(lst_value)


