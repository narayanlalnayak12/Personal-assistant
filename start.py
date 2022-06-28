from input_module import take_input
from process_module import process
from output_module import output
from welcome import greet

x=True
greet()    #for greeting messaging                                                                                                      
while(x):
    i=take_input()
    if i=='bye':
        x=False
        output("ok bye")
        break
    p=process(i)
    if p=='bye':
        output("ok bye")
        break
    elif p=='ok bye':
        output("ok bye ,have a nice day")
    output(p)
