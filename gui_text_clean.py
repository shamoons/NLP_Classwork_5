# 1. Please read :
# https://docs.python.org/3/library/tkinter.html
# for documentation on how to create GUI

# import libraries
from tkinter import *
import urllib3
from bs4 import BeautifulSoup


class Window(Frame):
    """ Class to handle window"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.html = ''

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Clean Text GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a buttons, entry, textbox instance
        self.entry_url = Entry(width=50)
        self.entry_url.insert(0, "https://en.wikipedia.org/wiki/BookSwim")
        self.get_url = Button(self, text="Get URL", command=self.client_get_url)
        self.quitButton = Button(self, text="Exit", command=self.client_exit)
        self.saveButton = Button(self, text="Save", command=self.save)
        self.t = Text(self, width=40, height=15)

        # placing the button on my window
        self.quitButton.place(x=400, y=260)
        self.saveButton.place(x=320, y=260)
        self.get_url.place(x=420, y=20)
        self.entry_url.place(x=5, y=20)
        self.t.place(x=5, y=40)

    def client_exit(self):
        """Exit function"""
        exit()

    def save(self):
        f = open('output.txt', 'w')
        f.write(self.html)
        f.close()

    def client_get_url(self):
        """ Clean text operations """
        url = self.entry_url.get()
        http = urllib3.PoolManager()
        page = http.request('GET', url)
        soup = BeautifulSoup(page.data, "html.parser")
        self.t.delete(1.0, END)
        for pp in soup.find_all('p'):
            self.html += pp.text
            self.t.insert("end", pp.text)


root = Tk()

# size of the window
root.geometry("500x400")

app = Window(root)
root.mainloop()
