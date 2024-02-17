from initializer.initializer import Initializer

from ui.mainWindow import MainWindow
from ui.authorizationWindow import AuthorizationWindow


class App:
    def __init__(self):
        Initializer.run()

    def run(self):
        authorizationWindow = AuthorizationWindow()
        authorizationWindow.mainloop()

