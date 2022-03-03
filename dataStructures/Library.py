from dataStructures.Author import Author
from dataStructures.Book import Book


authors = []
books = []


author1 = Author("Mhamad", +96170123456, "mhamad@gmail.com")
author2 = Author("Salem",  +9664021833,  "salem@gmail.com")
author3 = Author('Rola',   +9631249392,  "rola@gmail.com")

book1 = Book("Learn Java", 12-20-2019, 1, author1)
book2 = Book("Learn HTML", 5-8-2018, 3, author2)
book3 = Book("PHP for beginners", 10-2-2019, 1, author3)


authors.append(book1)
authors.append(book2)

for x in authors:
    print(x.version, x.author.name)