import cx_Oracle
from datetime import datetime
import loggerutility as logger

class ApplMst:
    sql_models = []

    def check_app_name_exists(self, app_name, conn):
        if not conn:
            return False

        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT COUNT(*) FROM APPL_MST WHERE APP_NAME = :app_name", app_name=app_name)
            count = cursor.fetchone()[0]
            return count > 0
        except cx_Oracle.Error as error:
            logger.log(f"Error checking APP_NAME existence: {error}")
            return False

    def insert_or_update_applmst(self, application,connection):
        if not connection:
            return
        cursor = connection.cursor()

        required_keys = ['id']
        missing_keys = [key for key in required_keys if key not in application]
        logger.log(f"Missing required keys for APPL_MST table: {', '.join(missing_keys)}")

        if missing_keys:
            raise KeyError(f"Missing required keys for APPL_MST table: {', '.join(missing_keys)}")
        else:
            app_name = application.get('id', '')
            app_name = app_name[:3]
            logger.log(f"app_name ::: {app_name}")
            descr = application.get('description', '')[:60]
            chg_date = datetime.now().strftime('%d-%m-%y')
            chg_user = application.get('chg_user', '').strip() or 'System'
            chg_term = application.get('chg_term', '').strip() or 'System'
            appl_group = application.get('group', '')
            appl_color = application.get('theme_color', '')
            appl_order = application.get('appl_order', '')
            conn_option = application.get('conn_option', '')
            appl_type = application.get('appl_type', '')
            search_domain = application.get('search_domain', '')
            appl_grp_descr = application.get('appl_grp_descr', '')
            appl_group_color = application.get('appl_group_color', '')

            exists = self.check_app_name_exists(app_name, connection)
            if exists:
                update_query = """
                    UPDATE APPL_MST SET
                        DESCR = :descr,
                        CHG_DATE = TO_DATE(:chg_date, 'DD-MM-YY'),
                        CHG_USER = :chg_user,
                        CHG_TERM = :chg_term,
                        APPL_GROUP = :appl_group,
                        APPL_COLOR = :appl_color,
                        APPL_ORDER = :appl_order,
                        CONN_OPTION = :conn_option,
                        APPL_TYPE = :appl_type,
                        SEARCH_DOMAIN = :search_domain,
                        APPL_GRP_DESCR = :appl_grp_descr,
                        APPL_GROUP_COLOR = :appl_group_color
                    WHERE APP_NAME = :app_name
                    """
                cursor.execute(update_query, 
                    {'app_name':app_name,
                    'descr':descr,
                    'chg_date':chg_date,
                    'chg_user':chg_user,
                    'chg_term':chg_term,
                    'appl_group':appl_group,
                    'appl_color':appl_color,
                    'appl_order':appl_order,
                    'conn_option':conn_option,
                    'appl_type':appl_type,
                    'search_domain':search_domain,
                    'appl_grp_descr':appl_grp_descr,
                    'appl_group_color':appl_group_color
                    })
                
                logger.log(f"Successfully updated row.")
            else:
                insert_query = """
                    INSERT INTO APPL_MST (
                        APP_NAME, DESCR, CHG_DATE, CHG_USER, CHG_TERM,
                        APPL_GROUP, APPL_COLOR, APPL_ORDER, CONN_OPTION,
                        APPL_TYPE, SEARCH_DOMAIN, APPL_GRP_DESCR, APPL_GROUP_COLOR
                    ) VALUES (
                        :app_name, :descr, TO_DATE(:chg_date, 'DD-MM-YY'), :chg_user, :chg_term,
                        :appl_group, :appl_color, :appl_order, :conn_option,
                        :appl_type, :search_domain, :appl_grp_descr, :appl_group_color
                    )
                    """
                cursor.execute(insert_query, 
                    {'app_name':app_name,
                    'descr':descr,
                    'chg_date':chg_date,
                    'chg_user':chg_user,
                    'chg_term':chg_term,
                    'appl_group':appl_group,
                    'appl_color':appl_color,
                    'appl_order':appl_order,
                    'conn_option':conn_option,
                    'appl_type':appl_type,
                    'search_domain':search_domain,
                    'appl_grp_descr':appl_grp_descr,
                    'appl_group_color':appl_group_color
                    })
                logger.log(f"Successfully inserted row.")

    def process_data(self, conn, menu_model):
        if "application" in menu_model:
            application = menu_model["application"]
            self.insert_or_update_applmst(application, conn)
            
        
