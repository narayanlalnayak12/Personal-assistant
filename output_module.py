from assitent_details import name
from speak import speech
y=0
def output(p):
    #command line output
    global y    #To make change in golabal variable in any function we need to write the global keyword in funtion with variable.
    if p=='on':
        y=1
    if p=='off':
        y=0
    if y==0:
        # print(name+": "+p)    while using gui comment it
        pass
    else:
        # print(name+": "+p)   while using gui comment it
        speech(p)
    return p       #while using gui uncomment it
   