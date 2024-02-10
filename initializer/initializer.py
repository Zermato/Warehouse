import os
from pathlib import Path

from database.queries import SqlQueries as ds
from database.tables import DatabaseTables
from settingsConfig import settingsConfig
from database.pipeline import DatabasePipeline
from .queries import SqlQueries
from .consts import Constants
from tools.fileSystem import FileSystem


class _Initializer:
    @staticmethod
    def initializeDatabase():
        databaseCreationPipeline = DatabasePipeline()
        databaseCreationPipeline.addOperation(SqlQueries.applyingSettings)
        databaseCreationPipeline.addOperation(SqlQueries.createTableUsers)
        databaseCreationPipeline.addOperation(SqlQueries.createTableRoles)
        databaseCreationPipeline.run()

    @staticmethod
    def initializeDatabaseData():
        record = DatabasePipeline()
        record.addOperation(ds.insertIntoTable(DatabaseTables.ROLES, ["Name"]), ["Admin"])
        record.run()

    @staticmethod
    def run():
        if not FileSystem.exists(Constants.DATA_DIRECTORY):
            FileSystem.makeDir(Constants.DATA_DIRECTORY)
        if not FileSystem.exists(Path(Constants.DATA_DIRECTORY) / settingsConfig.DatabaseSettings["database"]):
            print("call create")
            _Initializer.initializeDatabase()
            _Initializer.initializeDatabaseData()


g_initializer = _Initializer()
