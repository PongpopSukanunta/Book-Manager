import tkinter as tk
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

        self.hframe.pack()
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
        self.book_list = tk.Listbox(self.bframe)
        self.scrollbar = tk.Scrollbar(self.bframe)

        self.bframe.pack(fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')
        self.book_list.pack(side='left', fill='both', expand=True)
              
        # set scrollbar
        self.book_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.book_list.yview)
        
        # bind select
        self.book_list.bind('<<ListboxSelect>>', self.select_item)

    def populate_list(self):
        self.book_list.delete(0, tk.END)
        for row in db.fetch():
            self.book_list.insert(tk.END, row)


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
            self.selected_item = self.book_list.get(tk.ANCHOR)
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