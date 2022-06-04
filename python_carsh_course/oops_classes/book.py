class Book:
    def __init__(self, title):
        self.title = title
        self.author = None

    def add_author(self, name):
        # add author property
        self.author = name

    def add_chapter(self, number, title):
        # add properties chapter_number and chapter_title
        self.chapter_number = number
        self.chapter_title = title



class BookInfo(Book):
    def __init__(self, title, price, info=False):
        Book.__init__(self, title)
        # add properties price and info
        self.price = price
        self.info = info
        self.stars = 0

    def rating(self, stars):
        try:
            # check if existing stars are less than new stars
            # and if new stars are greater than 4
            # adjust new price by a 20% increase
            if self.stars < stars and stars > 4:
                self.price += .20 * self.price
            elif self.stars > stars:
                self.price -= .20 * self.price

            # update the stars property
            self.stars = stars
        except Exception as e:
            print(e, "Please try again")


book = Book("Two Scoops of Django")
book.add_author("Greenfeld")
book.add_chapter(3, "Async Views")

book_info = BookInfo(title=book.title, price=10, info=True)
book_info.rating(5)

print("Book info: ", end=" ")
print(
    book_info.title, str(book_info.stars) + " stars",
    book_info.price, book_info.author, sep=", "
)
print("Book properties: ", book.__dict__)
print("BookInfo properties: ", book_info.__dict__)
