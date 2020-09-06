import tkinter as tk

class BookManager:
    LIST = ['mindset by Dr.Carol S. Dweck']
    def __init__(self, root):
        self.root = root
        self.root.title('Book Manager')
        self.root.geometry('600x600')

        self.name = tk.StringVar()
        self.author = tk.StringVar()

        # head
        self.hframe = tk.Frame(self.root)
        self.lName = tk.Label(self.hframe, text='Name')
        self.eName = tk.Entry(self.hframe, textvariable=self.name)
        self.lAuthor = tk.Label(self.hframe, text='Author')
        self.eAuthor = tk.Entry(self.hframe, textvariable=self.author)
        self.bsubmit = tk.Button(self.hframe, text='Add This Book', command=self.add_book)

        self.hframe.pack()
        self.lName.grid(row=0, column=0, pady=20, padx=10)
        self.eName.grid(row=0, column=1)
        self.lAuthor.grid(row=0, column=2, padx=10)
        self.eAuthor.grid(row=0, column=3)
        self.bsubmit.grid(row=0, column=4, padx=10)

        # body
        self.bframe = tk.Frame(self.root)
        self.listbox = tk.Listbox(self.bframe)
        self.scrollbar = tk.Scrollbar(self.bframe)

        self.bframe.pack(fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')
        self.listbox.pack(side='left', fill='both', expand=True)
              

    def insert_to_listbox(self, book): # change to populate listbox from Data Base
        self.listbox.insert(tk.END, book)

    def add_book(self): # need to add to Data Base
        book = f'{self.name.get()} by {self.author.get()}'
        print(book)
        self.insert_to_listbox(book)

if __name__ == '__main__':
    root = tk.Tk()
    GUI = BookManager(root)
    root.mainloop()