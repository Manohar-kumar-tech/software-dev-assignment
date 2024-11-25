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
from datetime import datetime, timedelta
import json


class Book():
    def __init__(self, title, author, is_available = True):
        self.title = title
        self.author = author
        self.is_available = is_available
        self.due_date = None
        
    def setDueDate(self, borrow_date, days= 7):
         self.due_date = borrow_date + timedelta(days=days)
         
    
    def getDueDate(self):
        if self.due_date is None:
            self.setDueDate()
        return self.due_date
        
        
        
    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed (Due Date: {self.due_date})"
        return f"{self.title} by {self.author} is {status}"
    
class User():
    def __init__(self, name, library):
        self.name = name
        self.library = library
        self.borrowed_books = []
        
    def borrowBook(self, book, borrow_date):
        if book.is_available:
            book.is_available = False
            book.setDueDate(borrow_date)
            self.borrowed_books.append(book.title)
            self.library.record_tarnsaction(self, book, "Borrowed")
            print(f" '{self.name}' borrowed '{book.title}' Due date: '{book.getDueDate()}'.")
        else:
            print(f"{book.title} is not available")
            
    def returnBook(self, book,  return_date):
        if book.title in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book.title)
            if return_date > book.getDueDate():
                days_overdue = (return_date - book.getDueDate()).days
                # print(type(days_overdue))
                fine = 10 * days_overdue
                print(f"'{self.name}' returned '{book.title}' {days_overdue}days late. Fine: Rs = {fine}")
            else:
                print(f"{book.title} returne on time: ...")
            # book.due_date = None
            self.library.record_tarnsaction(self, book, "Returned")
            # print(f"{self.name} returned {book.title}.")
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
            
    def search(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if results:
            print("\nSearch Results: ")
            for book in results:
                print(book)
        else:
            print("No Bokk found. ")
            
    def record_tarnsaction(self, user, book, action):
        self.transactions.append({
            "user" : user.name,
            "book" : book.title,
            "action": action,
            "time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    
    def displayTransaction(self):
        print("\nTansaction History.")
        for txn in self.transactions:
            print(f"{txn['time']}- {txn['user']} {txn['action']} '{txn['book']}")
    
    # def exract1(self, books):
    #     record = {}
    #     for key, value in self.books.__dir__.items():
    #         if key == record['due_date']:
    #             record[key] = str(value)
    #         else:
    #             record[key] = value
    #     return record
    
    # def exract2(self, transactions):
    #     record = {}
    #     for key, value in self.transactions.__dir__.items():
    #         if key == record['time']:
    #             record[key] = str(value)
    #         else:
    #             record[key] = value
    #     return record
            
    def saveData(self, filename):
        with open(filename, 'w') as file: 
            # b = self.books
            # t = self.transactions
            # book = self.exract1(b)
            # transaction = self.exract2(t)
                         
            # data = {
            #     "books": book,
            #     "transactions": transaction 
            #     }
            # json.dump(data, file)
            # print(f"Library data saved to {filename}")
            pass      
              
    def loadData(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data['books']]
                self.transactions = data['transactions']
                print(f"Library data loaded from {filename}")
        except FileNotFoundError:
            print("No saved data found")
        
        

# Demontration

library = Library()
book1 = Book("1984", "I don't remember now the author")
book2 = Book("India way", "Dr. S jai sankar")
book3 = Book("Atomic Habit", "James clear")
book4 = Book("Psychology of money", "Random")
library.addBook(book1)
library.addBook(book2)
library.addBook(book3)
library.addBook(book4)


library.saveData("library.json")
library.displayBooks()

user1 = User("Manohar", library)
user2 = User("Bob", library)

borrow_date = datetime.now()

user1.borrowBook(book2,  borrow_date)
user1.borrowBook(book3,  borrow_date)
user2.borrowBook(book1,  borrow_date)

user3 = User("Alice", library)

# library.saveData("library.json")

# library.loadData("library.json")

library.displayBooks()
print(user1)
print(user2)
print(user3)

return_date = borrow_date + timedelta(days=10)
user1.returnBook(book2, return_date)
user1.returnBook(book1, datetime.now())
user2.returnBook(book1, return_date)

# library.saveData("library.json")
library.displayBooks()
library.displayTransaction()
