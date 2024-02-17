from customtkinter import CTk, CTkButton, CTkEntry

from database.database import databaseSession
from database.queries import SqlQueries
from database.tables import DatabaseTables

from ui.mainWindow import MainWindow

from tools.logger import logger


_log = logger.getLogger(__name__)


class AuthorizationWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(400, 300)
        self._createUIEelements()

    def _createUIEelements(self):
        self.button = CTkButton(master=self, command=self._login)
        self.entryLogin = CTkEntry(master=self, placeholder_text="Логин")
        self.entryPassword = CTkEntry(master=self, placeholder_text="Пароль", show="*")
        self.entryLogin.pack(padx=20, pady=20)
        self.entryPassword.pack(padx=20, pady=20)
        self.button.pack(padx=20, pady=20)

    def _login(self):
        loginData = self.entryLogin.get()
        passwordData = self.entryPassword.get()
        if len(passwordData) != 0 and len(loginData) != 0:
            if self._checkLoginDetails(loginData, passwordData):
                _log.debug("Вошел")
                self.openMainWindow()
            else:
                _log.error("Error: No login")
        else:
            _log.error("Error")

    def _checkLoginDetails(self, login, password):
        with databaseSession as db:
            data = db.getData(SqlQueries.selectFromTable(DatabaseTables.USERS, requestData={"Login": login, "Password": password}, args=["Login", "Password"]))
        return bool(data)

    def openMainWindow(self):
        self.withdraw()
        MainWindow().mainloop()
        self.destroy()
