from time_details import get_hour
from output_module import output
from speak import speech
time=int(get_hour())

def greet():
    if time>=4 and time <=12:
        speech("Good morning user")
        output("Good morning user")

    elif time>=12 and time<=16:
        speech("Good afternoon user")
        output("Good afternoon user")
    else:
        speech("Good evening user")
        output("Good evening user")

# greet()