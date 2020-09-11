import tkinter as tk
from tkinter import ttk
from db import DataBase


db = DataBase('shelf.db')

class BookManager:
    def __init__(self, root):
        self.root = root
        self.root.title('Book Manager')
        self.root.geometry('600x600')

        self.create_widgets()
        self.selected_item = 0
        self.populate_list()


    def create_widgets(self):
        self.name = tk.StringVar()
        self.author = tk.StringVar()

        # head
        self.hframe = tk.Frame(self.root)
        self.lName = tk.Label(self.hframe, text='Name')
        self.eName = tk.Entry(self.hframe, textvariable=self.name)
        self.lAuthor = tk.Label(self.hframe, text='Author')
        self.eAuthor = tk.Entry(self.hframe, textvariable=self.author)
        self.bAddBook = tk.Button(self.hframe, text='Add', command=self.add_book)
        self.bDeleteBook = tk.Button(self.hframe, text='Delete', command=self.delete_book)
        self.bUpdateBook = tk.Button(self.hframe, text='Update', command=self.update_book)
        self.bSearchBook = tk.Button(self.hframe, text='Search', command=self.search_book)

        self.hframe.pack(pady=(0, 10))
        self.lName.grid(row=0, column=0, pady=20, padx=10)
        self.eName.grid(row=0, column=1)
        self.lAuthor.grid(row=0, column=2, padx=10)
        self.eAuthor.grid(row=0, column=3)

        self.bAddBook.grid(row=1, column=0, padx=10)
        self.bDeleteBook.grid(row=1, column=1, pady=10, padx=10)
        self.bUpdateBook.grid(row=1, column=2, pady=10)
        self.bSearchBook.grid(row=1, column=3, pady=10, padx=10)

        # body
        self.bframe = tk.Frame(self.root)
        
        self.book_trv = ttk.Treeview(self.bframe, columns=('ID', 'Name', 'Author'), show='headings', height='20')
        self.book_trv.column('ID', anchor=tk.CENTER)

        self.book_trv.heading('ID', text='Book ID')
        self.book_trv.heading('Name', text='Name')
        self.book_trv.heading('Author', text='Author')

        self.bframe.pack()
        self.book_trv.pack()

        self.book_trv.bind('<ButtonRelease-1>', self.select_item)
        

    def populate_list(self):
        self.book_trv.delete(*self.book_trv.get_children())
        for row in db.fetch():
            self.book_trv.insert('', 'end', values=row)


    def add_book(self):
        # validate entry
        if self.eName.get() == '' or self.eAuthor == '':
            return
        # add into DB
        db.insert(self.eName.get(), self.eAuthor.get())
        # populate book_list
        self.populate_list()
    

    def select_item(self, event):
        try:
            # get selected item
            item = self.book_trv.item(self.book_trv.focus())
            self.selected_item = item['values']
            # set entries
            self.name.set(self.selected_item[1])
            self.author.set(self.selected_item[2])

        except IndexError:
            pass
        

    def delete_book(self):
        db.remove(self.selected_item[0])
        self.populate_list()


    def update_book(self):
        db.update(self.selected_item[0], self.name.get(), self.author.get())
        self.populate_list()


    def search_book(self):
        print('Search')




if __name__ == '__main__':
    root = tk.Tk()
    GUI = BookManager(root)
    root.mainloop()