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
