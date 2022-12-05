from datetime import date, timedelta

from flask import Flask
import pymysql as sql
import pymysql.cursors

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae20295943'
                
#Connecting to the remote database
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
