books = [
    {
        "title": "Darkness Hour", 
        "author": "Aatrox D. Darkness", 
        "publication_year": 1998, 
        "isbn": "978-3-16-148410-0", 
        "genre": "Thriller, Mystery"
    },
    {
        "title": "Lightness Hour", 
        "author": "Kyle D. Light", 
        "publication_year": 1991, 
        "isbn": "978-0-7432-7356-5", 
        "genre": "Romantic, Drama"
    },
    {
        "title": "Happiest of My Life", 
        "author": "Teemo D. Veli", 
        "publication_year": 2010, 
        "isbn": "978-0-452-28423-4", 
        "genre": "Adventure, Drama"
    },
    {
        "title": "Monster of Demacia", 
        "author": "Fiddle D. Stick", 
        "publication_year": 1999, 
        "isbn": "978-1-4516-7321-8", 
        "genre": "Horror, Mystery, Thriller"
    },
    {
        "title": "Void Century", 
        "author": "Kass D. Adin", 
        "publication_year": 1942, 
        "isbn": "978-3-16-148410-0", 
        "genre": "Adventure, Mystery, Thriller, Horror"
    }
]

for book in books:
    print(f"Title: {book['title']} | Author: {book['author']} | Publication Year: {book['publication_year']} | ISBN: {book['isbn']} | Genre: {book['genre']}")
