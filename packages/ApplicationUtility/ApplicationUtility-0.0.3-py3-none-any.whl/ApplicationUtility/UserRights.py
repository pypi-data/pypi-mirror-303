import cx_Oracle
import json
from DatabaseConnectionUtility import Oracle 
import loggerutility as logger

class UserRights:

    menu_model = {}

    def check_user_rights(self, application, connection):
        if not connection:
            return False
        cursor = connection.cursor()
        try:
            where_clause = """APPLICATION = :application"""
            cursor.execute(f"SELECT COUNT(*) FROM USER_RIGHTS WHERE {where_clause}", application=application)
            count = cursor.fetchone()[0]
            return count > 0
        except cx_Oracle.Error as error:
            logger.log(f"Error: {error}")
            return False

    def process_data(self, conn, app_model):
        cursor = conn.cursor()
        logger.log(f"Start of UserRights Class")
        self.menu_model = app_model
        application_name = self.menu_model['application']['id']
        logger.log(f"application_name ::: {application_name}")
        exsist = self.check_user_rights(application_name, conn)
        logger.log(f"exsist ::: {exsist}")
        if exsist:
            model_obj_name_list = [i['obj_name'] for i in self.menu_model['navigation']]

            cursor.execute(f"SELECT obj_name FROM USER_RIGHTS WHERE APPLICATION = :application", application=application_name)
            data_obj_name_list = cursor.fetchall()
            for obj_name_list in data_obj_name_list:
                obj_name = obj_name_list[0]
                if obj_name not in model_obj_name_list:
                    raise KeyError(f"Data for APPLICATION: {application_name} having no user rights.")          

            for navigation in self.menu_model['navigation']:
                logger.log(f"navigation ::: {navigation}")
                update_query = """
                    UPDATE USER_RIGHTS SET
                    MENU_ROW = :menu_row, MENU_COL = :menu_col, MENU_SUBCOL = :menu_subcol, LEVEL_4 = :level_4, LEVEL_5 = :level_5
                    WHERE APPLICATION = :application AND OBJ_NAME = :obj_name
                """
                cursor.execute(update_query, {
                    'menu_row': '5',
                    'menu_col': '4',
                    'menu_subcol': '3',
                    'level_4': '1',
                    'level_5': '2',
                    'application': application_name,
                    'obj_name': navigation['obj_name']
                })
        logger.log(f"End of UserRights Class")