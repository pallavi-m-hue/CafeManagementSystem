from tkinter import *
import time
import ttkthemes
import mysql.connector
from tkinter import ttk,messagebox
from db_connect import fetch_data,execute_query
import pymysql

def load_menu(rightFrame):
    for widget in rightFrame.winfo_children():
        widget.destroy()
    scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
    scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
    cafeTable=ttk.Treeview(rightFrame,columns=('Id','Name','Type','Description','Price','Availability'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
    scrollBarX.config(command=cafeTable.xview)
    scrollBarY.config(command=cafeTable.yview)
    cafeTable.config(show='headings')

    scrollBarX.pack(side=BOTTOM,fill=X)
    scrollBarY.pack(side=RIGHT,fill=Y)

    cafeTable.pack(side=BOTTOM,fill=BOTH,expand=1)
    cafeTable.heading('Id',text='Id')
    cafeTable.heading('Name',text='Name')
    cafeTable.heading('Type',text='Type')
    cafeTable.heading('Description',text='Description')
    cafeTable.heading('Price',text='Price')
    cafeTable.heading('Availability',text='Availability')

    cafeTable.column('Id',width=50,anchor=CENTER)
    cafeTable.column('Name',width=300,anchor=CENTER)
    cafeTable.column('Type',width=300,anchor=CENTER)
    cafeTable.column('Description',width=400,anchor=CENTER)
    cafeTable.column('Price',width=400,anchor=CENTER)
    cafeTable.column('Availability',width=100,anchor=CENTER)

    def update_menu():
        def update_data():
            query='update menu set name=%s,type=%s,description=%s,price=%s,availability=%s where id=%s'
            execute_query(query,(nameEntry.get(),typeEntry.get(),descriptionEntry.get(),priceEntry.get(),availabilityEntry.get(),idEntry.get()))
            messagebox.showinfo('Success',f'Id{idEntry.get()} is modifed successfully')
            update_window.destroy()
            show_menu()


        update_window=Toplevel()
        update_window.title('update menu')
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

        typeLable=Label(update_window,text='type',font=('times in roman',20,'bold'))
        typeLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        typeEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
        typeEntry.grid(row=2,column=1,pady=15,padx=10)

        descriptionLable=Label(update_window,text='description',font=('times in roman',20,'bold'))
        descriptionLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        descriptionEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
        descriptionEntry.grid(row=4,column=1,pady=15,padx=10)


        priceLable=Label(update_window,text='price',font=('times in roman',20,'bold'))
        priceLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        priceEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
        priceEntry.grid(row=3,column=1,pady=15,padx=10)


        availabilityLable=Label(update_window,text='availability',font=('times in roman',20,'bold'))
        availabilityLable.grid(row=5,column=0,padx=30,pady=15,sticky=W)
        availabilityEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
        availabilityEntry.grid(row=5,column=1,pady=15,padx=10)

        update_menu_button=ttk.Button(update_window,text='update',command=update_data)
        update_menu_button.grid(row=6,column=1,pady=15)

        indexing=cafeTable.focus()
        print(indexing)
        content=cafeTable.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        typeEntry.insert(0,listdata[2])
        descriptionEntry.insert(0,listdata[3])
        priceEntry.insert(0,listdata[4])
        availabilityEntry.insert(0,listdata[5])

    def show_menu():
        query='select * from menu'
        cafeTable.delete(*cafeTable.get_children())
        fetched_data=fetch_data(query)
        for data in fetched_data:
            cafeTable.insert('',END,values=data)

    def delete_menu():
        indexing=cafeTable.focus()
        print(indexing)
        content=cafeTable.item(indexing)
        content_id=content['values'][0]
        query='delete from menu where id=%s'
        execute_query(query,(content_id,))
        messagebox.showinfo('Deleted',f'id{content_id} id is deleted successfully')
        query='select * from menu'
        fetched_data=fetch_data(query)
        cafeTable.delete(*cafeTable.get_children())
        for data in fetched_data:
            cafeTable.insert('',END,values=data)

    def search_menu():
        def search_data():
            query='select * from menu where id=%s or name=%s or type=%s or description=%s or price=%s or availability=%s'
            fetched_data=fetch_data(query,(idEntry.get(),nameEntry.get(),typeEntry.get(),descriptionEntry.get(),priceEntry.get(),availabilityEntry.get()))
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

        typeLable=Label(search_window,text='type',font=('times in roman',20,'bold'))
        typeLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        typeEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        typeEntry.grid(row=2,column=1,pady=15,padx=10)

        descriptionLable=Label(search_window,text='description',font=('times in roman',20,'bold'))
        descriptionLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        descriptionEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        descriptionEntry.grid(row=4,column=1,pady=15,padx=10)


        priceLable=Label(search_window,text='price',font=('times in roman',20,'bold'))
        priceLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        priceEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        priceEntry.grid(row=3,column=1,pady=15,padx=10)


        availabilityLable=Label(search_window,text='availability',font=('times in roman',20,'bold'))
        availabilityLable.grid(row=5,column=0,padx=30,pady=15,sticky=W)
        availabilityEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        availabilityEntry.grid(row=5,column=1,pady=15,padx=10)

        search_menu_button=ttk.Button(search_window,text='search',command=search_data)
        search_menu_button.grid(row=6,column=1,pady=15)

    def insert_menu():
        def insert_data():
            if idEntry.get()=='' or nameEntry.get()=='' or typeEntry.get()=='' or  descriptionEntry.get()=='' or priceEntry.get()=='' or availabilityEntry.get()=='':
                messagebox.showerror('Error','All feilds are required',parent=insert_window)
            else:
                try:
                    execute_query('insert into menu values (%s,%s,%s,%s,%s,%s)',(idEntry.get(),nameEntry.get(),typeEntry.get(),descriptionEntry.get(),priceEntry.get(),availabilityEntry.get()))
                    result=messagebox.askyesno('conform','Data added successfully. Do you whant to clean the form?',parent=insert_window)
                    if result:
                        idEntry.delete(0,END)
                        nameEntry.delete(0,END)
                        typeEntry.delete(0,END)
                        descriptionEntry.delete(0,END)
                        priceEntry.delete(0,END)
                        availabilityEntry.delete(0,END)
                    else:
                        pass
                except mysql.connector.IntegrityError:
                    messagebox.showerror('Error', 'ID cannot be repeated', parent=insert_window)
                except Exception as e:
                    messagebox.showerror('Error', f'Unexpected error: {e}', parent=insert_window)

                query='select * from menu'
                fetched_data=fetch_data(query)
                cafeTable.delete(*cafeTable.get_children())
                for data in fetched_data:
                    cafeTable.insert('',END,values=data)


        insert_window=Toplevel()
        insert_window.title("Insert item from Menu")
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

        typeLable=Label(insert_window,text='type',font=('times in roman',20,'bold'))
        typeLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        typeEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        typeEntry.grid(row=2,column=1,pady=15,padx=10)

        descriptionLable=Label(insert_window,text='description',font=('times in roman',20,'bold'))
        descriptionLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        descriptionEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        descriptionEntry.grid(row=4,column=1,pady=15,padx=10)


        priceLable=Label(insert_window,text='price',font=('times in roman',20,'bold'))
        priceLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        priceEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        priceEntry.grid(row=3,column=1,pady=15,padx=10)


        availabilityLable=Label(insert_window,text='availability',font=('times in roman',20,'bold'))
        availabilityLable.grid(row=5,column=0,padx=30,pady=15,sticky=W)
        availabilityEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        availabilityEntry.grid(row=5,column=1,pady=15,padx=10)

        insert_menu_button=ttk.Button(insert_window,text='insert',command=insert_data)
        insert_menu_button.grid(row=6,column=1,pady=15)


    show_menu()
    insertButton=ttk.Button(rightFrame,text='Insert',width=15,command=insert_menu)
    insertButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    searchButton=ttk.Button(rightFrame,text='Search',width=15,command=search_menu)
    searchButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    updateButton=ttk.Button(rightFrame,text='Update',width=15,command=update_menu)
    updateButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    deleteButton=ttk.Button(rightFrame,text='Delete',width=15,command=delete_menu)
    deleteButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    showButton=ttk.Button(rightFrame,text='Show',width=15,command=show_menu)
    showButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)