from database.database import databaseSession
from database.queries import SqlQueries
from database.tables import DatabaseTables


class Authorization:
    def __init__(self):
        self._roleID = None

    def login(self, login, password):
        if len(password) != 0 and len(login) != 0:
            if self._checkLoginDetails(login, password):
                print("Вошел")
                return True
            else:
                print("Error: No login")
                return False
        else:
            print("Error")
            return False

    def _checkLoginDetails(self, login, password):
        with databaseSession as db:
            data = db.getData(SqlQueries.selectFromTable(DatabaseTables.USERS, requestData={"Login": login, "Password": password}, args=["Login", "Password", "RoleID"]))
        if bool(data):
            self._roleID = data[-1]
        return bool(data)

    @property
    def role(self):
        with databaseSession as db:
            data = db.getData(SqlQueries.selectFromTable(DatabaseTables.ROLES, requestData={"ID": self._roleID}, args=["Name"]))
        return data[0]


g_authorization = Authorization()
