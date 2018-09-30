
from src import Handler
from src.readers import *

h: Handler = Handler()

h.add_series("Data from CSV", CSVReader("./data.csv"))
h.add_series("Data from CSV only A", CSVReader("./data.csv", filters=[("vid", "A")]))
h.add_series("Data from CSV only B", CSVReader("./data.csv", filters=[("vid", "B")]))
#h.add_series("Data from DB", SQLReader("postgresql://user@localhost:5432/mydb", "SELECT * FROM 'trace-data'", "latitude", "longitude"))

h.run_app()
