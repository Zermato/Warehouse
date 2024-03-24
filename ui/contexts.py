from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkFrame

from userAuthorization import Authorization
from settingsConfig import g_settingsConfig


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
        self.userRoleFrame = CTkFrame(window)
        self.userRoleFrame.grid(row=0, column=0, padx=10, pady=10)
        self.userRoleLabel = CTkLabel(self.userRoleFrame, text=g_settingsConfig.role, font=("Helvetica", 30))
        self.userRoleLabel.pack(padx=10, pady=10)

        self.buttonFrame = CTkFrame(window)
        self.buttonStorage = CTkButton(self.buttonFrame, text="Склад", font=("Helvetica", 30), command=self._onButtonStorage)
        self.buttonParish = CTkButton(self.buttonFrame, text="Приход", font=("Helvetica", 30), command=self._onButtonParish)
        self.buttonExpense = CTkButton(self.buttonFrame, text="Расход", font=("Helvetica", 30), command=self._onButtonExpense)
        self.buttonService = CTkButton(self.buttonFrame, text="Сервис", font=("Helvetica", 30), command=self._onButtonService)
        self.buttonFrame.grid(row=0, column=1, padx=10, pady=10)
        self.buttonStorage.grid(row=0, column=0, padx=10, pady=10)
        self.buttonParish.grid(row=0, column=1, padx=10, pady=10)
        self.buttonExpense.grid(row=0, column=2, padx=10, pady=10)
        self.buttonService.grid(row=0, column=3, padx=10, pady=10)

        self.exitFrame = CTkFrame(window)
        self.buttonExit = CTkButton(self.exitFrame, text="Выйти", font=("Helvetica", 30), command=self._onButtonExit)
        self.exitFrame.grid(row=0, column=2, padx=10, pady=10)
        self.buttonExit.pack(padx=10, pady=10)

    def _onButtonStorage(self):
        window = self._window
        self.clear()
        window.changeContext(SubContext, {"text": "Label text"})

    def _onButtonParish(self):
        ...

    def _onButtonExpense(self):
        ...

    def _onButtonService(self):
        ...

    def _onButtonExit(self):
        self._window.close()


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
