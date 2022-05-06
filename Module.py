# Imports to support functions
from audioop import add
from tkinter import *
from tkinter import messagebox

# Creates main window
root = Tk()
root.title("Library Of The Gods!")
root.geometry("600x400")

# Database for books
database = []

# Function that creates a window that displays all books and their availability
def showBooks():
    librarySelection = ''
    for i in database:
        librarySelection = librarySelection + i['Title'] + ': ' + str(i['# Not checked out']) + '\n'
    messagebox.showinfo("Title: # Available", librarySelection)

# Function to add book to database
def addBook():
    top = Toplevel()
    top.title("Book Information")
    top.geometry("450x300")

    # Title Label and input box
    titlLabel = Label(top, text="Title: ")
    titl1 = Entry(top, width=50)
    titl1.insert(0, "Title")

    # Author Label and input box
    authLabel = Label(top, text="Author: ")
    auth1 = Entry(top, width=50)
    auth1.insert(0, "Letters only")

    # ISBN Label and input box
    isbnLabel = Label(top, text="ISBN: ")
    isbn1 = Entry(top, width=50)
    isbn1.insert(0, "Numbers only")

    # Purchased amount Label and input box
    purchLabel = Label(top, text="Num Purchased: ")
    purch1 = Entry(top, width=50)
    purch1.insert(0, "Whole number only")

    # Available Label and input box
    availLabel = Label(top, text="Num Available: ")
    avail1 = Entry(top, width=50)
    avail1.insert(0, "Whole number only")

    # Submit button
    submButton = Button(top, text="Submit", command=lambda: appendBook(titl1.get, auth1.get, isbn1.get, purch1.get, avail1.get))

    # Cancel button
    canclButton = Button(top, text="Cancel", command=top.destroy)

    # top level window layout
    titlLabel.grid(column=0, row=2)
    titl1.grid(column=1, row=2)
    authLabel.grid(column=0, row=3)
    auth1.grid(column=1, row=3)
    isbnLabel.grid(column=0, row=4)
    isbn1.grid(column=1, row=4)
    purchLabel.grid(column=0, row=5)
    purch1.grid(column=1, row=5)
    availLabel.grid(column=0, row=6)
    avail1.grid(column=1, row=6)
    submButton.grid(column=0, row= 8)
    canclButton.grid(column=1, row=8)

def appendBook(title, author, isbn, purchased, available):
    database.append({'Title': title, 'Author': author, 'ISBN': isbn, '# Purchased': purchased, '# Not checked out': available})
    messagebox.showinfo("Confirmation", "Book Added Successfully!")
    

database.append({'Title': 'This land is our land', 'Author': 'Miranda Cosgrow', 'ISBN': 98413483, '# Purchased': 23, '# Not checked out': 20, 'Price': 2.49})
database.append({'Title': 'To Kill a Mockingbird', 'Author': 'Drake', 'ISBN': 1002334, '# Purchased': 15, '# Not checked out': 12, 'Price': 5.23})

# Creation of main window buttons
signLibrary = Label(root, text="Welcome to the library. Please choose an option.")
showButton = Button(root, text="Show Library Books", command=showBooks)
addButton = Button(root, text="Add A Book", command=addBook)
editButton = Button(root, text="Edit A Book")
removeButton = Button(root, text="Remove A Book")
quitButton = Button(root, text="Quit", command=root.destroy)

# Layout for main window buttons
signLibrary.grid(row=0, column=2)
showButton.grid(row=2, column=0, pady=6, sticky=W)
addButton.grid(row=3, column=0, pady=6, sticky=W)
editButton.grid(row=4, column=0, pady=6, sticky=W)
removeButton.grid(row=5, column=0, pady=6, sticky=W)
quitButton.grid(row=6, column=0, pady=6, sticky=W)

# Main window loop
root.mainloop()