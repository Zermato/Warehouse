from customtkinter import CTkButton, CTkLabel

from .context import Context
from .mainWindow import MainWindowContext


class SubContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.button1 = CTkButton(master=window, command=self._onButton1)
        self.button1.pack()
        CTkLabel(window, text=data["text"]).pack()

    def _onButton1(self):
        window = self._window
        self.clear()
        window.changeContext(MainWindowContext)
