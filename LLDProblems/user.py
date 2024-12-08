class User():
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        # self.borrowed_books = []
        
    def __repr__(self):
        return f"User({self.name}, {self.user_id})"
        
        
    # def borrowBook(self, Book):
    #     if Book.is_available:
    #         self.borrowed_books.append(Book)
    #         Book.is_available = False
    #         print(f"'{self.name}' borrowed '{Book.title}'")
    #     else:
    #         print(f"{Book.title} is not availble...")
            
    # def returnBook(self, Book):
    #     if Book in self.borrowed_books:
    #         self.borrowed_books.remove(Book)
    #         Book.is_available = True
    #         print(f"{self.name} retured '{Book.title}'")
    #     else:
    #         print(f"{self.name} did not borrowed '{Book.title}'")
            
            
# Librarian class (inherit - User)
# class Librarian(User):
#     def __init__(self, name):
#         super().__init__(name)
        
#     def addBook(self, library, book):
#         library.addBook(book)
        
#     def removeBook(self, library, book):
#         library.removeBook(book)
    
        