from LibraryMain import  Library
from user import User
from book import Book

library = Library("Thakurganj")

book1 = Book("Atomic Habit", "James Clear") 
book2 = Book("The India Way", "Dr. S Jai Sankar") 
book3 = Book("Wings of Fire", "A.P.J Abdul Kalam") 
book4 = Book("Autobiography of Yogi", "Yogi")
library.addBook(book1)
library.addBook(book2)
library.addBook(book3)
library.addBook(book4)

user1 = User("Manohar", "U0001")
user2 = User("Alice", "U0002")
user3 = User("Bob", "U0003")

library.addUser(user1)
library.addUser(user2)
library.addUser(user3)

library.listAllBook()

library.borrowBook(user1, book1)
library.borrowBook(user1, book2)
library.borrowBook(user2, book3)
library.borrowBook(user3, book4)



library.listAllBook()


book5 = Book("Hard Thing for hard thing", "Someone")
library.addBook(book5)


library.listAllBook()

library.returnBook(user1, book2)

library.listAllBook()
library.userAll()

