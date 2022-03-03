'''
Create a Book class that has two attributes:

.title
.author
and two methods:

A method named .get_title() that returns: "Title: " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:

Pride and Prejudice - Jane Austen (PP)
Hamlet - William Shakespeare (H)
War and Peace - Leo Tolstoy (WP)

'''

class Book:
    def __init__(self, title,  author):
        '''
        :param title:
        :param author:
        '''
        self.title = title
        self.author = author

    def get_title(self):
        '''
        :return: title
        '''
        return 'Title: {}'.format(self.title)
    def get_author(self):
        '''
        :return: author
        '''
        return 'Author: '.format(self.author)


PP = Book('Pride and Prejudice', 'Jane Austen')
H = Book('Hamlet', 'William Shakespeare')
WP = Book('War and Peace', 'Leo Tolstoy')
print(PP.title)