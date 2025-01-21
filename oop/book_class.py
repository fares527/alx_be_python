class Book:
    def __init__(self, title, author, year=0):
        self.title= title
        self.author= author
        self.year= year
        pass
    def __del__(self):
        return "Deleting (title of the book)"
    def __str__(self):
        return"(title) by (author), published in (year)"
        
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
        pass