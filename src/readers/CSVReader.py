
import typing
from .Reader import Reader
import pandas as pd 

class CSVReader(Reader):

    def __init__(self, path: str, x_column: str="x", y_column: str="y", filters: typing.List[typing.Tuple[str, typing.Any]] = []):
        self.data = pd.read_csv(path)
        self.x = x_column 
        self.y = y_column
        self.filters = filters

    def filter_data(self, df: pd.DataFrame, filters: typing.List[typing.Tuple[str, typing.Any]]) -> pd.DataFrame:
        for k, v in filters:
            df = df[df[k] == v]
        return df

    def get_x(self) -> typing.List[float]:
        res: pd.Series = self.filter_data(self.data, self.filters)[self.x]
        return res.tolist()

    def get_y(self) -> typing.List[float]:
        return self.filter_data(self.data, self.filters)[self.y].tolist()

    def get_title(self) -> str:
        return ""
