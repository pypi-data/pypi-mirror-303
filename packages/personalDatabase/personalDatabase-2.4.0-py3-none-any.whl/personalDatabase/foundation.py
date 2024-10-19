from . import get_logger

from dotenv import load_dotenv
load_dotenv()

# api_key = os.getenv('api_key')
import psycopg2
from custom_development_standardisation.function_output import *
from psycopg2 import OperationalError,Error



class foundation():
    def __init__(self) -> None:
        self.cursor = None
        self.connection = None
        self.uncommitted_change = None
    
    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def initialise(self,database_name,user=None,host=None,password=None):
        try:
            if user == None and host == None:
                # Determine which database to connect to
                self.connection = psycopg2.connect(
                    database=database_name,
                    port=5433,
                )
                # Create the means to execute commands within the database you connected to
                self.cursor = self.connection.cursor()
                return generate_outcome_message("success","Cursor object has been created...")
            
            else:

                self.connection = psycopg2.connect(
                    database=database_name,
                    user=user,
                    host=host,
                    port=5433,
                    password=password
                )
                self.cursor = self.connection.cursor()
                
                return generate_outcome_message("success","Cursor object has been created...")
            # Attempt to establish a connection  
        
        except OperationalError as e:
            # Print the error message
            return generate_outcome_message("error",e,the_type="others")

    def retrieve(self,command):
        # LOGGING FUNCTIONALITY
        try:
            get_logger().store_log()
        except Exception as e:
            None

        # CORE FUNCTIONALITY
        if self.cursor == None:
            return generate_outcome_message("error","cursor has not been initialised...Run initialise method...",the_type="custom")
        if self.check_for_edit_action(command) == True:
            return generate_outcome_message("error","expect non edit command, but recieved one...",the_type="custom")
        try:
            self.cursor.execute(command)
            outcome = self.cursor.fetchall()
            return generate_outcome_message("success",outcome)
        except Error as e:
            return generate_outcome_message("error",e.pgerror,the_type="others")
    

    def insert(self,command):
        # LOGGING FUNCTIONALITY
        try:
            get_logger().store_log()
        except:
            None
        
        # CORE
        if self.cursor == None:
            return generate_outcome_message("error","cursor has not been initialised...Run initialise method...",the_type="custom")
        edit_type = self.check_for_edit_action(command)
        if edit_type == False or edit_type != "INSERT":
            return generate_outcome_message("error","Command is not an insert command...",the_type="custom")
        try:
            splitted = command.split(" ")
            table_name = splitted[2]
            outcome = self.retrieve(f"select count(*) from {table_name}")
            if outcome["outcome"] == "error":
                return generate_outcome_message("error",outcome["output"],the_type=outcome["the_type"])
            preinsert_count = outcome["output"][0][0]
            
            outcome = self.cursor.execute(command)
            outcome = self.retrieve(f"select count(*) from {table_name}")
            if outcome["outcome"] == "error":
                return generate_outcome_message("error",outcome["output"],the_type=outcome["the_type"])
            postinsert_count = outcome["output"][0][0]
            
            if postinsert_count == preinsert_count:
                return generate_outcome_message("error","something went wrong. Insert did not work. ",the_type="custom")
            self.connection.commit()
            return generate_outcome_message("success","data inserted...")
        except psycopg2.Error as e:
            # Handle errors
            return generate_outcome_message("error",e,the_type="others")
            # print(f"Database error: {e}")
            # self.conn.rollback()  # Rollback any partial changes


    def check_for_edit_action(self,command):
        # LOGGING FUNCTIONALITY
        try:
            get_logger().store_log()
        except:
            None

        # CORE
        command_string = command.upper()  # Convert to uppercase for case-insensitive comparison
        if 'INSERT' in command_string:
            return "INSERT"
        elif 'UPDATE' in command_string:
            return "UPDATE"
        elif 'DELETE' in command_string:
            return "DELETE"
        else:
            return False

    
# x = foundation()
# print(x.initialise("logging_data"))
# print(x.insert("insert into test (something) values (100)"))
# print(x.execute("insert into usage_data (timestamp,specific_utility,utility,function_name) values (TO_TIMESTAMP(1718617100),'test','test','test')"))

