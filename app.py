
from src import Handler
from src.readers import *

h: Handler = Handler()

h.add_series("Data from CSV", CSVReader("./data.csv"))

h.run_app()
