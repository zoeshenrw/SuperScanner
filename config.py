from datetime import date, timedelta

from flask import Flask
import pymysql as sql
import pymysql.cursors

#from google.cloud.sql.connector import Connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae20295943'
# cloud database in Google
# conn=Connector.connect(
#    "project:region:instance",
#    "pymysql",
#    user="root",
#    password="",
#    db="ScannerDB"
# )

#conn = sql.connect(host='127.0.0.1',
#                   user='root',
#                   password='',
#                   db='ScannerDB',
#                   unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
#                   charset='utf8mb4',
#                  cursorclass=pymysql.cursors.DictCursor
#               )
                
conn = sql.connect(host='sql9.freesqldatabase.com',
                   user='sql9581619',
                   password='zYJJENMhQC',
                   db='sql9581619',
                   unix_socket='',
                   charset='utf8mb4',
                   cursorclass=pymysql.cursors.DictCursor
                )
from register import register_bp
app.register_blueprint(register_bp, url_prefix="/register")
