from Library import Book, Library, User, Librarian

library = Library()

book1 = Book("Atomic Habit", "James Clear") 
book2 = Book("The India Way", "Dr. S Jai Sankar") 
book3 = Book("Wings of Fire", "A.P.J Abdul Kalam") 
book4 = Book("Autobiography of Yogi", "Yogi")
library.addBook(book1)
library.addBook(book2)
library.addBook(book3)
library.addBook(book4)

user1 = User("Manohar")
user2 = User("Alice")
user3 = User("Bob")

library.saveData()


library.loadData()
library.list_available_book()

user1.borrowBook(library, book1)
user1.borrowBook(library, book2)
user2.borrowBook(library, book3)
user3.borrowBook(library, book3)
library.saveData()

library.loadData()
library.list_available_book()

librarian = Librarian("James")

book5 = Book("Hard Thing for hard thing", "Someone")

librarian.addBook(library,book5)

library.list_available_book()

user1.returnBook(library, book2)
library.saveData()


library.loadData()
library.list_available_book()

