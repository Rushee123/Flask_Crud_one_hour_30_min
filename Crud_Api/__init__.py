from flask import Flask,request,jsonify
from flask_mysqldb import MySQL
import urllib.parse
from sqlalchemy import create_engine
from flask_cors import CORS
import os,sys
import json

def read_config():
    with open(r'C:\Users\rusha\Desktop\Auth_Practical\Auth_Api\config.json') as data:
        data = data.read()

    data = json.loads(data)
    return data

app = Flask(__name__)
CORS(app,supports_credentials=True)
server_config = read_config()
server_ip = server_config['server_ip']
app_port = server_config['port']
app.config['MYSQL_HOST'] = server_config['mysql_congig']['host']
app.config['MYSQL_USER'] = server_config['mysql_congig']['user']
app.config['MYSQL_PASSWORD'] = server_config['mysql_congig']['password']
app.config['MYSQL_DB'] = server_config['mysql_congig']['database']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = 'myapp'

mysql = MySQL(app)
user = server_config['mysql_congig']['user']
password = server_config['mysql_congig']['password']
host = server_config['mysql_congig']['host']
port = server_config['mysql_congig']['port']
database_name = server_config['mysql_congig']['database']
connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}"
engine = create_engine(connection_string, echo=True)

print("engine---",engine)


general_responce_success = {"Status":200,"message":"","data":[]}
general_responce_fail = {"Status":500,"message":"Internal Server Erorr"}
def error_line_no():
    exception_type, exception_object, exception_traceback = sys.exc_info()
    line_no=exception_traceback.tb_lineno
    print("line_no",line_no) 



