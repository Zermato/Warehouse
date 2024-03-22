from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkFrame

from userAuthorization import Authorization


class Context:
    def __init__(self, window, data):
        self._window = window
        self._data = data

    def clear(self):
        for widget in self._window.winfo_children():
            widget.destroy()
        self._window = None


class AuthorizationWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.button = CTkButton(master=window, command=self._login)
        self.entryLogin = CTkEntry(master=window, placeholder_text="Логин")
        self.entryPassword = CTkEntry(master=window, placeholder_text="Пароль", show="*")
        self.entryLogin.pack(padx=20, pady=20)
        self.entryPassword.pack(padx=20, pady=20)
        self.button.pack(padx=20, pady=20)

    def _login(self):
        window = self._window
        if Authorization.login(self.entryLogin.get(), self.entryPassword.get()):
            self.clear()
            window.changeContext(MainWindowContext)


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
