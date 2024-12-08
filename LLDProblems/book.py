class Book():
    def __init__(self, title, author, is_available=True, book_id = None):
        self.title = title
        self.author = author
        self.book_id = book_id
        # self.due_date = due_date
        self.is_available = is_available
    
    def __repr__(self):
        status = "Availabel" if self.is_available else "Unavailable"
        return f"'{self.title}' by '{self.author}' is -{status}"