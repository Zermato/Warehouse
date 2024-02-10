from database.database import databaseSession
import customtkinter
from database.queries import SqlQueries
from database.tables import DatabaseTables

from initializer.initializer import g_initializer


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        g_initializer.run()
        self.insert()

        self.title("minimal example app")
        self.minsize(400, 300)
        self._createUIEelements()

    def _createUIEelements(self):
        self.button = customtkinter.CTkButton(master=self, command=self.buttoncallback)
        self.entryLogin = customtkinter.CTkEntry(master=self, placeholder_text="Логин")
        self.entryPassword = customtkinter.CTkEntry(master=self, placeholder_text="Пароль")

        self.entryLogin.pack(padx=20, pady=20)
        self.entryPassword.pack(padx=20, pady=20)
        self.button.pack(padx=20, pady=20)


    def insert(self):
        with databaseSession as db:
            db.execute(SqlQueries.insertIntoTable(DatabaseTables.USERS, args=["Login", "Password"]), data=["l", "p"])

    def buttoncallback(self):
        loginData = self.entryLogin.get()
        passwordData = self.entryPassword.get()
        if len(passwordData) != 0 and len(loginData) != 0:
            with databaseSession as db:
                data = db.getData(SqlQueries.selectFromTable(DatabaseTables.USERS, requestData={"Login": loginData, "Password": passwordData}, args=["Login", "Password"]))
                if data is not None:
                    print("Вошел")
                else:
                    print("Error: No login")
        else:
            print("Error")
