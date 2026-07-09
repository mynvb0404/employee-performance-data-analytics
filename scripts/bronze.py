import pandas as pd
from scripts.db import get_engine, save_to_sql

engine = get_engine()

# load data from .csv to dataframe
employee = pd.read_csv('data/employees.csv')
store = pd.read_csv('data/stores.csv')
performance = pd.read_csv('data/monthly_performance.csv')

save_to_sql(employee, 'employee', 'bronze', engine)
save_to_sql(store, 'store', 'bronze', engine, chunk_size=100)
save_to_sql(performance, 'monthly_performance', 'bronze', engine, chunk_size=10000)