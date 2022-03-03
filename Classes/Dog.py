class Dog:
    # n name, m month, d day, y year, st speaktext
    def __init__(self, n, m, d, y, st):
        """
        :param n:
        :param m:
        :param d:
        :param y:
        :param st:
        """
        self.n = n
        self.m = m
        self.d = d
        self.y = y
        self.st = st

    def speak(self):
        """
        :return: speaktext
        """
        return self.st

    def getName(self):
        """
        :return: name of dog
        """
        return self.n

    def birthday(self):
        """
        :return: day month year
        """
        return "{}.{}.{}".format(self.d, self.m, self.y)

    def changeBark(self, bark):
        """
        :param bark:
        :return:
        """
        self.st = bark

    def __add__(self, otherDog):
        return Dog("Puppy of " + self.n + " and " + otherDog.n,
        self.m, self.d, self.y + 1,
        self.st +" "+ otherDog.st)


def main():
    boyDog = Dog("Mesa", 5, 15, 2004, "WOOOOF")
    girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
    boyDog.changeBark("hahahhah")

    puppy = boyDog + girlDog
    print(puppy.st)
    print(puppy.n)
    print(puppy.birthday())


if __name__ == '__main__':
    main()
