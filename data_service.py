import pymysql
import configparser


class DataService:
    def __init__(self):
        """
        :creates: a new instance of connection and cursor
        reads connection info from config file
        """
        config = configparser.ConfigParser()
        config.read('db.ini')

        host = config['mysql']['host']
        port = 3306
        user = config['mysql']['user']
        password = config['mysql']['passwd']
        database = config['mysql']['db']

        self.conn = pymysql.connect(host=host, user=user, port=port, password=password, db=database)
        self.cursor = self.conn.cursor()

    def get_widget(self, widget_id=None):
        all_widgets = []

        if widget_id is None:
            sql_all_widgets = "select * from widgets order by ID asc"
            self.cursor.execute(sql_all_widgets)
            all_widgets = self.cursor.fetchall()
        else:
            sql_widget_by_id = """select * from widgets where ID = %s"""

            input_values = (widget_id,)
            self.cursor.execute(sql_widget_by_id, input_values)
            all_widgets = self.cursor.fetchone()
        return all_widgets

    def add_widget(self, name, price):
        sql_add_widget = """insert into widgets (Name, Price) values (%s, %s)"""
        input_values = (name, price)
        try:
            self.cursor.execute(sql_add_widget,input_values)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("Attempt to insert a new widget: transaction was rolled back", e)
            return None

        sql_new_widget_id = "select LAST_INSERT_ID()"
        self.cursor.execute(sql_new_widget_id)
        widget_post_id = self.cursor.fetchone()
        return widget_post_id
