

class Book:
    counter_id = 0

    def __init__(self, title, publishing_date, version, author):
        Book.counter_id += 1
        self.title = title
        self.publishing_date = publishing_date
        self.version = version
        self.author = author
        self.id = Book.counter_id


