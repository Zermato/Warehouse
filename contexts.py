from customtkinter import CTkButton, CTkLabel


class Context:
    def __init__(self, window, data):
        self._window = window
        self._data = data

    def clear(self):
        for widget in self._window.winfo_children():
            widget.destroy()
        self._window = None


class MainWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.button1 = CTkButton(master=window, command=self._onButton1)
        self.button2 = CTkButton(master=window)
        self.button1.pack()
        self.button2.pack()

    def _onButton1(self):
        window = self._window
        self.clear()
        window.changeContext(SubContext, {"text": "Label text"})

    def _onButton2(self):
        ...


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
