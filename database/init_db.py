import psycopg2
from database import db_configs
from psycopg2.errors import UniqueViolation, InFailedSqlTransaction, InterfaceError, ProgrammingError


class DataBase:
    def __init__(self, database, user, password, host, port):
        self.db_database = database
        self.db_user = user
        self.db_password = password
        self.db_host = host
        self.db_port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        keepalive_kwargs = {
            "keepalives": 1,
            "keepalives_idle": 30,
            "keepalives_interval": 5,
            "keepalives_count": 5,
        }

        self.connection = psycopg2.connect(
            database=self.db_database,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            **keepalive_kwargs
        )
        # to commit automatically
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def execute_update(self, sql_execute, params=None):
        try:
            if params:
                self.cursor.execute(sql_execute, params)
            else:
                self.cursor.execute(sql_execute)
        except UniqueViolation:
            return True
        except InFailedSqlTransaction:
            self.cursor.execute("ROLLBACK")
            self.execute_update(sql_execute, params)
        except InterfaceError:
            self.connect()
            self.execute_update(sql_execute, params)

    def execute_get_one(self, sql_execute, params=None):
        try:
            if params:
                self.cursor.execute(sql_execute, params)
            else:
                self.cursor.execute(sql_execute)
        except UniqueViolation:
            return "UniqueViolation: ", sql_execute, params
        except InFailedSqlTransaction:
            self.cursor.execute("ROLLBACK")
            self.execute_get_one(sql_execute, params)
        except InterfaceError:
            self.connect()
            self.execute_get_one(sql_execute, params)
        try:
            result = self.cursor.fetchone()
        except ProgrammingError:
            return False
        return result

    def execute_get_all(self, sql_execute, params=None):
        try:
            if params:
                self.cursor.execute(sql_execute, params)
            else:
                self.cursor.execute(sql_execute)
        except UniqueViolation:
            return "UniqueViolation: ", sql_execute, params
        except InFailedSqlTransaction:
            self.cursor.execute("ROLLBACK")
            self.execute_get_all(sql_execute, params)
        except InterfaceError:
            self.connect()
            self.execute_get_all(sql_execute, params)
        return self.cursor.fetchall()


db = DataBase(
        db_configs.db_database,
        db_configs.db_user,
        db_configs.db_password,
        db_configs.db_host,
        db_configs.db_port,
    )


