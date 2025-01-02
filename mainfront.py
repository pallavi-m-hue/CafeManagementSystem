from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql 
from db_connect import fetch_data,execute_query
from menu import load_menu
from employee import load_employee
from customer import load_customer
from order import load_order

count=0
text=''

def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLable.config(text=text)
    count+=1
    sliderLable.after(300,slider)

def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date:{date}\n Time: {currenttime}')
    datetimeLabel.after(1000,clock)

root= ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)

root.title('Cafe Manegement System')

datetimeLabel=Label(root,text='hello',font=('times in romen',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Cafe Manegement System'
sliderLable=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLable.place(x=230,y=0)
slider()


leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='menu.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

menuButton=ttk.Button(leftFrame,text='MENU',width=25,command= lambda: load_menu(rightFrame))
menuButton.grid(row=1,column=0,pady=30)

CustomerButton=ttk.Button(leftFrame,text='CUSTOMER',width=25,command= lambda:load_customer(rightFrame))
CustomerButton.grid(row=2,column=0,pady=30)

EmployeeButton=ttk.Button(leftFrame,text='EMPLOYEE',width=25,command= lambda:load_employee(rightFrame))
EmployeeButton.grid(row=3,column=0,pady=30)

OrdersButton=ttk.Button(leftFrame,text='ORDERS',width=25,command= lambda:load_order(rightFrame))
OrdersButton.grid(row=4,column=0,pady=30)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)


scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

style=ttk.Style()

style.configure('Treeview',rowheight=40,front=('arial',12,'bold'),foreground='black')
style.configure('Treeview',font=('arial',14,'bold'))

root.mainloop()