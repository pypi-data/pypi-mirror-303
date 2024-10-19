# from data_extractor import log_function_usage
import psycopg2

connection = psycopg2.connect(database="data")
cusor = connection.cursor()
## Description: 

def addRowData(tableName,columns,info):
    # log_function_usage('addRowData-database-actions.py')
    if len(columns) != len(info):
            return False
    commaSeparatedColumns = ",".join([str(item) for item in columns])
    commaSeparatedData = ",".join([str(item) for item in info])
    cusor.execute(f"INSERT INTO {tableName} ({commaSeparatedColumns}) VALUES ({commaSeparatedData})")
    connection.commit()

# Assumption: You are adding the same data to a single column for a range of id.
def addColumnData(tableName, columnName, data, id_beginning_range, id_ending_range):
    # log_function_usage('addColumnData-database-actions.py')
    cusor.execute(f"UPDATE {tableName} SET {columnName}={data} WHERE id BETWEEN {id_beginning_range} AND {id_ending_range}")
    connection.commit()

def createTable(table_name, column_dict):
    # log_function_usage('createTable-database-actions.py')
    # Create the CREATE TABLE query dynamically
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for column_name, data_type in column_dict.items():
        create_table_query += f"{column_name} {data_type}, "
    create_table_query = create_table_query[:-2] + ");"
    # Execute the CREATE TABLE query
    cusor.execute(create_table_query)
    # Commit the transaction
    connection.commit()

def retrieveData(command):
    # log_function_usage('retrieveData-database-actions.py')
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

## Objective: Facilitate the adding of data
##    - Ensure data type matches database column data type
##    - Specify column name componnent of the sql command. 
def getColumns(table_name):
    # log_function_usage('getColumns-database-actions.py')
    cusor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = %s", (table_name,))
    return cusor.fetchall()

def getTables():
    # log_function_usage('getTables-database-actions.py')
    cusor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    return cusor.fetchall()

def link_id(tableToUpdate,tableToGetID,columnToUpdate,columnToCompare):
    # log_function_usage('link_id-database-actions.py')
    cusor.execute(f"""UPDATE {tableToUpdate} AS r
                        SET {columnToUpdate} = i.id
                        FROM {tableToGetID} AS i
                        WHERE r.{columnToCompare} = i.{columnToCompare};
                   """)
    return True 

def get_rows_based_on_date(tableName, columnName, date):
    cusor.execute(f"select * from {tableName} where DATE({columnName}) = '{date}' ORDER BY {columnName}")
    rows = cusor.fetchall()
    columnNames = [desc[0] for desc in cusor.description]
    if rows:
         return {
            "column_names": columnNames,    
            "data": rows
         }
    else:
         return False
    

