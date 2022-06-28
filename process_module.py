from pickle import TRUE
from mysql_connecter import mysql
from assitent_details import name
from mysql_connecter import mysql
from time_details import get_time
from internet import connect,check_on_wikipedia
from insert import insert_queans
from input_module import take_input
from output_module import output
import web
def process(query):
    query=query.lower()
    rtr=mysql(query)
    if "time" in rtr:
        return get_time()
    elif "internet" in rtr:
        if connect():
            return "Internet is connected."
        else:
            return "Internet is not connected."
    elif rtr=="":
        q=take_input()
        if q=="yes":
            output("wait for few seconds while searching.")
            data=check_on_wikipedia(query)
            if data!="":
                insert_queans(query,data) #TO insert data in database ,searched on google.
                return data
            else:
                return "sorry i didn't find anything on internet."
        else:
            return "ok, you find it out and tell me also. "
        # return data
    elif rtr=='on':
        output("from now i will speak.")
        return rtr
    elif rtr=='off':
        output("from now i won't speak.")
        return rtr
    elif rtr=='facebook':
        web.open_facebook()
        return "opening facebook"
    elif rtr=='google':
        web.open_google()
        return "opening google"
    elif rtr=='close':
        web.close_browser()
        return "closing browser"
    return rtr
