# replace name with dbname
# replace table name

import cx_Oracle
import json
import random
import loggerutility as logger

class Dynamic_Table_Creation:
        
    def check_table_exists(self, table_name, connection):
        if not connection:
            return False
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT COUNT(*) as CNT FROM USER_TABLES WHERE TABLE_NAME = :table_name", table_name=table_name)
            count = cursor.fetchone()[0]
            return count > 0
        except cx_Oracle.Error as error:
            logger.log(f"Error checking APP_NAME existence: {error}")
            return False
        
    def get_table_columns(self, table_name, connection):
        query = f"""SELECT column_name FROM all_tab_columns WHERE table_name = :table_name_upper"""
        cursor = connection.cursor()
        try:
            cursor.execute(query, {'table_name_upper': table_name})
            columns = [row[0] for row in cursor.fetchall()]
            return columns
        except cx_Oracle.Error as error:
            logger.log(f"Error fetching columns for table {table_name}: {error}")
            return False

    def get_missing_column_json(self, json_obj, column_list):
        result = []
        for single_json in json_obj:
            col_name = single_json['column']['db_name']
            key_upper = col_name.upper()
            if key_upper not in column_list:
                result.append(single_json)
        return result
    
    def create_new_table(self, table_name, columns_data, connection):
        columns_sql = []
        unique_column_list = []

        for column in columns_data:
            single_col = column['column']

            col_name = single_col['db_name']
            col_type = single_col['col_type'].upper()
            db_size = single_col.get('db_size', None)
            is_key = single_col.get('key', False)
            mandatory = single_col.get('mandatory', 'false')

            if col_name not in unique_column_list:
                unique_column_list.append(col_name)
                col_def = ''
                if col_type == 'CHAR' and db_size:
                    if db_size == '0':
                        col_def = f"{col_name} {col_type}(10)"  
                    else:
                        col_def = f"{col_name} {col_type}({db_size})"
                
                elif col_type == 'DECIMAL':
                    if db_size != '0':
                        col_def = f"{col_name} DECIMAL({db_size}, 2)"  
                    else:
                        col_def = f"{col_name} DECIMAL(5, 2)"  
                
                elif col_type == 'DATETIME':
                    col_def = f"{col_name} DATE" 

                else:
                    col_def = f"{col_name} {col_type}"  

                if mandatory == 'true':
                    col_def += " NOT NULL"
                    
                if col_def != '':
                    columns_sql.append(col_def)

        columns_sql_str = ", ".join(columns_sql)
        
        create_table_sql = f"CREATE TABLE {table_name} ({columns_sql_str})"
        logger.log(f"{create_table_sql}")

        cursor = connection.cursor()
        try:
            cursor.execute(create_table_sql)
            print(f"Table {table_name} created successfully.")
        except cx_Oracle.Error as error:
            print(f"Error creating table {table_name}: {error}")
            return False

    def alter_table_add_columns(self, table_name, missing_json, connection):
        unique_column_list = []

        for column in missing_json:
            single_col = column['column']

            col_name = single_col['db_name']
            col_type = single_col['col_type'].upper()
            db_size = single_col.get('db_size', None)
            is_key = single_col.get('key', False)
            mandatory = single_col.get('mandatory', 'false')

            if col_name not in unique_column_list:
                unique_column_list.append(col_name)
                col_def = ''
                if col_type == 'CHAR' and db_size:
                    if db_size == '0':
                        col_def = f"{col_name} {col_type}(10)"  
                    else:
                        col_def = f"{col_name} {col_type}({db_size})"
                
                elif col_type == 'DECIMAL':
                    if db_size != '0':
                        col_def = f"{col_name} DECIMAL({db_size}, 2)"  
                    else:
                        col_def = f"{col_name} DECIMAL(5, 2)"  
                
                elif col_type == 'DATETIME':
                    col_def = f"{col_name} DATE" 

                else:
                    col_def = f"{col_name} {col_type}"  

                if mandatory == 'true':
                    col_def += " NOT NULL"

                alter_table_sql = f"ALTER TABLE {table_name} ADD ({col_def})"
                logger.log(f"{alter_table_sql}")

                cursor = connection.cursor()
                try:
                    cursor.execute(alter_table_sql)
                    logger.log(f"Column {col_name} added successfully to table {table_name}.")
                except cx_Oracle.Error as error:
                    logger.log(f"Error adding column {col_name} to table {table_name}: {error}")
                    return False

    def create_alter_table(self, data, connection):
        logger.log(f"Start of Dynamic_Table_Creation Class")
        if "transaction" in data and "sql_models" in data['transaction']:
            for index,sql_models in enumerate(data["transaction"]["sql_models"]):
                columns = sql_models["sql_model"]["columns"]
                table_name = columns[0]['column']['table_name']
                exists = self.check_table_exists(table_name.upper(), connection)
                if exists:
                    current_table_columns = self.get_table_columns(table_name.upper(), connection)
                    missing_json = self.get_missing_column_json(columns, current_table_columns)
                    self.alter_table_add_columns(table_name.upper(),missing_json, connection)
                else:
                    self.create_new_table(table_name.upper(),columns[:15], connection)
            
            logger.log(f"Start of Dynamic_Table_Creation Class")
            return f"Success"

