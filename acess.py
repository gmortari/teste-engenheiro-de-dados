import pyodbc 
server = 'localhost' 
database = 'enem' 
username = 'root' 
password = 'enem123' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='
    +database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()