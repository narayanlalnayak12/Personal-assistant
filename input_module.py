import speech_to_text as st
import output_module
x=0
def take_input(i):
    global x
    #command line input
    if x==0:
        # i=input("Narayan: ")      while using gui comment it
        if i=='i want to speak':
            x=1
    else:
        try:
            i=st.spc_to_text()
            if i=="I don't want to speak":
                x=0
            elif i=="I do not want to speak":
                x=0
            elif i=="I want to text":
                x=0
            print("Narayan: "+i)
        except:
            output_module.output("i didn't recognized your voice")
            return "empty"
       
    i=i.lower()
    return i
