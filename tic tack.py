from tkinter import*

from tkinter import ttk
from tkinter import messagebox
from random import randint

ro=Tk()
ro.title("tic tac toy : player 1")

style=ttk.Style()
style.theme_use('classic')


actilayer=1 # set active layr
p1=[]# what p1 select

p2=[] # what p2 select






bt1 =ttk.Button(ro,text=' ')
bt1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bt1.config(command=lambda:btclick(1))

bt2=ttk.Button(ro,text=' ')
bt2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bt2.config(command=lambda:btclick(2))

bt3=ttk.Button(ro,text=' ')
bt3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bt3.config(command=lambda:btclick(3))

bt4=ttk.Button(ro,text=' ')
bt4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bt4.config(command=lambda:btclick(4))


bt5=ttk.Button(ro,text=' ')
bt5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bt5.config(command=lambda:btclick(5))


bt6=ttk.Button(ro,text=' ')
bt6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bt6.config(command=lambda:btclick(6))

bt7=ttk.Button(ro,text=' ')
bt7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bt7.config(command=lambda:btclick(7))


bt8=ttk.Button(ro,text=' ')
bt8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bt8.config(command=lambda:btclick(8))

bt9=ttk.Button(ro,text=' ')
bt9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bt9.config(command=lambda:btclick(9))






def autplay():
    global p1
    global p2
    empcell=[]
    for cell in range(9):
        if(not(cell+1 in p1) or(cell+1 in p2)):
           empcell.append(cell+1)
    randindex=randint(0,len(empcell)-1)
    btclick(empcell[randindex])






def btclick(id):
    global actilayer
    global p1
    global p2
    if( actilayer==1):
        setlayer(id,'x')
        p1.append(id)
        ro.title('tic tack :player 2')
        actilayer=2
        autplay()
        print('p1:{}'.format(p1))
    elif( actilayer==2):
        setlayer(id,'0')
        p2.append(id)
        ro.title('tic tack :player 1')
        actilayer=1
        print('p2:{}'.format(p2))
    checwin()



def checwin():
    win=-1
    if((1 in p1)and(2 in p1)and(3 in p1)):
        win=1
    
    if((1 in p2)and(2 in p2)and(3 in p2)):
        win=2
    
    if((4 in p1)and(5 in p1)and(6 in p1)):
        win=1
    
    if((4 in p2)and(5 in p2)and(6 in p2)):
        win=2
        
    if((7 in p1)and(8 in p1)and(9 in p1)):
         
        win=1
        
    if((7 in p2)and(8 in p2)and(9 in p2)):
        win=2
    
        
    if((1 in p1)and(4 in p1)and(7 in p1)):
        win=1
    if((1 in p2)and(4 in p2)and(7 in p2)):
        win=2

    if((2 in p1)and(5 in p1)and(8 in p1)):
        win=1
    if((2 in p2)and(5 in p2)and(8 in p2)):
        win=2
    if(( 3 in p1)and( 6 in p1)and(9 in p1)):
        win=1
    if((3 in p2)and(6 in p2)and(9 in p2)):
        win=2
    if win ==1:
        messagebox.showinfo(title='yes',message='player  1 is win')
        
    if win==2:
        messagebox.showinfo(title='yes',message='player  2 is win')
    if(( win==1) and (win==2)):
        messagebox.showinfo(title='yes',message='players متعادلين')
    
    
    
    
    

def setlayer(id,text):
    if( id==1):
        bt1.config(text=text)
        bt1.state(['disabled'])
    elif(id==2):
        bt2.config(text=text)
        bt2.state(['disabled'])
    elif(id==3):
        bt3.config(text=text)
        bt3.state(['disabled'])
    elif(id==4):
         bt4.config(text=text)
         bt4.state(['disabled'])
    elif(id==5):
        bt5.config(text=text)
        bt5.state(['disabled'])
    elif(id==6):
        bt6.config(text=text)
        bt6.state(['disabled'])
    elif(id==7):
        bt7.config(text=text)
        bt7.state(['disabled'])
    elif(id==8):
        bt8.config(text=text)
        bt8.state(['disabled'])
    elif(id==9):
        bt9.config(text=text)
        bt9.state(['disabled'])
        
       
        










ro.mainloop()
