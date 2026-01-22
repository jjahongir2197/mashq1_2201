class Book:
    def __init__(self, bid, name):
        self.bid = bid
        self.name = name
        self.available = True

    def info(self):
        return f"{self.bid} | {self.name} | {'Bor' if self.available else 'Olingan'}"


class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def add_reader(self, reader):
        self.readers.append(reader)

    def show_books(self):
        for b in self.books:
            print(b.info())

    def rent_book(self, reader_name, book_id):
        for r in self.readers:
            if r.name == reader_name:
                for b in self.books:
                    if b.bid == book_id and b.available:
                        b.available = False
                        r.books.append(b.name)
                        print("Kitob berildi")
                        return
        print("Xatolik")

    def report(self):
        for r in self.readers:
            print(r.name, "->", r.books)


lib = Library()
lib.add_book(Book(1, "Python"))
lib.add_book(Book(2, "Algorithms"))
lib.add_reader(Reader("Jahongir"))

while True:
    print("\n1.Kitoblar  2.Ijara  3.Hisobot  0.Exit")
    c = input(">>> ")

    if c == "1":
        lib.show_books()
    elif c == "2":
        lib.rent_book(input("Ism: "), int(input("Kitob ID: ")))
    elif c == "3":
        lib.report()
    elif c == "0":
        break
