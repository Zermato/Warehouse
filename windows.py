from customtkinter import CTk

from contexts import MainWindowContext, AuthorizationWindowContext


class Window(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainWindow(Window):
    def __init__(self):
        super().__init__()

        self.context = AuthorizationWindowContext(self, None)

    def changeContext(self, contextClass, data=None):
        self.context = contextClass(self, data)
