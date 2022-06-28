from tkinter import*

from input_module import take_input
from output_module import output
from process_module import process

root = Tk()
root.title('POOJA')

root.geometry("500x500")
root.minsize(200,100)
root.maxsize(900,800)

# main function for input and output
def ques():
    que = ent.get()
    # print(que)
    chatwin.insert(END,'You: '+que+'\n')
    i=take_input(que)
    ent.delete(0,END)
    p=process(i)
    ans=output(p)
    chatwin.insert(END,'Pooja: '+ans+'\n')
#create main menu bar

main_menu = Menu(root)

#file menu
file_menu=Menu(root)

file_menu.add_command(label='New')
file_menu.add_command(label='Save as')
file_menu.add_command(label='Exit')


main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Block')
main_menu.add_command(label='Quit')

root.config(menu=main_menu)

#create chatwindow

chatwin = Text(root,bd=5,bg='light green' , width=50 ,height = 8,font=(10))
chatwin.place(x=10,y=10, width=460 , height=400)

#create message win
ent = Entry(root,font=(10),bd=2,bg='white',width=31)
ent.place(x=10,y=410)
# ent.pack()
#create button to send message
btn=Button(root,text='send',bg='green' ,activebackground='light blue',width=130 ,height=2 ,font=(20),command=ques)
btn.place(x=360,y=410,width=110,height=30)

#Add scroll bar
scr = Scrollbar(root,command=chatwin.yview())
scr.place(x=470,y=10,height=400,width=20)
root.mainloop()