import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "SQL@123!",
    database = "testdb"
)

mycursor = mydb.cursor()

"""Creating the table"""
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),             
    ISBN VARCHAR(255)             
)
""")

#Function to add books
def insertBook():
    sql = "INSERT INTO Books (title, author, ISBN) VALUES(%s, %s, %s)"
    book_title = input("Enter Book Title: ")
    book_author = input("Enter Book Author: ")
    book_isbn = input("Enter Book ISBN: ")
    val = (book_title, book_author, book_isbn)

    mycursor.execute(sql, val)
    mydb.commit()

    print(f"{book_title} by {book_author}, ISBN({book_isbn}) is added")

#Function to Search for books
def searchBook():
    sql = "SELECT * FROM Books WHERE title = %s"
    search_title = input("Enter Book title for search: ")
    val = (search_title,) #value should be passed as a tuple

    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    print("Book(s) found")
    for book in myresult:
        print(book)

#Function to list all books in the library
def allBooks():
    sql = "SELECT * FROM Books"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("List of all the books in the Library")
    for book in myresult:
        print(book)

#Function to delete a book
def deleteBook():
    delete_book = int(input("Enter Book's ID to delete: "))
    
    while True:
        confirm_choice = input(f"Are you sure you want to delete the book with ID{delete_book}?(Y/N): ")
        if confirm_choice.upper() == "N":
            print("The book will not be deleted!")
            break
        elif confirm_choice.upper() == "Y":
            sql = "DELETE FROM Books WHERE id = %s"
            val = (delete_book,)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted.")
            break
        else:
            print("Wrong Choice. Pick Y or N")



while True:
    print("Welcome to TestDB Library.")
    print()
    print("""
        1. Add a book
        2. Search for a book
        3. List all books in the library
        4. Delete a book
        5. Exit
    """)

    choice = int(input("Pick the service you require(1-4): "))
    match choice:
        case 1:
            insertBook()
            print()
        case 2:
            searchBook()
            print()
        case 3:
            allBooks()
            print()
        case 4:
            deleteBook()
            print()
        case 5:
            print("Bye Library User!")
            mycursor.close()
            mydb.close()
            print("Database connection closed.")
            break
        case _:
            print("Kindly select an option from 1 to 5")


                
    