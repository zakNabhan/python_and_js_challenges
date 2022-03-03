
# Instruction

'''
Create methods for the Calculator class that can do the following:

Add two numbers.
Subtract two numbers.
Multiply two numbers.
Divide two numbers.

'''

class Calculator:
    # Write methods to add(), subtract(), multiply() and divide()

    def add(self, number1, num2):
        return number1 + num2


    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 + num2


    def divide(self, num1, num2):
        return num1 / num2


cal = Calculator()
cal.subtract(10, 2)
cal.multiply(10, 2)
cal.divide(10, 2)
print(cal.add(10, 2))
