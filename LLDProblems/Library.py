# Phase 1: Requirements
#     User can borrow Book 
#     Library can add and remove Books and users
#     Books have metadata (title, author, availability)
#     Track borrowed book and due dates
    
    
# Phase 2: class relationship
#     1. User: Borrow books
#     2. Librarian (inhert user): add/remove Book 
#     3. Library: holds collection of books
#     4. Book: represent single book
    
# Phase 3: Implementation

import json
from datetime import datetime, timedelta

# Book Class
class Book:
    def __init__(self, title, author, due_date = None):
        self.title = title
        self.author = author
        self.borrowed_by = None
        self.due_date = None if due_date else datetime.now().strftime('%Y-%m-%d')
        self.is_available = True
    
    def borrow(self, user):
        if self.is_available:
            self.is_available = False
            self.borrowed_by = user
            self.due_date = datetime.now() + timedelta(days=10)
            print(f"'{self.title}' borrowed by {user.name} Due date: {self.due_date}")
        else:
            print(f"{self.title} is currently unavailable")
            
    def isReturn(self):
        self.borrowed_by = None
        self.due_date = None
        self.is_available = True
        print(f"{self.title} is now return")
        
    def to_dict(self):
        return {
            'title' : self.title,
            'author': self.author,
            'due_date': self.due_date,
            'is_available': self.is_available
                    
        }
    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['author'], data['due_date'])
        
        
        
        
# Library Class (Composition- Book) 
class Library:
    def __init__(self, data_file = "libraryData.json"):
        self.books = []
        self.data_file = data_file
        self.loadData()
        
    def addBook(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
        
    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library")
        else:
            print(f"Book '{book.title} not found in the library'")
            
            
    def list_available_book(self):
        print("Available Books: ")
        for book in self.books:
            if book.is_available:
                print(f"- {book.title} by {book.author}")
                
    def saveData(self):
        with open(self.data_file, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)
            print("Data saved to file")
        
    def loadData(self):
        try:
            
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.books = [Book.from_dict(book_data) for book_data in data]
                print("data load from file")
        
            
        except FileNotFoundError:
            self.books = []


# User class (Association with Library)
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrowBook(self, library, Book):
        for book in library.books:
            if book.title == Book.title and book.is_available:
                book.borrow(self)
                self.borrowed_books.append(book)
                return
        print(f"Book {Book.title} is not availabe")
        
    def returnBook(self, library, Book):
        for book in library.books:
            if book.title == Book.title:      
                book.isReturn() 
                self.borrowed_books.remove(book)              
                return
        print(f"You don't have the book '{Book}' to return")
                
                
# Librarian class (inherit - User)
class Librarian(User):
    def __init__(self, name):
        super().__init__(name)
        
    def addBook(self, library, book):
        library.addBook(book)
        
    def removeBook(self, library, book):
        library.removeBook(book)
    

              