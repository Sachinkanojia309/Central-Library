class library:
    def __init__(self,listofbooks):
        self.books = listofbooks
    
    def displayavailablebooks(self):
        print("Books present in the Library are : ")
        for book in self.books:
            print(" * " +book)

    def borrowbooks(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}.keep it safe and return in 30 days.")
            self.books.remove(bookname)
            return True
        else:
            print("Book is not present in the library,wait until the book available in library.")
            return False

    def returnBooks(self,bookname):
        self.books.append(bookname)
        print("Thank you for add/returning the book,Hope you enjoyed this book! ")



class student:
    def requestbook(self):
        self.book = input("Enter the name of the book you want to borrow = ")
        return self.book

    def returnbook(self):
        self.book = input("Enter the name of the book you want to add or return = ")
        return self.book
    

if __name__ == "__main__":
    centralibraray = library(['DSA','clear','algo','python','c++','java','ruby','HTML'])
    #centralibraray.displayavailablebooks()
    students = student()

    while (True):
        menu = '''\n********* CENTRAL LIBRARY *********
        1. List all the books available.
        2. Request a book.
        3. Return a book.
        4. Exit from the library.
        '''
        print(menu)
        a = int(input("Enter a choice = "))
        if a==1:
            centralibraray.displayavailablebooks()
        elif a==2:
             centralibraray.borrowbooks(students.requestbook())
        elif a==3:
            centralibraray.returnBooks(students.returnbook())
        elif a==4:
            print("Thank you for using Cental Library.! Have a good day!")
            exit()
        else:
            print("Invalid choice!")

        
        
    