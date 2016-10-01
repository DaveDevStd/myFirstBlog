from tkinter import *

class Application(Frame):
    """Aplikacja oparta na GUI z trzema przyciskami"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttnClicks = 0
        self.createWidgets()

    def createWidgets(self):
        """Utworz przycisk"""
        self.bttn = Button(self)
        self.bttn['text'] = 'Liczba klikniec: 0'
        self.bttn['command'] = self.updateCount
        self.bttn.grid()

    def updateCount(self):
        self.bttnClicks += 1
        self.bttn['text'] = 'Liczba kliknięć: ' + str(self.bttnClicks)



#main
root = Tk()
root.title('Przyciski')
root.geometry('210x85')

app = Application(root)

root.mainloop()

