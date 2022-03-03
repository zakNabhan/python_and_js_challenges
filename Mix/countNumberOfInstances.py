'''
Create a class named User
and create a way to check the number
 of users (number of instances) were created,
so that the value can be accessed as a class attribute.
'''


class User:
    useraccount = 0

    def __init__(self, username):
        self.username = username
        User.useraccount += 1



u1 = User("johnsmith10")
u2 = User("johnsmith10")
u3 = User("johnsmith10")

