from customtkinter import CTk, CTkLabel


class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        self.minsize(400, 300)

        self.protocol("WM_DELETE_WINDOW", self.onDestroy)

        self._createUIEelements()

    def onDestroy(self):
        print("program is exiting...")
        self.quit()
        self.destroy()

    def _createUIEelements(self):
        label = CTkLabel(master=self, text='Second Window')
        label.pack()
