import psycopg2
import datetime
connection = psycopg2.connect(database="logging_data")
cusor = connection.cursor()



def record_data(table,columns,data):
    x = ','.join(columns)
    y = ','.join(data)
    cusor.execute(f"INSERT INTO {table} ({x}) VALUES ({y})")
    connection.commit()

def retrieveData(command):
    cusor.execute(command)
    rows = cusor.fetchall()
    columnNames = [desc[0] for desc in cusor.description]
    if rows:
         return {
            "column_names": columnNames,    
            "data": rows
         }
    else:
         return False

def retrieveData_v2(command):
    cusor.execute(command)
    rows = cusor.fetchall()
    return rows

