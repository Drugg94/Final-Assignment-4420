# Imports to support functions
from audioop import add
from tkinter import *
from tkinter import messagebox
from os.path import exists
import re
import pickle
from turtle import title

# Creates main window
root = Tk()
root.title("Library Of The Gods!")
root.geometry("600x400")

# Database for books and pickling for database
database = []
file_exists = exists("database.pickle")
if file_exists:
    pickle_off = open("database.pickle","rb")
    database = pickle.load(pickle_off)

# Function that creates a window that displays all books and their availability
def showBooks():
    """Displays books in row by row format"""

    librarySelection = ''
    for i in database:
        librarySelection = librarySelection + i['Title'] + ': ' + str(i['# Not checked out']) + '\n'
    messagebox.showinfo("Title: # Available", librarySelection)

# Function to destroy the window and pickle the database.
def quit():
    """Pickles current database and implements the destroy module for Tk windows"""
    pickling_on = open("database.pickle","wb")
    pickle.dump(database, pickling_on)
    pickling_on.close()
    root.destroy()

# Function to add book to database
def addBook():
    """Creates entry boxes for user to input book information to be added to collection
    
       Output: Outputs book data into database
    """
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
    submButton = Button(top, text="Submit", command=lambda: appendBook(titl1.get(), auth1.get(), isbn1.get(), purch1.get(), avail1.get()))

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
    """Uses entered book data to create book in database.
    
       Parameters: title(string): title of book
       author(string): author of book
       isbn(int): isbn number of book
       purchased(int): number of purchased books
       available(int): number of books available
       """

    if testSpecialAndNum(author):
        messagebox.showerror("ERROR!", "INVALID CHARACTER IN AUTHOR ENTRY! PLEASE RE-ENTER ONLY USING LETTERS!")
        return 0
    elif testLetterAndSpecial(isbn):
        messagebox.showerror("ERROR!", "INVALID CHARACTER IN ISBN ENTRY! PLEASE RE-ENTER ONLY USING NUMBERS!")
        return 0
    elif testLetterAndSpecial(purchased):
        messagebox.showerror("ERROR!", "INVALID CHARACTER IN NUM PURCHASED ENTRY! PLEASE RE-ENTER ONLY USING AN INTEGER EX. 23!")
        return 0
    elif testLetterAndSpecial(available):
        messagebox.showerror("ERROR!", "INVALID CHARACTER IN NUM AVAILABLE ENTRY! PLEASE RE-ENTER ONLY USING AN INTEGER EX. 23!")
        return 0
    else:
        database.append({'Title': title, 'Author': author, 'ISBN': isbn, '# Purchased': purchased, '# Not checked out': available})
        messagebox.showinfo("Confirmation", "Book Added Successfully!")

# Edit book option
def editBook():
    """Finds the book using entered title and edits the database"""
    top = Toplevel()
    top.title("Book Information")
    top.geometry("450x300") 
    titl1 = Label(top, text="Book Title: ")
    titl1Box = Entry(top, width=50)
    titl1Box.insert(0, "Book to be edited")   

    editTitle = Button(top, text="Title", command=lambda: editTitleNow(titl1Box.get(), titleEdit.get()))
    titleEdit = Entry(top, width=50)
    editAuthor = Button(top, text="Author", command=lambda: editAuthorNow(titl1Box.get(), authorEdit.get()))
    authorEdit = Entry(top, width=50)
    editISBN = Button(top, text="ISBN", command=lambda: editISBNNow(titl1Box.get(), isbnEdit.get()))
    isbnEdit = Entry(top, width=50)
    editPurchased = Button(top, text="Purchased", command=lambda: editPurchasedNow(titl1Box.get(), purchasedEdit.get()))
    purchasedEdit = Entry(top, width=50)
    editAvailable = Button(top, text="Available", command=lambda: editAvailableNow(titl1Box.get(), availableEdit.get()))
    availableEdit = Entry(top, width=50)

    titl1.grid(column=0, row=0)
    titl1Box.grid(column=1, row=0)
    editTitle.grid(column=0, row=1)
    titleEdit.grid(column=1, row=1)
    editAuthor.grid(column=0, row=2)
    authorEdit.grid(column=1, row=2)
    editISBN.grid(column=0, row=3)
    isbnEdit.grid(column=1, row=3)
    editPurchased.grid(column=0, row=4)
    purchasedEdit.grid(column=1, row=4)
    editAvailable.grid(column=0, row=5)
    availableEdit.grid(column=1, row=5)

def editTitleNow(title1, newTitle):
    """Edits the title only of book
    
       Parameters:
       title1(string): title of book to be edited.
       newTitle(string): new title of book"""
    for i in database:
        if i['Title'] == title1:
            i['Title'] = newTitle
            messagebox.showinfo("Confirmation", "Title Updated.")
            return 0
    messagebox.showerror("ERROR", "ERROR: NO BOOK MATCHING INPUT TITLE!")
    return 0

def editAuthorNow(title1, newAuthor):
    """Edits the author only of book
    
       Parameters:
       title1(string): title of book to be edited.
       newAuthor(string): new author of book"""
    for i in database:
        if i['Title'] == title1:
            if testSpecialAndNum(newAuthor):
                messagebox.showerror("ERROR!", "INVALID CHARACTER IN AUTHOR ENTRY! PLEASE RE-ENTER ONLY USING LETTERS!")
                return 0
            i['Author'] = newAuthor
            messagebox.showinfo("Confirmation", "Author Updated.")
            return 0
    messagebox.showerror("ERROR", "ERROR: NO BOOK MATCHING INPUT TITLE!")
    return 0

