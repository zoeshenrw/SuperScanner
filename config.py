from datetime import date, timedelta

from flask import Flask
import pymysql as sql
import pymysql.cursors

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae20295943'
                
#Connecting to the remote database
conn = sql.connect(host='sql.freedb.tech',
                   user='freedb_nyudb',
                   password='5?G3$vJ7c$8QSz4',
                   db='freedb_scannerdb',
                   unix_socket='',
                   charset='utf8mb4',
                   cursorclass=pymysql.cursors.DictCursor
                )
from register import register_bp
app.register_blueprint(register_bp, url_prefix="/register")
