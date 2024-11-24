# Library Management System   - A system to manage book and user in a labrary

# Features (Extended and with persistence)
#     1. Add book to the library
#     2. Borrow book for a user
#     3. Return book and update availability
#     4. View transaction history

# How
# 1. library class // hold collection of book , provide methods ton add display, and manage book
# 2. book class  // indivisual book with attributes title, author, and availability
# 3. User class // user who can borrow a book

# programm
from datetime import datetime
import json


class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        
    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} is {status}"
    
class User():
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrowBook(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book.title)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available")
            
    def returnBook(self, book):
        if book.title in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book.title)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} has not borrowed {book.title}.")
            
    def __str__(self):
        return f"{self.name} has borrowed Books: {', '.join(self.borrowed_books) if self.borrowed_books else None}"
    
    
class Library():
    def __init__(self):
        self.books = []
        self.transactions = []
        
    def addBook(self, book):
        if book:
            new_book = book
            self.books.append(new_book)
            print(f"Added {book.title} by {book.author} to the library")
        else:
            print("You haven't added book. Try again ...")
               
    
    def displayBooks(self):
        print("\nLibrary Books: ")
        for book in self.books:
            print(book)
            
    def record_tarnsaction(self, user, book, action):
        self.transactions.append({
            "user" : user.name,
            "book" : book.title,
            "action": action,
            "time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    
    def displayTransaction(self):
        print("\Tansaction History.")
        for txn in self.transactions:
            print(f"{txn['time']}- {txn['user']} {txn['action']} '{txn['book']}")
            
    def saveData(self, filename):
        with open(filename, 'w') as file:
            data = {"books":[book.__dict__ for book in self.books], "tarnsactions": self.transactions }
            json.dump(data, file)
            
    def loadData(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data['books']]
                self.transactions = data['transactions']
        except FileNotFoundError:
            print("No saved data found")
        
        

# Demontration

library = Library()
book1 = Book("1984", "I don't remember now the author")
book2 = Book("India way", "Dr. S jai sankar")
book3 = Book("Atomic Habit", "James clear")
library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

library.displayBooks()

user1 = User("Manohar")
user2 = User("Bob")

user1.borrowBook(book2)
user1.borrowBook(book3)
user2.borrowBook(book1)

user3 = User("Alice")

library.displayBooks()
print(user1)
print(user2)
print(user3)

user1.returnBook(book2)
user1.returnBook(book1)

library.displayBooks()
