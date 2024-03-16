# -*- coding: utf-8 -*-
from odoo import fields, models, _
import pyodbc


class SqlServer(models.Model):
    _name = 'sql.server'

    name = fields.Char(string='Name')
    server = fields.Char(string='Server')
    database = fields.Char(string='Database')
    sql_user = fields.Char(string='SQL User')
    sql_user_password = fields.Char(string='SQL User Password')
    query = fields.Text('Query')

    def run_query(self):
        connection_str = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:' + self.server + ',1433;Database=' + self.database + ';Uid=' + self.sql_user + ';Pwd=' + self.sql_user_password + ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        try:
            conn = pyodbc.connect(connection_str)
            cursor = conn.cursor()
            cursor.execute(f"{self.query}")

            if self.query.strip().upper().startswith("SELECT"):
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            else:
                print("Query executed successfully!")

                # Commit changes (for non-SELECT queries)
            if not self.query.strip().upper().startswith("SELECT"):
                conn.commit()

        except Exception as e:
            message = _(e)
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'success',
                    'sticky': False,
                }
            }
        finally:
            # Close cursor and connection
            cursor.close()
            conn.close()

    def test_sql_connection(self):
        connection_str = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:' + self.server + ',1433;Database=' + self.database + ';Uid=' + self.sql_user + ';Pwd=' + self.sql_user_password + ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        try:
            conn = pyodbc.connect(connection_str)
            conn.close()
            message = _("Connection Test Successful!")
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'success',
                    'sticky': False,
                }
            }

        except Exception as e:
            message = _(e)
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'success',
                    'sticky': False,
                }
            }
