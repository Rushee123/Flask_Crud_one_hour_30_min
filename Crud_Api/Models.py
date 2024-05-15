from Crud_Api import mysql

class Connection_db():
    def __init__(self,query_type,query):
        self.query_type = query_type
        self.query = query
        self.conn = mysql.connection
    
    def sql_query_execute(self):    
        conn = self.conn
        cur = conn.cursor()
        if self.query_type == 1:
            cur.execute(self.query)
            data = cur.fetchall()
            conn.commit()
            cur.close()
            return data
        else:
            print("in Update part")
            cur.execute(self.query)
            conn.commit()
            cur.close()
            return 1
            
            
            
            
        
        
        
        
    
    
        
    