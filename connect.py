import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\sayom\OneDrive\Documents\Database4.accdb;')
    print("Database is Connected")


except pyodbc.Error:
    print("Error in Connection")


    save,delete, update,view, generate