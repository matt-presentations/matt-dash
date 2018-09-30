
import typing
from .Reader import Reader
import pandas as pd 
from sqlalchemy import create_engine

ConnectionURL = typing.Type[str]

class SQLReader(Reader):

    def __init__(self, url: ConnectionURL, query: str, x_column: str="x", y_column: str="y"):
        self.engine = create_engine(url)
        self.x = x_column 
        self.y = y_column
        self.query = query

    def get_results(self):
        return pd.read_sql_query(self.query, self.engine)
    def get_x(self) -> typing.List[float]:
        return self.get_results()[self.x].tolist()

    def get_y(self) -> typing.List[float]:
        return self.get_results()[self.y].tolist()

    def get_title(self) -> str:
        return ""
