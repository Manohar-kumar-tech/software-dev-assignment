from DB4Library import DBHandler
from user import User
from book import Book

# Library Class (Composition- Book) 
class Library:
    def __init__(self, name):
        self.name = name
        self.db = DBHandler()
        
        
   # Book Managements
    def addBook(self, book:Book):
        try:
            cursor = self.db.conn.cursor()           
            cursor.execute("""
                INSERT INTO books(title, author, is_available)
                VALUES(?, ?, ?)""",
                (book.title, book.author, int(book.is_available))                
            )
            book.book_id = cursor.lastrowid
            self.db.conn.commit()
            print(f"Book '{book.title}' by '{book.author}' is added to the library")            
        except Exception as e:
            print(f"Error adding book: {e}")
        
    def removeBook(self, book:Book):
        self.db.executeQuery("DELETE FROM books WHERE id=?", (book.book_id))
        print(f"Book with ID '{book.title}' removed from the library.")
    
            
    def listAllBook(self):
        books = self.db.fetchAll("SELECT * FROM books")
        print(f"\n Books in '{self.name}' library: ")
        for book in books:
            status = "Available" if book[3] else "Cheked Out"
            print(f"ID- {book[0]}, {book[1]} by {book[2]} - '{status}'")
            
    # User management
    def addUser(self, user:User):
        self.db.executeQuery("INSERT INTO  users(name, user_id) VALUES (?, ?)", (user.name, user.user_id))
        print(f"User '{user.name} added to the library.'")
        
    def userAll(self):
        users = self.db.executeQuery("SELECT * FROM users")
        print(f"\nUsers in {self.name} library")
        for user in range(users[0], len(users[0])):
            print(f"ID :{user[0]}, Name: {user[1]}, User ID: {user[2]}")
            
    # Transactions of books
    def borrowBook(self, user:User, book:Book):
        book_id = book.book_id
        user_id = user.user_id
        print(type(book_id))
        print(type(user_id))
        # book = self.db.fetchOne("""SELECT * FROM books WHERE book_id = ? AND is_available = 1""", (book_id))
        # if not book:
        #     print(f"Book ID '{book.book_id}' is not available.")
        #     return
        self.db.executeQuery("""INSERT INTO borrowed_books (user_id, book_id) VALUES(?,?)""", (user_id, book_id))
        # self.db.executeQuery("""UPDATE books SET is_available = 0 WHERE book_id = ?""", (book_id))
        print(f"\nBook: '{book.title} is borrowed by USER: {user.name}.'")
        
    def returnBook(self, user:User, book:Book):
        book_id = book.book_id
        user_id = user.user_id
        self.db.executeQuery("""DELETE FROM borrowed_books WHERE user_id = ? AND book_id = ? """, (user_id, book_id))
        # self.db.executeQuery("""UPDATE books SET is_available = 1 WHERE book_id = ?""", (book_id))
        print(f"\nBook: '{book.title} is returned by USER: {user.name}.'")
        
                
    