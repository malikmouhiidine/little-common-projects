from isbntools.app import *

# getting the name
book = input("Enter book plz: ")

#getting it's isbn
get_isbn = isbn_from_words(book)

# getting info from the isbn
info = registry.bibformatters['labels'](meta(get_isbn))

# outputing info
print(info)