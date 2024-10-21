import cx_Oracle, json
from DatabaseConnectionUtility import Oracle 
from DatabaseConnectionUtility import Dremio
from DatabaseConnectionUtility import InMemory 
from DatabaseConnectionUtility import Oracle
from DatabaseConnectionUtility import MySql
from DatabaseConnectionUtility import MSSQLServer 
from DatabaseConnectionUtility import SAPHANA
from DatabaseConnectionUtility import Postgress
from DatabaseConnectionUtility import SnowFlake
from .Genmst_Appl import Genmst_Appl
from .Genmst import Genmst
from .Obj_Actions import Obj_Actions
from .Obj_Forms import Obj_Forms
from .Obj_Itemchange import Obj_Itemchange
from .Obj_Links import Obj_Links
from .Pophelp import Pophelp
from .Transetup import Transetup
from .Sd_Trans_Design import Sd_Trans_Design
from .GenerateEditMetadataXML import GenerateEditMetadataXML
from .GenerateBrowMetadataXML import GenerateBrowMetadataXML
from .Dynamic_Table_Creation import Dynamic_Table_Creation
import loggerutility as logger
from flask import request
import traceback
import commonutility as common
from datetime import datetime

class Generate_Transcation:

    connection  =   None

    def get_database_connection(self, dbDetails):        
        if dbDetails != None:
            klass = globals()[dbDetails['DB_VENDORE']]
            dbObject = klass()
            connection_obj = dbObject.getConnection(dbDetails)
                
        return connection_obj

    def commit(self):
        if self.connection:
            try:
                self.connection.commit()
                logger.log(f"Transaction committed successfully.")
            except cx_Oracle.Error as error:
                logger.log(f"Error during commit: {error}")
        else:
            logger.log(f"No active connection to commit.")

    def rollback(self):
        if self.connection:
            try:
                self.connection.rollback()
                logger.log(f"Transaction rolled back successfully.")
            except cx_Oracle.Error as error:
                logger.log(f"Error during rollback: {error}")
        else:
            logger.log(f"No active connection to rollback.")

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
                logger.log(f"Transaction close successfully.")
            except cx_Oracle.Error as error:
                logger.log(f"Error during close: {error}")
        else:
            logger.log(f"No active connection to close.")
        
    def is_valid_json(self, data):
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False
        
    def replace_lookup(self, sql_models, obj_name):
        for sql_model in sql_models:
            if "sql_model" in sql_model and "columns" in sql_model['sql_model']:
                for column in sql_model['sql_model']['columns']:
                    sql_str = column['column']['lookup']
                    if sql_str.startswith("SELECT ") and not self.is_valid_json(sql_str):
                        logger.log(f"lookup in ::: {sql_str}")
                        ques_mark_list = sql_str.split("'?'")
                        sql_input_list = []
                        for lst in ques_mark_list:
                            space_list = lst.split(' ')
                            if len(space_list) > 1:
                                sql_input_list.append(f":{space_list[-3].lower()}")

                        sql_input = ','.join(sql_input_list)
                        logger.log(f"sql_str ::: {sql_input}")

                        json_to_replace = {
                            "field_name": (column['column']['db_name']).upper(),
                            "mod_name": ("w_"+obj_name).upper(),
                            "sql_str": sql_str,
                            "dw_object": "", 
                            "msg_title": "",
                            "width": "", 
                            "height": "",
                            "dist_opt": "",
                            "filter_string": "",
                            "sql_input": sql_input,
                            "default_col": 1, 
                            "pop_align": "", 
                            "query_mode": "",
                            "page_context": "", 
                            "pophelp_cols": "", 
                            "pophelp_source": "",
                            "multi_opt": 0, 
                            "help_option": 2, 
                            "popup_xsl_name": "",
                            "auto_fill_len": 2, 
                            "thumb_obj": "", 
                            "thumb_image_col": "",
                            "thumb_alt_col": "", 
                            "auto_min_length": 2, 
                            "obj_name__ds": "",
                            "data_model_name": "", 
                            "validate_data": "", 
                            "item_change": "",
                            "msg_no": "", 
                            "filter_expr": "", 
                            "layout": "",
                            "chg_date": datetime.now().strftime('%d-%m-%y'),
                            "chg_user": "System",
                            "chg_term": "System"
                            } 

                        column['column']['lookup'] = json_to_replace
        return sql_models
    
    def replace_validation(self, sql_models, obj_name):
        for sql_model in sql_models:
            if "sql_model" in sql_model and "columns" in sql_model['sql_model']:
                for column in sql_model['sql_model']['columns']:
                    if "column" in column and "validations" in column['column']:
                        str_input = column['column']['validations']
                        if str_input.startswith("must_exist"):
                            fld_name = column['column']['db_name']
                            fetched_word = str_input.split("'")[1]
                            error_cd = "V"+str(fld_name[:3].upper())+str(obj_name[:3].upper())+str(fetched_word[:3].upper())

                            msg_str = f"{str(column['column']['descr'])} does't exists"

                            json_to_replace = {
                                "fld_name": fld_name.upper(),
                                "mod_name": ("w_"+obj_name).upper(),
                                "descr": msg_str, 
                                "error_cd": error_cd,
                                "blank_opt": "N", 
                                "fld_type": "C",
                                "fld_min": "", 
                                "fld_max": "", 
                                "val_type": "L",
                                "val_table": "", 
                                "sql_input": "", 
                                "fld_width": "",
                                "udf_usage_1": "", 
                                "udf_usage_2": "", 
                                "udf_usage_3": "",
                                "val_stage": "",
                                "obj_name": "w_"+obj_name,
                                "form_no": sql_model['sql_model']['form_no'],
                                "action": "", 
                                "user_id": "System",
                                "udf_str1_descr": "", 
                                "udf_str2_descr": "", 
                                "udf_str3_descr": "",
                                "exec_seq": "",
                                "chg_date": datetime.now().strftime('%d-%m-%y'),
                                "chg_user": "System",
                                "chg_term": "System"
                            }

                            column['column']['validations'] = json_to_replace
        return sql_models
    
    def replace_obj_itemchange(self,sql_models, object_name):
        try:
            for sql_model in sql_models:
                form_no = sql_model['sql_model'].get('form_no', '') 

                if "sql_model" in sql_model and "columns" in sql_model['sql_model']:
                    for column in sql_model['sql_model']['columns']:
                        item_change = column['column']['item_change']

                        try:
                            obj_name = object_name  
                            field_name = column['column'].get('db_name', '')
                            mandatory = item_change.get('mandatory_server', '')

                            if mandatory.lower() == "yes":
                                mandatory = "Y"
                            elif mandatory.lower() == "no":
                                mandatory = "N"

                            exec_at = item_change.get('itemchange_type', '')
                            if exec_at.lower() == "local":
                                exec_at = "L"
                            elif exec_at.lower() == "server":
                                exec_at = "Z"

                            js_arg = item_change.get('local_file_name', '')

                            output_data = {
                                'obj_name': obj_name,
                                'form_no': form_no,
                                'field_name': field_name,
                                'mandatory': mandatory,
                                'exec_at': exec_at,
                                'js_arg': js_arg
                            }
                            column['column']['item_change'] = output_data

                        except Exception as e:
                            logger.log(f"Error processing column: {e}")
                            continue
            return sql_models

        except Exception as e:
            logger.log(f"Error in replace_obj_itemchange: {str(e)}")
            trace = traceback.format_exc()
            descr = str(e)
            returnErr = common.getErrorXml(descr, trace)
            logger.log(f'Exception: {returnErr}', "0")
            return str(returnErr)

        finally:
            logger.log('Closed connection successfully')
            self.close_connection()

    def enhancement_in_model(self, transaction_model, object_name):

        sql_models = transaction_model["transaction"]["sql_models"]

        sql_models = self.replace_lookup(sql_models, object_name)
        sql_models = self.replace_validation(sql_models, object_name)
        sql_models = self.replace_obj_itemchange(sql_models, object_name)

        transaction_model["transaction"]["sql_models"] = sql_models

        return transaction_model
        
    def genearate_transaction(self, transaction_model, object_name, connection):

        sql_models = transaction_model["transaction"]["sql_models"]

        dynamic_table_creation = Dynamic_Table_Creation()
        dynamic_table_creation.create_alter_table(transaction_model, connection)

        generatebrowmetadataXML = GenerateBrowMetadataXML()
        generatebrowmetadataXML.jsonData = transaction_model
        result = generatebrowmetadataXML.build_xml_str()
        logger.log(f"{result}")

        generateeditmetadataXML = GenerateEditMetadataXML()
        generateeditmetadataXML.jsonData = transaction_model
        result = generateeditmetadataXML.build_xml_str()
        logger.log(f"{result}")

        genmst = Genmst()
        genmst.process_data(connection, sql_models)

        obj_actions = Obj_Actions()
        obj_actions.process_data(connection, sql_models)

        obj_forms = Obj_Forms()
        obj_forms.process_data(connection, sql_models, object_name)

        obj_links = Obj_Links()
        obj_links.process_data(connection, sql_models)

        pophelp = Pophelp()
        pophelp.process_data(connection, sql_models)

        transetup = Transetup()
        transetup.process_data(connection, sql_models, object_name)

        obj_itemchange = Obj_Itemchange()
        obj_itemchange.process_data(connection, sql_models)
        
   