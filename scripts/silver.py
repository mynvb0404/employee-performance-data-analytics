from scripts.db import get_engine, load_from_sql, save_to_sql

engine = get_engine()

employee = load_from_sql('employee', 'bronze',engine=engine)
store = load_from_sql('store', 'bronze',engine=engine)
performance = load_from_sql('monthly_performance', 'bronze',engine=engine)

print('employee table shape: {}'.format(employee.shape))
print('store table shape: {}'.format(store.shape))
print('monthly_performance table shape: {}'.format(performance.shape))