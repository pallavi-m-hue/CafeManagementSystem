from tkinter import *
import time
import ttkthemes
import mysql.connector
from tkinter import ttk,messagebox
from db_connect import fetch_data,execute_query
import pymysql

def load_customer(rightFrame):
    for widget in rightFrame.winfo_children():
        widget.destroy()
    scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
    scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
    cafeTable=ttk.Treeview(rightFrame,columns=('Id','Name','Contact','Email','Address'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
    scrollBarX.config(command=cafeTable.xview)
    scrollBarY.config(command=cafeTable.yview)
    cafeTable.config(show='headings')

    scrollBarX.pack(side=BOTTOM,fill=X)
    scrollBarY.pack(side=RIGHT,fill=Y)

    cafeTable.pack(side=BOTTOM,fill=BOTH,expand=1)
    cafeTable.heading('Id',text='Id')
    cafeTable.heading('Name',text='Name')
    cafeTable.heading('Contact',text='Contact')
    cafeTable.heading('Email',text='Email')
    cafeTable.heading('Address',text='Address')

    cafeTable.column('Id',width=50,anchor=CENTER)
    cafeTable.column('Name',width=300,anchor=CENTER)
    cafeTable.column('Contact',width=300,anchor=CENTER)
    cafeTable.column('Email',width=400,anchor=CENTER)
    cafeTable.column('Address',width=100,anchor=CENTER)

    def update_customer():
        def update_data():
            query='update customer set name=%s,contact=%s,email=%s,address=%s where id=%s'
            execute_query(query,(nameEntry.get(),contactEntry.get(),emailEntry.get(),addressEntry.get(),idEntry.get()))
            messagebox.showinfo('Success',f'Id{idEntry.get()} is modifed successfully')
            update_window.destroy()
            show_customer()


        update_window=Toplevel()
        update_window.title('update customer')
        update_window.grab_set()
        update_window.resizable(False,False)
        idLable=Label(update_window,text='Id',font=('times in roman',20,'bold'))
        idLable.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        idEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
        idEntry.grid(row=0,column=1,pady=15,padx=10)


        nameLable=Label(update_window,text='name',font=('times in roman',20,'bold'))
        nameLable.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        nameEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
        nameEntry.grid(row=1,column=1,pady=15,padx=10)

        contactLable=Label(update_window,text='contact',font=('times in roman',20,'bold'))
        contactLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        contactEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
        contactEntry.grid(row=2,column=1,pady=15,padx=10)

        emailLable=Label(update_window,text='email',font=('times in roman',20,'bold'))
        emailLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        emailEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
        emailEntry.grid(row=4,column=1,pady=15,padx=10)


        addressLable=Label(update_window,text='address',font=('times in roman',20,'bold'))
        addressLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        addressEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
        addressEntry.grid(row=3,column=1,pady=15,padx=10)

        update_menu_button=ttk.Button(update_window,text='update',command=update_data)
        update_menu_button.grid(row=6,column=1,pady=15)

        indexing=cafeTable.focus()
        print(indexing)
        content=cafeTable.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        contactEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        addressEntry.insert(0,listdata[4])
       

    def show_customer():
        query='select * from customer'
        cafeTable.delete(*cafeTable.get_children())
        fetched_data=fetch_data(query)
        for data in fetched_data:
            cafeTable.insert('',END,values=data)

    def delete_customer():
        indexing=cafeTable.focus()
        print(indexing)
        content=cafeTable.item(indexing)
        content_id=content['values'][0]
        query='delete from customer where id=%s'
        execute_query(query,(content_id,))
        messagebox.showinfo('Deleted',f'id{content_id} id is deleted successfully')
        query='select * from customer'
        fetched_data=fetch_data(query)
        cafeTable.delete(*cafeTable.get_children())
        for data in fetched_data:
            cafeTable.insert('',END,values=data)

    def search_customer():
        def search_data():
            query='select * from customer where id=%s or name=%s or contact=%s or email=%s or address=%s '
            fetched_data=fetch_data(query,(idEntry.get(),nameEntry.get(),contactEntry.get(),emailEntry.get(),addressEntry.get()))
            cafeTable.delete(*cafeTable.get_children())
            for data in fetched_data:
                cafeTable.insert('',END,values=data)

        search_window=Toplevel()
        search_window.title('search')
        search_window.grab_set()
        search_window.resizable(False,False)
        idLable=Label(search_window,text='Id',font=('times in roman',20,'bold'))
        idLable.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        idEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        idEntry.grid(row=0,column=1,pady=15,padx=10)

    
        nameLable=Label(search_window,text='name',font=('times in roman',20,'bold'))
        nameLable.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        nameEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        nameEntry.grid(row=1,column=1,pady=15,padx=10)

        contactLable=Label(search_window,text='contact',font=('times in roman',20,'bold'))
        contactLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        contactEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        contactEntry.grid(row=2,column=1,pady=15,padx=10)

        emailLable=Label(search_window,text='email',font=('times in roman',20,'bold'))
        emailLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        emailEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        emailEntry.grid(row=4,column=1,pady=15,padx=10)


        addressLable=Label(search_window,text='address',font=('times in roman',20,'bold'))
        addressLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        addressEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        addressEntry.grid(row=3,column=1,pady=15,padx=10)

        search_menu_button=ttk.Button(search_window,text='search',command=search_data)
        search_menu_button.grid(row=6,column=1,pady=15)

    def insert_customer():
        def insert_data():
            if idEntry.get()=='' or nameEntry.get()=='' or contactEntry.get()=='' or  emailEntry.get()=='' or addressEntry.get()=='' :
                messagebox.showerror('Error','All feilds are required',parent=insert_window)
            else:
                try:
                    execute_query('insert into customer values (%s,%s,%s,%s,%s)',(idEntry.get(),nameEntry.get(),contactEntry.get(),emailEntry.get(),addressEntry.get()))
                    result=messagebox.askyesno('conform','Data added successfully. Do you whant to clean the form?',parent=insert_window)
                    if result:
                        idEntry.delete(0,END)
                        nameEntry.delete(0,END)
                        contactEntry.delete(0,END)
                        emailEntry.delete(0,END)
                        addressEntry.delete(0,END)
                        
                    else:
                        pass
                except mysql.connector.IntegrityError:
                    messagebox.showerror('Error', 'ID cannot be repeated', parent=insert_window)
                except Exception as e:
                    messagebox.showerror('Error', f'Unexpected error: {e}', parent=insert_window)

                query='select * from customer'
                fetched_data=fetch_data(query)
                cafeTable.delete(*cafeTable.get_children())
                for data in fetched_data:
                    cafeTable.insert('',END,values=data)


        insert_window=Toplevel()
        insert_window.grab_set()
        insert_window.resizable(False,False)
        idLable=Label(insert_window,text='Id',font=('times in roman',20,'bold'))
        idLable.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        idEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        idEntry.grid(row=0,column=1,pady=15,padx=10)


        nameLable=Label(insert_window,text='name',font=('times in roman',20,'bold'))
        nameLable.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        nameEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        nameEntry.grid(row=1,column=1,pady=15,padx=10)

        contactLable=Label(insert_window,text='contact',font=('times in roman',20,'bold'))
        contactLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        contactEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        contactEntry.grid(row=2,column=1,pady=15,padx=10)

        emailLable=Label(insert_window,text='email',font=('times in roman',20,'bold'))
        emailLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        emailEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        emailEntry.grid(row=4,column=1,pady=15,padx=10)


        addressLable=Label(insert_window,text='address',font=('times in roman',20,'bold'))
        addressLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        addressEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        addressEntry.grid(row=3,column=1,pady=15,padx=10)

        insert_menu_button=ttk.Button(insert_window,text='insert',command=insert_data)
        insert_menu_button.grid(row=6,column=1,pady=15)


    show_customer()
    insertButton=ttk.Button(rightFrame,text='Insert',width=15,command=insert_customer)
    insertButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    searchButton=ttk.Button(rightFrame,text='Search',width=15,command=search_customer)
    searchButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    updateButton=ttk.Button(rightFrame,text='Update',width=15,command=update_customer)
    updateButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    deleteButton=ttk.Button(rightFrame,text='Delete',width=15,command=delete_customer)
    deleteButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    showButton=ttk.Button(rightFrame,text='Show',width=15,command=show_customer)
    showButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)