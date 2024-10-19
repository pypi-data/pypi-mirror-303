import psycopg2

connection = None
cursor = None

def create_connection(dbname,user,host,port):
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        host=host,
        port=port
    )

def create_cursor_object():
    cursor = connection.cursor()

def execute_command(command):
    cursor.execute(command)
    rows = cursor.fetchall()
    return rows


