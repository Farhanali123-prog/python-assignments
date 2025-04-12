books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    books.append({
        "title": title,
        "author": author,
        "status": "Available"
    })
    print("Book added successfully.")

def display_books():
    if not books:
        print("No books in library.")
        return
    print("\nLibrary Books:")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. {book['title']} by {book['author']} - {book['status']}")

def borrow_book():
    display_books()
    if books:
        num = int(input("Enter book number to borrow: "))
        if 1 <= num <= len(books):
            if books[num-1]["status"] == "Available":
                books[num-1]["status"] = "Borrowed"
                print("You have borrowed the book.")
            else:
                print("Sorry, the book is already borrowed.")
        else:
            print("Invalid book number.")

def return_book():
    display_books()
    if books:
        num = int(input("Enter book number to return: "))
        if 1 <= num <= len(books):
            if books[num-1]["status"] == "Borrowed":
                books[num-1]["status"] = "Available"
                print("Book returned successfully.")
            else:
                print("This book wasn't borrowed.")
        else:
            print("Invalid book number.")

def menu():
    while True:
        print("\n--- Library Manager ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Exiting Library Manager. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

menu()
