class Test:

    def __init__(self, name, salary_1, salary_2):
        self.name = name
        self.salary_1 = salary_1
        self.salary_2 = salary_2

    def __add__(self, othersalary):
        totalsalaries = self.salary_1 + othersalary.salary_2
        return totalsalaries



def main():
    p1 = Test("zakaria", 26, 30)
    p2 = Test("zakaria", 2, 30)

    # summiere all salary of p1
    summe = p1 + p2


    print("name: " + p1.name + " age: ", p1.salary_1)
    print(summe)


if __name__ == '__main__':
    main()
