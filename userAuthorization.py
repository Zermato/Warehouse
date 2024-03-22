from database.database import databaseSession
from database.queries import SqlQueries
from database.tables import DatabaseTables


class Authorization:
    @staticmethod
    def login(login, password):
        if len(password) != 0 and len(login) != 0:
            if Authorization._checkLoginDetails(login, password):
                print("Вошел")
                return True
            else:
                print("Error: No login")
                return False
        else:
            print("Error")
            return False

    @staticmethod
    def _checkLoginDetails(login, password):
        with databaseSession as db:
            data = db.getData(SqlQueries.selectFromTable(DatabaseTables.USERS, requestData={"Login": login, "Password": password}, args=["Login", "Password"]))
        return bool(data)
