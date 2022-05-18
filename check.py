import pyodbc

msa_drivers = [x for x in pyodbc.drivers() if 'access']
print(f'MS-ACCES Drivers: {msa_drivers}')

