import mysql.connector as msc
from input_module import take_input
from assitent_details import name
from insert import insert_queans
from output_module import output
# from process_module import process
mydb=msc.connect(
    host="localhost",
    password="",
    port="3306",
    user="root",
    database="test"
)
def mysql(que):
    cursor=mydb.cursor()
    sql="SELECT * FROM quesandans;"
    # print(sql)
    cursor.execute(sql)
    res=cursor.fetchall()
    for i in res:
        if que==i[1]:
            return i[2]
    output("i didn't get you,can you please tell what its mean?")
    c=0
    for i in range(2):
        ans=take_input()
        if ans=='bye':
            return ans
        if "its mean" in ans:
            ans=ans.replace("its mean ","")
            for i in res:
                if ans==i[1]:
                    insert_queans(que,i[2])
                    return i[2]
        else:
            for i in res:
                if ans==i[1]:
                    return i[2]
        if c<=0:
            output("i didn't get you,can you please tell what its mean?")
        else:
            output("it's not in my find should i search on internet?")  
        c+=1
    return ""

           
