from . import get_logger

from dotenv import load_dotenv
load_dotenv()

from .foundation import *
from custom_development_standardisation.function_output import *
from log_data import *




class db_utility(foundation):
    def __init__(self) -> None:
        super().__init__()
    
    def count_number_of_distinct_values(self,table_name,column_name):
        try:
            get_logger().store_log()
        except Exception as e:
            None

        # log_function_usage('extract_distinct-database-general_functionality.py')
        outcome = self.execute(f"SELECT COUNT(DISTINCT {column_name}) AS unique_count FROM {table_name};")    
        if outcome["outcome"] == "error":
            return generate_outcome_message("error",outcome["output"],the_type=outcome["the_type"])
        return generate_outcome_message("success",outcome["output"][0][0])
    
    def count_distinct_occurrance(self,table_name,column_name):
        try:
            get_logger().store_log()
        except Exception as e:
            print("failed: ",e)
            None
            
        # log_function_usage('count_number_for_each_distinct-database-general_functionality.py')
        outcome = self.execute(f"SELECT {column_name}, COUNT(*) AS count_per_value FROM {table_name} GROUP BY {column_name} ORDER BY count_per_value DESC;")
        if outcome["outcome"] == "error":
            return generate_outcome_message("error",outcome["output"],the_type=outcome["the_type"])
        reformatted = {}
        for i in outcome["output"]:
            reformatted[i[0]] = i[1]
        
        return generate_outcome_message("success",reformatted)
    
    # def count_distinct_occurrance_within_specific_value_possibility(self,table_name,scope_column,column_count, scope_value):
    #     outcome = self.execute(f"SELECT {column_count}, COUNT(*) AS occurrence_count FROM {table_name} WHERE {scope_column} = '{scope_value}' GROUP BY {column_count}")
    #     if outcome["outcome"] == "error":
    #         return generate_outcome_message("error",outcome["output"],the_type=outcome["the_type"])
    #     return generate_outcome_message("success",outcome["output"])

    

# x = db_utility()
# x.initialise("logging_data")
# outcome = x.count_distinct_occurrance_within_specific_value_possibility("usage_data","timestamp","specific_utility","DATE(2024-04-27)",)
# print(outcome["output"])
