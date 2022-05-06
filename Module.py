from tkinter import *

root = Tk()

database = []

def showBooks():
    for i in database:
        print(i['Title'])

    

database.append({'Title': 'This land is our land', 'Author': 'Miranda Cosgrow', 'ISBN': 98413483, '# Purchased': 23, '# Not checked out': 20, 'Price': 2.49})
database.append({'Title': 'To Kill a Mockingbird', 'Author': 'Drake', 'ISBN': 1002334, '# Purchased': 15, '# Not checked out': 12, 'Price': 5.23})

signLibrary = Label(root, text="Welcome to the library. Please choose an option.")

showButton = Button(text="Show Library Books", command=showBooks)

signLibrary.grid(row=0, column=0)
showButton.grid(row=2, column=2)

root.mainloop()