from Crud_Api import mysql,general_responce_success,general_responce_fail,jsonify,request,error_line_no
from Crud_Api.Models import *



def Crud_Fun():
    if request.method == "GET":
        try:
            sql_query = """SELECT * FROM crud_table"""
            dbc = Connection_db(1,sql_query)
            data = dbc.sql_query_execute()
            general_responce_success["data"] = data
            return jsonify(general_responce_success)

            
        except Exception as es:
            error_line_no()
            print("error-==",es)
            return jsonify(general_responce_fail)
    
    if request.method == "POST":
        try:
            data = request.json
            sql_query = """INSERT INTO crud_table(First_Name,Last_Name,Email) 
                        VALUES('{}','{}','{}')""".format(data["First_Name"],data["Last_Name"],
                                                                data["Email"])
            dbc = Connection_db(0,sql_query)
            flag = dbc.sql_query_execute()
            
            if flag == 1:
                general_responce_success['message'] = "User Insert Successfully"
                return jsonify(general_responce_success)
            else:
                general_responce_success['message'] = "Problem With Insert"
                return jsonify(general_responce_success)
                
        except Exception as es:
            error_line_no()
            print("error-==",es)
            return jsonify(general_responce_fail)
    
    if request.method == "PUT":
        try:
            data = request.json
            sql_query = """UPDATE crud_table SET First_Name = '{}', Last_Name = '{}' , Email 
            = '{}' WHERE User_Id = {} """.format(data["First_Name"],data["Last_Name"],
                                                                data["Email"],data["User_Id"])
            dbc = Connection_db(0,sql_query)
            flag = dbc.sql_query_execute()
            
            if flag == 1:
                general_responce_success['message'] = "User Insert Successfully"
                return jsonify(general_responce_success)
            else:
                general_responce_success['message'] = "Problem With Insert"
                return jsonify(general_responce_success)
                
        except Exception as es:
            error_line_no()
            print("error-==",es)
            return jsonify(general_responce_fail)
    if request.method == "DELETE":
        try:
            data = request.json
            sql_query = """DELETE FROM crud_table  WHERE User_Id = {} """.format(data["User_Id"])
            dbc = Connection_db(0,sql_query)
            flag = dbc.sql_query_execute()
            
            if flag == 1:
                general_responce_success['message'] = "User Insert Successfully"
                return jsonify(general_responce_success)
            else:
                general_responce_success['message'] = "Problem With Insert"
                return jsonify(general_responce_success)
                
        except Exception as es:
            error_line_no()
            print("error-==",es)
            return jsonify(general_responce_fail)
        
            