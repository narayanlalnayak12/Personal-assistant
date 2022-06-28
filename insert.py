
import mysql.connector as msc
from assitent_details import name
mydb=msc.connect(
    host="localhost",
    password="",
    port="3306",
    user="root",
    database="test"
)

def insert_queans(ques,ansr):
    cur=mydb.cursor()
    sql1="INSERT INTO quesandans (question,answer) VALUES ('"+ques+"','"+ansr+"');"
    cur.execute(sql1)
    mydb.commit()
    print(name+": Thanks i will remmeber it for the next time!")


# insert_queans('close browser','close')