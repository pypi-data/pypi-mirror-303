from google.cloud.sql.connector import Connector
from sqlalchemy.pool import QueuePool, Pool
import sqlalchemy
import os
import warnings
import pandas as pd
from cryptography.utils import CryptographyDeprecationWarning
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class _DB(BaseModel):
    host: str
    driver: str
    user: str
    password: str
    database: str
    app_name: str | None


class _Engine(BaseModel):
    url: str
    app_name: str | None
    pool_size: int
    max_overflow: int
    query_cache_size: int
    pool_timeout: int
    pool: type[Pool]


class BaseDB:
    """
    Base interface for database operations.
    """
    default_credentials = {
        "host": os.environ["CLOUDSQL_HOST"],
        "driver": "pg8000",
        "user": os.environ["CLOUDSQL_USER"],
        "password": os.environ["CLOUDSQL_PASSWORD"],
        "database": os.environ["CLOUDSQL_DATABASE"],
        "app_name": None,
    }

    def __init__(self, **kwargs) -> None:
        """
        Initialize the BaseDB instance.

        Parameters
        ----------
            url : str, optional
                The database URL. Default is "postgresql+pg8000://".
            app_name : str, optional
                The name of the application.
            pool_size : int, optional
                The size of the connection pool. Default is 10.
            max_overflow : int, optional
                The maximum number of connections to allow in the pool "overflow". Default is 20.
            query_cache_size : int, optional
                The number of queries to cache. Default is 1200.
            pool_timeout : int, optional
                The number of seconds to wait before timing out on getting a connection from the pool. Default is 10.
            pool : type[Pool], optional
                The pool class to use. Default is QueuePool.
            credentials : dict, optional
                A dictionary containing database credentials. If not provided, default_credentials will be pulled from the environment:
            ```python
            {
                "host": os.environ["CLOUDSQL_HOST"],
                "driver": "pg8000",
                "user": os.environ["CLOUDSQL_USER"],
                "password": os.environ["CLOUDSQL_PASSWORD"],
                "database": os.environ["CLOUDSQL_DATABASE"],
                "app_name": None,
            }
        """
        warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

        self.engine_params = _Engine(
            url=kwargs.get("url", "postgresql+pg8000://"),
            app_name=kwargs.get("app_name"),
            pool_size=kwargs.get("pool_size", 10),
            max_overflow=kwargs.get("max_overflow", 20),
            query_cache_size=kwargs.get("query_cache_size", 1200),
            pool_timeout=kwargs.get("pool_timeout", 10),
            pool=kwargs.get("pool", QueuePool),
        )

        self.credentials: _DB = _DB(**kwargs.get("credentials", self.default_credentials))

        self.connector = Connector()

        self.engine = sqlalchemy.create_engine(
            self.engine_params.url,
            creator=self._getconn,
            pool_size=self.engine_params.pool_size,
            max_overflow=self.engine_params.max_overflow,
            query_cache_size=self.engine_params.query_cache_size,
            pool_timeout=self.engine_params.pool_timeout,
            poolclass=self.engine_params.pool,
        )

    def _getconn(self) -> sqlalchemy.engine.base.Connection:
        connection = self.connector.connect(
            self.credentials.host,
            self.credentials.driver,
            user=self.credentials.user,
            password=self.credentials.password,
            db=self.credentials.database,
            application_name=self.credentials.app_name,
        )
        return connection

    def select(self, query: str) -> pd.DataFrame:
        """
        Execute a SELECT query.
        
        Parameters
        ----------
            query : str
                The query to execute.
                
        Returns
        -------
            pd.DataFrame
                A pandas DataFrame containing the results of the query.
        """
        sql_query = sqlalchemy.text(query)
        with self.engine.connect() as connection:
            res = connection.execute(sql_query)
            return pd.DataFrame(
                res.fetchall(), columns=[desc for desc in list(res.keys())]
            )

    def close_connection(self):
        """
        Closes the connection to the database.
        
        ----------------
        
        DONT FORGET TO CLOSE THE CONNECTION AFTER USING THE DATABASE
        
        ----------------
        """
        self.connector.close()
