from tkinter import *

class Application(Frame):
    """Aplikacja oparta na GUI z trzema przyciskami"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        """Utworz przycisk"""
        self.instLbl = Label(self, text = 'Wprowadz haslo do sekretu dlugowiecznosci')
        self.instLbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.pwLbl = Label(self, text = 'Hasło: ')
        self.pwLbl.grid(row = 1, column = 0, sticky = W)

        #entry
        self.pwEnt = Entry(self)
        self.pwEnt.grid(row = 1, column = 1, sticky = W)

        self.submitBttn = Button(self, text='Akceptuj', command = self.reveal)
        self.submitBttn.grid(row = 2, column = 0, sticky = W)

        self.secretTxt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secretTxt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        contents = self.pwEnt.get()
        if contents == 'sekret':
           message = 'Oto tajemny przeps'
        else:
            message = 'Nie poprawne haslo'
        self.secretTxt.delete(0.0, END)
        self.secretTxt.insert(0.0, message)


#main
root = Tk()
root.title('Przyciski')
root.geometry('300x185')

app = Application(root)

root.mainloop()

