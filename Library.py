print("""===================================================================
++++++++++++++++++++++++++    Welcome     +++++++++++++++++++++++++
===================================================================""")

library = {
    ("ikigai", "self help", "Héctor García and Francesc Miralles", "Available"),
    ("Love Hypothesis", "Romcom", "Ali Hazelwood", "Not Available"),
    ("Check & Mate", "Romcom", "Ali Hazelwood", "Available"),
    ("I hope this dosen't find you", "romcom", "Ann Liang", "Available"),
    ("Crimson Mandate", "Non Fiction", "Shaurya Dhakate", "Not Available"),
    ("The Shimla affair", "thriller", "Srishti Chaudhary", "Available")
}
Library = list(library)
# DONATE BOOK
def donate_book():
    book_name = input("Enter Book Name: ")
    genre = input("Enter the Genre: ")
    author = input("Enter the Author Name: ")
    book = (book_name, genre, author, "Available")
    Library.append(book)
    print("****THANKS FOR DONATING****")
# TOTAL BOOKS
def Total_books():
    print("Books in Library:")
    for i in Library:
        print(i)
# ISSUE BOOK
def Issue_books():
    count = len(Library)
    print("Books in Library:")
    for book in Library:
        print(book)
    book = input("Enter the book name: ")
    for i in range(count):
        if book == Library[i][0]:
            if Library[i][3] == "Available":
                print("BOOK AVAILABLE!!")
                days = int(input("For How many days do you want the book: "))
                Library[i] = (
                    Library[i][0],
                    Library[i][1],
                    Library[i][2],
                    "Not Available" )
                print("****BOOK HAVE BEEN ISSUED****")
            else:
                print("BOOK NOT AVAILABLE!!!")
            break
    else:
        print("BOOK NOT FOUND!!!")
# SEARCH BOOKS
def search_book():
    count = len(Library)
    print("""How do you want to search the book?
1. By BookName
2. By Genre
3. By Author""")
    choice = int(input("Enter the Choice (1/2/3)?: "))
    if choice == 1:
        book1 = input("Enter Bookname: ")
        for i in range(count):
            if book1 == Library[i][0]:
                print(Library[i])
                break
        else:
            print("BOOK NOT FOUND!!!")
    elif choice == 2:
        genre1 = input("Enter genre: ")
        found = False
        for i in range(count):
            if genre1.lower()==Library[i][1].lower():
                print(Library[i])
                found = True
        if not found:
            print("BOOK NOT FOUND!!!")
    elif choice == 3:
        Author1 = input("Enter Author Name: ")
        found = False
        for i in range(count):
            if Author1.lower() == Library[i][2].lower():
                print(Library[i])
                found = True
        if not found:
            print("BOOK NOT FOUND!!!")
    else:
        print("INVALID CHOICE!!!")
# RETURN BOOK
def return_book():
    count = len(Library)
    Book2 = input("Enter Book name: ")
    for i in range(count):
        if Book2 == Library[i][0]:

            Library[i] = (
                Library[i][0],
                Library[i][1],
                Library[i][2],
                "Available" )
            print("THANKS FOR RETURNING THE BOOK!!!")
            break
    else:
        print("BOOK NOT FROM HERE!!")
# MAIN MENU
enter = input("Do You Want to Enter the Library?(Y/N): ")
if enter.upper() == "Y":
  print("""===================================================================
+++++++++++++++++++++++WELCOME TO LIBRARY++++++++++++++++++++++++++
===================================================================""")
  name = input("Enter your Name: ")
  Number = input("Enter Your No.: ")
  def front():
    while True:
      print(""" 
1. DONATE BOOK
2. TOTAL BOOKS
3. BOOK ISSUE
4. SEARCH BOOKS
5. RETURN BOOK
6. EXIT
""")
      choice1 = int(input("Enter your Choice: "))
      if choice1 == 1:
        donate_book()
      elif choice1 == 2:
        Total_books()
      elif choice1 == 3:
        Issue_books()
      elif choice1 == 4:
        search_book()
      elif choice1 == 5:
        return_book()
      elif choice1 == 6:
        print("THANK YOU FOR USING THE LIBRARY!")
        break
      else:
        print("INVALID CHOICE!!!")
  front()
else:
    print("BYE :(")
