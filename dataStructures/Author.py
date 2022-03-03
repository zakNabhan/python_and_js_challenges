
class Author:
    counter_id = 0

    def __init__(self, name, phone, email):
        Author.counter_id += 1
        self.name = name
        self.phone = phone
        self.email = email
        self.id = Author.counter_id


    def add_author(self, author):
        self.authors.append(author)


author1 = Author("Mhamad", +96170123456, "mhamad@gmail.com")

print(author1.add_author("zakaria"))
print(author1.name)