def editISBNNow(title1, newISBN):
    """Edits the ISBN only of book
    
       Parameters:
       title1(string): title of book to be edited.
       newISBN(string): new ISBN of book"""
    for i in database:
        if i['Title'] == title1:
            if testLetterAndSpecial(newISBN):
                messagebox.showerror("ERROR!", "INVALID CHARACTER IN ISBN ENTRY! PLEASE RE-ENTER ONLY USING NUMBERS!")
                return 0
            i['ISBN'] = newISBN
            messagebox.showinfo("Confirmation", "ISBN Updated.")
            return 0
    messagebox.showerror("ERROR", "ERROR: NO BOOK MATCHING INPUT TITLE!")
    return 0

def editPurchasedNow(title1, newPurchased):
    """Edits the Number Purchased only of book
    
       Parameters:
       title1(string): title of book to be edited.
       newPurchased(string): new Number Purchased of book"""
    for i in database:
        if i['Title'] == title1:
            if testLetterAndSpecial(newPurchased):
                messagebox.showerror("ERROR!", "INVALID CHARACTER IN NUM PURCHASED ENTRY! PLEASE RE-ENTER ONLY USING AN INTEGER EX. 23!")
                return 0
            i['# Purchased'] = newPurchased
            messagebox.showinfo("Confirmation", "Purchased Updated.")
            return 0
    messagebox.showerror("ERROR", "ERROR: NO BOOK MATCHING INPUT TITLE!")
    return 0

def editAvailableNow(title1, newAvailable):
    """Edits the Number Available only of book
    
       Parameters:
       title1(string): title of book to be edited.
       newAvailable(string): new Number Available of book"""
    for i in database:
        if i['Title'] == title1:
            if testLetterAndSpecial(newAvailable):
                messagebox.showerror("ERROR!", "INVALID CHARACTER IN NUM AVAILABLE ENTRY! PLEASE RE-ENTER ONLY USING AN INTEGER EX. 23!")
                return 0
            i['# Not checked out'] = newAvailable
            messagebox.showinfo("Confirmation", "Available Updated.")
            return 0
    messagebox.showerror("ERROR", "ERROR: NO BOOK MATCHING INPUT TITLE!")
    return 0

def removeBook():
    """Removes the book from the database"""
    top = Toplevel()
    top.title("Book Deletion")
    top.geometry("450x300") 
    titl1 = Label(top, text="Book Title: ")
    titl1Box = Entry(top, width=50)
    titl1Box.insert(0, "Book to be removed")
    removeButton = Button(top, text="Submit", command=lambda: bookRemoval(titl1Box.get()))

    titl1.grid(column=0, row=0)
    titl1Box.grid(column=1, row=0)
    removeButton.grid(column=0, row=1)

def bookRemoval(title):
    """Finds the book in the database and removes it
    
       Parameter:
          title(string): title of book to be found and removed"""
    for i in range(len(database)):
        if database[i]['Title'] == title:
            del database[i]
            messagebox.showinfo("Confirmation", "Book Removed.")
            return 0
    messagebox.showerror("ERROR", "ERROR: NO BOOK MATCHING INPUT TITLE!")
    return 0

#test function
def testSpecialAndNum(subject):
    """Checks for illegal characters inside user input
    
       Parameter:
          subject(string): String to be checked
          
       Return:
          True if illegal character found/False if none found"""
    if "!" in subject:
        return True
    if "@" in subject:
        return True
    if "#" in subject:
        return True
    if "$" in subject:
        return True
    if "%" in subject:
        return True
    if "^" in subject:
        return True
    if "&" in subject:
        return True
    if "*" in subject:
        return True
    if "*" in subject:
        return True
    if "(" in subject:
        return True
    if ")" in subject:
        return True
    if "0" in subject:
        return True
    if "1" in subject:
        return True
    if "2" in subject:
        return True
    if "3" in subject:
        return True
    if "4" in subject:
        return True
    if "5" in subject:
        return True
    if "6" in subject:
        return True
    if "7" in subject:
        return True
    if "8" in subject:
        return True
    if "9" in subject:
        return True
    return False

def testLetterAndSpecial(subject):
    """Checks for illegal characters inside user input
    
       Parameter:
          subject(string): String to be checked
          
       Return:
          True if illegal character found/False if none found"""
    m = re.compile(r"[a-zA-Z!@%^&.]")

    if re.search(m, subject) == None:
        return False
    else:
        return True

# Creation of main window buttons
signLibrary = Label(root, text="Welcome to the library. Please choose an option.")
showButton = Button(root, text="Show Library Books", command=showBooks)
addButton = Button(root, text="Add A Book", command=addBook)
editButton = Button(root, text="Edit A Book", command=editBook)
removeButton = Button(root, text="Remove A Book", command=removeBook)
quitButton = Button(root, text="Quit", command=quit)

# Layout for main window buttons
signLibrary.grid(row=0, column=2)
showButton.grid(row=2, column=0, pady=6, sticky=W)
addButton.grid(row=3, column=0, pady=6, sticky=W)
editButton.grid(row=4, column=0, pady=6, sticky=W)
removeButton.grid(row=5, column=0, pady=6, sticky=W)
quitButton.grid(row=6, column=0, pady=6, sticky=W)

# Main window loop
root.mainloop()