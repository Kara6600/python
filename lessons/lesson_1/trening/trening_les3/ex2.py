from book import Book

# создаем список книг
library = [
    Book("Война и мир", "Лев Толстой"),
    Book("1984", "Джордж Оруэлл"),
    Book("Мастер и Маргарита", "Михаил Булгаков")
]

# цикл по списку и вывод в нужном формате
for book in library:
    print(f"{book.title} - {book.author}")