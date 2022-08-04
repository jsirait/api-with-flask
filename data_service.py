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
