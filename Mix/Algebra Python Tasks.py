# Multiple of 100

'''
Create a function that takes an integer
and return True if it's divisible by 100,
otherwise return False.
'''


def divisible(num):
    if num > 0 and num % 100 == 0:
        return True
    else:
        return False


print(divisible(1))
print(divisible(1000))

# Miserable of a Calculatur
'''
Create a function that will handle simple math expressions. 
The input is an expression in the form of a string.
'''


def calculator(txt):
    return eval(txt)


print(calculator("23+2"))

# On/Off Switches

'''
Create a function that returns 
how many possible outcomes can come from a
 certain number of switches (on / off). In other words,
  for a given number of switches, how many different combinations 
  of on and off can we have?


'''


def pos_com(num):
    return 2 ** num


print(pos_com(1))
print(pos_com(3))
print(pos_com(10))

# Number of Stickers

'''
Given a Rubik's Cube with a side length of n, 
return the number of individual stickers 
that are needed to cover the whole cube.

Pictures of Rubik's Cubes

The Rubik's cube of side length 1 has 6 stickers.
The Rubik's cube of side length 2 has 24 stickers.
The Rubik's cube of side length 3 has 54 stickers.

Keep in mind there are six faces to keep track of.

'''


def how_many_stickers(n):
   return 6*n*n



print(how_many_stickers(1))
print(how_many_stickers(2))
print(how_many_stickers(3))
