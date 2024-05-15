from Crud_Api import app
from Crud_Api.Crud import *

app.add_url_rule('/Crud','Crud_Fun',Crud_Fun,methods=['GET','POST','PUT','DELETE'])


