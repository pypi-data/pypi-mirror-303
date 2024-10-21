import cx_Oracle
from .Oracle import Oracle
from .SAPHANA import SAPHANA
from .InMemory import InMemory
from .Dremio import Dremio
from .MySql import MySql
from .ExcelFile import ExcelFile
from .Postgress import Postgress
from .MSSQLServer import MSSQLServer
from .Tally import Tally
from .ProteusVision import ProteusVision
from .SnowFlake import SnowFlake
import json
from .UserRights import UserRights
import loggerutility as logger
from flask import request
import commonutility as common
import requests, json, traceback
from .ApplMst import ApplMst
from .Itm2Menu import Itm2Menu

class Generate_Application:

    connection           = None
    dbDetails            = ''
    menu_model           = ''
    

    def get_database_connection(self, dbDetails):
        if dbDetails is not None:
            klass = globals()[dbDetails['DB_VENDORE']]
            dbObject = klass()
            connection_obj = dbObject.getConnection(dbDetails)
        return connection_obj

    def commit(self):
        if self.connection:
            try:
                self.connection.commit()
                logger.log("Transaction committed successfully.")
            except cx_Oracle.Error as error:
                logger.log(f"Error during commit: {error}")
        else:
            logger.log("No active connection to commit.")

    def rollback(self):
        if self.connection:
            try:
                self.connection.rollback()
                logger.log("Transaction rolled back successfully.")
            except cx_Oracle.Error as error:
                logger.log(f"Error during rollback: {error}")
        else:
            logger.log("No active connection to rollback.")

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
                logger.log("Connection closed successfully.")
            except cx_Oracle.Error as error:
                logger.log(f"Error during close: {error}")
        else:
            logger.log("No active connection to close.")

    def genearate_application_with_model(self):
        jsondata = request.get_data('jsonData', None)
        jsondata = json.loads(jsondata[9:])
        logger.log(f"\nJsondata inside Manage_Menu class:::\t{jsondata} \t{type(jsondata)}")

        if "menu_model" in jsondata and jsondata["menu_model"] is not None:
            self.menu_model = jsondata["menu_model"]
            logger.log(f"\nInside menu_model value:::\t{self.menu_model}")

        if "dbDetails" in jsondata and jsondata["dbDetails"] is not None:
            self.dbDetails = jsondata["dbDetails"]
            logger.log(f"\nInside dbDetails value:::\t{self.dbDetails}")

        self.connection = self.get_database_connection(self.dbDetails)

        if self.connection:
            try:
                appl_mst = ApplMst()
                appl_mst.process_data(self.connection, self.menu_model)

                user_rights = UserRights()
                user_rights.process_data(self.connection, self.menu_model)

                itm2menu = Itm2Menu()
                itm2menu.process_data(self.connection, self.menu_model)

                self.commit()
                trace = traceback.format_exc()
                descr = str("Menu application successfully managed")
                returnErr = common.getErrorXml(descr, trace)
                logger.log(f'\n Exception ::: {returnErr}', "0")
                return str(returnErr)

            except Exception as e:
                logger.log(f"Rollback due to error: {e}")
                self.rollback()
                trace = traceback.format_exc()
                descr = str(e)
                returnErr = common.getErrorXml(descr, trace)
                logger.log(f'\n Exception ::: {returnErr}', "0")
                return str(returnErr)
                
            finally:
                logger.log('Closed connection successfully.')
                self.close_connection()
        else:
            logger.log(f'\n In getInvokeIntent exception stacktrace : ', "1")
            trace = traceback.format_exc()
            descr = str("Connection fail")
            returnErr = common.getErrorXml(descr, trace)
            logger.log(f'\n Exception ::: {returnErr}', "0")
            return str(returnErr)


