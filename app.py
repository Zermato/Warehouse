from ui.mainWindow import MainWindow
from ui.authorizationWindow import AuthorizationWindow


class App:
    def __init__(self):
        ...

    def run(self):
        authorizationWindow = AuthorizationWindow()
        authorizationWindow.mainloop()

