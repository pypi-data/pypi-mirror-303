import os
import pickle 
from sqlalchemy import create_engine, MetaData, Table, and_
from sqlalchemy.sql import column
from pathlib import Path

from utsam.bases.params import _METADATA_


class PgDatabase:
    def __init__(
        self,
        user_name: str = None,
        password: str = None,
        host: str = None,
        db_name: str = None,
        port: str = '5432',
        echo = False,
        engine = None,
    ):
        self.database_type = 'postgresql'
        self.user_name = user_name
        self.password = password
        self.host = host
        self.db_name = db_name
        self.port = port
        self.connection_str = f'{self.database_type}://{self.user_name}:{self.password}@{self.host}:{self.port}/{self.db_name}'
        self.engine = engine
        self.create_engine()

    def execute_sql(self, sql_statement):
        with self.engine.connect() as conn:
            if sql_statement.is_select:
                return conn.execute(sql_statement).fetchall()
            conn.execute(sql_statement)
            conn.commit()

    def create_engine(self):
        if self.engine is None:
            self.engine = create_engine(self.connection_string, pool_size=10, max_overflow=0, echo=False)


class PgTable(PgDatabase):
    def __init__(
        self,
        table_name: str = None,
        user_name: str = None,
        password: str = None,
        host: str = None,
        db_name: str = None,
        port: str = '5432',
        schema: str = "public",
        engine = None
    ):
        super().__init__(
            user_name = user_name,
            password = password,
            host = host,
            db_name = db_name,
            port = port,
            engine = engine,
        )
        self.table_name= table_name
        self.schema = schema
        self.metadata = None
        self.table = None
        self.meta_path = Path.cwd() / _METADATA_
        self.meta_file_name = f'{self.table_name}.metadata'
        self.load_metadata()

    def load_metadata(self):
        if os.path.isfile(self.meta_path / self.meta_file_name):  
            self.reload_metadata()
        else:
            self.metadata = MetaData(schema=self.schema)
            self.metadata.reflect(self.engine, only=[self.table_name])
            self.table = Table(self.table_name, self.metadata, autoload=True, autoload_with=self.engine)

            temp_table = self.table.to_metadata(MetaData())
            with open(self.meta_path / self.meta_file_name, 'wb') as f:
                pickle.dump(temp_table, f)

    def reload_metadata(self):
        with open(self.meta_path / self.meta_file_name, 'rb') as f:
            self.table = pickle.load(f)

    def load_table(self, where_dict: dict = None):
        filters = [column(key) == value for key, value in where_dict.items()]
        stmt = (
            self.table.select().where(and_(*filters))
        )
        return self.execute_sql(sql_statement=stmt)