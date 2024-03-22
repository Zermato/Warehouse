from initializer.initializer import Initializer
from ui.windows import MainWindow


class App:
    def __init__(self):
        Initializer.run()

    def run(self):
        window = MainWindow()
        window.mainloop()
