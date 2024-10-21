# for 21.xml

import json
import loggerutility as logger

class GenerateEditMetadataXML:

    header = '''<?xml version="1.0" encoding="UTF-8"?>
                <!DOCTYPE Sybase_eDataWindow>
                <Sybase_eDataWindow>
                    <Release>9</Release>
                    <BaseDefinition>
                        <units>1</units>
                        <timer_interval>0</timer_interval>
                        <color>79741120</color>
                        <processing>0</processing>
                        <HTMLDW>no</HTMLDW>
                        <print>
                            <documentname></documentname>
                            <printername></printername>
                            <orientation>0</orientation>
                            <margin>
                                <left>24</left>
                                <right>24</right>
                                <top>24</top>
                                <bottom>24</bottom>
                            </margin>
                            <paper>
                                <source>0</source>
                                <size>0</size>
                            </paper>
                            <prompt>no</prompt>
                            <canusedefaultprinter>yes</canusedefaultprinter>
                            <buttons>no</buttons>
                            <preview.buttons>no</preview.buttons>
                            <cliptext>no</cliptext>
                            <overrideprintjob>no</overrideprintjob>
                        </print>
                    </BaseDefinition>
                    <Summary>
                        <height>0</height>
                        <color>536870912</color>
                    </Summary>
                    <Footer>
                        <height>0</height>
                        <color>536870912</color>
                    </Footer>
                    <Detail>
                        <height>523</height>
                        <color>536870912</color>
                    </Detail>'''

    footer = '''<HtmlTable>
                    <border>1</border>
                </HtmlTable>
                <HtmlGen>
                    <clientevents>1</clientevents>
                    <clientvalidation>1</clientvalidation>
                    <clientcomputedfields>1</clientcomputedfields>
                    <clientformatting>0</clientformatting>
                    <clientscriptable>0</clientscriptable>
                    <generatejavascript>1</generatejavascript>
                    <encodeselflinkargs>1</encodeselflinkargs>
                    <netscapelayers>0</netscapelayers>
                </HtmlGen>
                <Export.XML>
                    <headgroups>1</headgroups>
                    <includewhitespace>0</includewhitespace>
                    <metadatatype>0</metadatatype>
                    <savemetadata>0</savemetadata>
                </Export.XML>
                <Import.XML>
                </Import.XML>
                <Export.PDF>
                    <method>0</method>
                    <distill.custompostscript>0</distill.custompostscript>
                    <xslfop.print>0</xslfop.print>
                </Export.PDF>
            </Sybase_eDataWindow>
        '''

    jsonData = {}

    def get_Table_Column(self, column_detail):
        # inside tableDefinition tag
         
        initial_tag = f"<initial>{column_detail['default_value']}</initial>" if len(column_detail['default_value']) != 0 else "" 
        
        table_column_tag   = f'''<table_column>
                                        <type size="{column_detail['db_size']}">{column_detail['col_type'].lower()}</type>
                                        <name>{column_detail['db_name'].lower()}</name>
                                        <dbname>{column_detail['table_name'].lower()}.{column_detail['db_name'].lower()} </dbname>
                                        {initial_tag}
                                </table_column>'''
        return table_column_tag
    
    def get_Text_Object(self, column_detail, x, y):
        
        # visible_tag = "<visible>1</visible>" if column_detail['HIDDEN'] == "" or column_detail['HIDDEN'] == "true"   else "<visible>0</visible>"
        
        text_object_tag = f'''<TextObject>
                                    <band>Detail</band>
                                    <alignment>1</alignment>
                                    <text>{column_detail['heading']}</text>
                                    <border>0</border>
                                    <color>0</color>
                                    <x>{x}</x>
                                    <y>{y}</y>
                                    <height>15</height>
                                    <width>200</width>
                                    <html>
                                        <valueishtml>0</valueishtml>
                                    </html>
                                    <name>{column_detail['db_name'].lower()}_t</name>
                                    <visible>{column_detail['hidden']}</visible>
                                    <font>
                                        <face>Times New Roman</face>
                                        <height>-10</height>
                                        <weight>400</weight>
                                        <family>1</family>
                                        <pitch>2</pitch>
                                        <charset>0</charset>
                                    </font>
                                    <background>
                                        <mode>2</mode>
                                        <color>79741120</color>
                                    </background>
                            </TextObject>'''
        
        return text_object_tag
        
    def get_Column_Object(self, column_detail, x, y, tabsequence):
        # visible_tag = "<visible>1</visible>" if column_detail['HIDDEN'] == "" or column_detail['HIDDEN'] == "true"   else "<visible>0</visible>"
        # format_tag      = column_detail['FORMAT'] if len(column_detail['FORMAT']) != 0 else "[general]"
        tabsequence_tag = ""
        if 'protect' in column_detail.keys():
            if column_detail['protect'] == "true" :
                tabsequence_tag = f"<tabsequence>32766</tabsequence>"
            else:
                tabsequence_tag = f"<tabsequence>{tabsequence}<tabsequence>"
                tabsequence+=10
        
        column_object_tag = f'''<ColumnObject>
                                    <band>Detail</band>
                                    <id>2</id>
                                    <alignment>0</alignment>
                                    {tabsequence_tag}
                                    <border>5</border>
                                    <color>0</color>
                                    <x>{x}</x>
                                    <y>{y}</y>
                                    <height>15</height>
                                    <width>200</width>
                                    <format>{column_detail['format']}</format>
                                    <html>
                                        <valueishtml>0</valueishtml>
                                    </html>
                                    <name>{column_detail['db_name'].lower()}</name>
                                    <visible>{column_detail['hidden']}</visible>
                                    <EditStyle style="edit">
                                        <limit>10</limit>
                                        <case>upper</case>
                                        <focusrectangle>no</focusrectangle>
                                        <autoselect>yes</autoselect>
                                        <imemode>0</imemode>
                                    </EditStyle>
                                    <font>
                                        <face>Times New Roman</face>
                                        <height>-10</height>
                                        <weight>400</weight>
                                        <family>1</family>
                                        <pitch>2</pitch>
                                        <charset>0</charset>
                                    </font>
                                    <background>
                                        <mode>2</mode>
                                        <color>16777215</color>
                                    </background>
                            </ColumnObject>'''
        
        return column_object_tag, tabsequence
        
    def get_groupBox_Object(self, column_detail, x, y, group_name): 
        group_object_tag = f'''<GroupBox>
                                    <band>Detail</band>
                                    <text>{group_name}</text>
                                    <border>2</border>
                                    <color>33554432</color>
                                    <x>{x}</x>
                                    <y>{y}</y>
                                    <height>419</height>
                                    <width>651</width>
                                    <name>gb_1</name>
                                    <visible>1</visible>
                                    <font>
                                        <face>Liberation Sans</face>
                                        <height>-11</height>
                                        <weight>400</weight>
                                        <family>2</family>
                                        <pitch>2</pitch>
                                        <charset>0</charset>
                                    </font>
                                    <background>
                                        <mode>2</mode>
                                        <color>1073741824</color>
                                    </background>
                            </GroupBox>'''
            
        return group_object_tag

    def retrival_query(self, sqlModel, column_detail, argument_list):
        sql_query = ""
        columns   = []

        # for column in column_detail['column']:
        # if column_detail['checked'] == 'true' and not column_detail['default_function']:    # Original

        if not column_detail['default_function']:
            alias = column_detail['name']
            col = f"{column_detail['table_name']}.{column_detail['db_name']}"
            columns.append(f"{col} AS {alias}")
        
        # Extract joins that are not on the same table
        joins = []
        # base_table = jsonData['sql_model']['columns'][0]['column'][0]['table_name'] # original
        
        base_table = sqlModel['columns'][0]['column']['table_name']
        
        if "joins" in sqlModel and "join_predicates" in sqlModel['joins'] and "joins" in sqlModel['joins']['join_predicates']:
            for join in sqlModel['joins']['join_predicates']['joins']:
                if join['main_table'] == 'true' and join['join_table'] and join['table'] != join['join_table']:
                    joins.append(f"JOIN {join['join_table']} ON {join['table']}.{join['column']} = {join['join_table']}.{join['join_column']}")
            
        # Construct SQL query
        sql_query = f"SELECT {', '.join(columns)}\n FROM {base_table}\n"
        if joins:
            sql_query += ' '.join(joins)
        
        for argument_detail in argument_list:
            tableName = argument_detail[argument_detail.find("<table_name>") + 12 : argument_detail.find("</table_name>")]
            columnName = argument_detail[argument_detail.find("<name>") + 6 : argument_detail.find("</name>")]
            if "WHERE" in sql_query :
                sql_query += f" AND {tableName}.{columnName} = ? "
            else:
                sql_query += f" WHERE {tableName}.{columnName} = ? "
        return sql_query

    def get_argument_list(self, column_detail):
        argument_object_list = []
        if column_detail['key'] == "true" :
            tableName           = column_detail['table_name'].lower()
            column_Name         = column_detail['db_name'].lower()
            column_Datatype     = column_detail['col_type'].lower()
            if column_Datatype == "char" or column_Datatype == "varchar2":
                column_Datatype = "string"
            
            argument_tags       = f'''<argument>
                                        <table_name>{tableName}</table_name>
                                        <name>{column_Name}</name>
                                        <type>{column_Datatype}</type>
                                    </argument>'''
            argument_object_list.append(argument_tags)
        return argument_object_list

    def get_join_object(self, sqlModel, column_detail):
        update_tag_list      = []
        update_tag           = ""
  
        if "joins" in sqlModel and "join_predicates" in sqlModel['joins'] and "joins" in sqlModel['joins']['join_predicates']:
            join_Data_list       = sqlModel['joins']['join_predicates']['joins']
        
            if len(join_Data_list) == 1:
                update_tag = f'''<update>yes</update>
                                         <updatewhereclause>yes</updatewhereclause>
                                         <update>{each_join_detail['table'].lower()}</update>'''
                update_tag_list.append(update_tag)
                
            else:    
                for each_join_detail in join_Data_list :
                    if each_join_detail['main_table'] == "true" :
                        update_tag = f'''<update>yes</update>
                                         <updatewhereclause>yes</updatewhereclause>
                                         <update>{each_join_detail['table'].lower()}</update>'''
                        
                        update_tag_list.append(update_tag)
        else:
            update_tag = f'''<update>yes</update>
                             <updatewhereclause>yes</updatewhereclause>
                             <update>{column_detail['table_name'].lower()}</update>'''
    
            update_tag_list.append(update_tag)
            
        return update_tag_list
            
    def build_xml_str(self):

        x                     = 10
        y                     = 10
        tabsequence           = 10
        previous_group_name   = ""
        current_group_name    = ""
        tableColumn_list      = []
        textObject_list       = []
        columnObject_list     = []
        groupObject_list      = []
        retreival_query_list  = []
        final_XML             = ""
        
        for sqlmodels_list in self.jsonData["transaction"]["sql_models"]:
            for index, column_detail in enumerate(sqlmodels_list['sql_model']['columns']) :# [0]['column']):
                tableColumn     = self.get_Table_Column(column_detail['column'])
                tableColumn_list.append(tableColumn)
                y+=10
                
                textObject      = self.get_Text_Object(column_detail['column'], x, y)
                textObject_list.append(textObject)
                y+=10
                
                columnObject, tabsequence      = self.get_Column_Object(column_detail['column'], x, y, tabsequence)
                columnObject_list.append(columnObject)
    
                current_group_name = column_detail['column']['group_name']                                              # not working vala  -- self.jsonData['SQLModel']['COLUMNS'][0]['COLUMN']
                if (previous_group_name != "" and current_group_name != "" and previous_group_name is not current_group_name ) or len(column_detail['column']) - 1 == index : # len(self.jsonData['SQLModel']['COLUMNS'][0]['COLUMN']) - 1 == index :
                    y+=10
                    group_name       = previous_group_name
                    groupObject      = self.get_groupBox_Object(column_detail['column'], 5, y, group_name)
                    groupObject_list.append(groupObject) 
                previous_group_name = current_group_name 

                argument_list         = self.get_argument_list(column_detail['column'])
                retreival_query       = self.retrival_query(sqlmodels_list['sql_model'], column_detail['column'], argument_list) 
                update_tag_list       = self.get_join_object(sqlmodels_list['sql_model'], column_detail['column'])
                
            final_XML       = ( self.header + "\n" 
                                    + "<TableDefinition>"             + "\n"
                                    + "\n".join(tableColumn_list)     + "\n" 
                                    + "<retrieve>" + retreival_query  + "</retrieve> \n"
                                    + "\n".join(update_tag_list)      
                                    + "\n".join(argument_list)        + "\n"
                                    + "</TableDefinition>"  
                                    + "\n".join(textObject_list)      + "\n" 
                                    + "\n".join(columnObject_list)    + "\n" 
                                    + "\n".join(groupObject_list)     + "\n" 
                                    + self.footer ) 
            
            fileName     = f"output2{sqlmodels_list['sql_model']['form_no']}.xml"
            finalMessage = self.create_XML_file(fileName, final_XML)
        return finalMessage
     
    def create_XML_file(self, fileName, final_XML_str):
        filePath = "XML/"
        with open(filePath + fileName, "w") as file:
            file.write(final_XML_str)
            return f" New '{fileName}' file written and saved successfully."


