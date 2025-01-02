from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from db_connect import fetch_data,execute_query

def load_order(rightFrame):
    for widget in rightFrame.winfo_children():
        widget.destroy()
    scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
    scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
    orderTable=ttk.Treeview(rightFrame,columns=('OrderID','CustomerName','MenuItem'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
    scrollBarX.config(command=orderTable.xview)
    scrollBarY.config(command=orderTable.yview)
    orderTable.config(show='headings')

    scrollBarX.pack(side=BOTTOM,fill=X)
    scrollBarY.pack(side=RIGHT,fill=Y)

    orderTable.pack(side=BOTTOM,fill=BOTH,expand=1)
    orderTable.heading('OrderID',text='OrderID')
    orderTable.heading('CustomerName',text='CustomerName')
    orderTable.heading('MenuItem',text='MenuItem')

    orderTable.column('OrderID',width=50,anchor=CENTER)
    orderTable.column('CustomerName',width=300,anchor=CENTER)
    orderTable.column('MenuItem',width=300,anchor=CENTER)
    
    def show_order():
        query='select orders.orderid,customer.name,menu.name FROM orders JOIN customer ON orders.customerid=customer.id JOIN menu ON orders.menuid=menu.id'
        orderTable.delete(*orderTable.get_children())
        fetched_data=fetch_data(query)
        for data in fetched_data:
            orderTable.insert('',END,values=data)

    def delete_order():
        indexing=orderTable.focus()
        print(indexing)
        content=orderTable.item(indexing)
        content_id=content['values'][0]
        query='delete from orders where orderid=%s'
        execute_query(query,(content_id,))
        messagebox.showinfo('Deleted',f'id{content_id} id is deleted successfully')
        show_order()


    def insert_order():
        def insert_data():
            if idEntry.get()=='' or customerEntry.get()=='' or menuEntry.get()=='':
                messagebox.showerror('Error','All feilds are required',parent=insert_window)
            else:
                try:
                    execute_query('insert into orders values (%s,%s,%s)',(idEntry.get(),customerEntry.get(),menuEntry.get()))
                    result=messagebox.askyesno('conform','Data added successfully. Do you whant to clean the form?',parent=insert_window)
                    if result:
                        idEntry.delete(0,END)
                        customerEntry.delete(0,END)
                        menuEntry.delete(0,END)
                    else:
                        pass
                except mysql.connector.IntegrityError:
                    messagebox.showerror('Error', 'ID cannot be repeated', parent=insert_window)
                except Exception as e:
                    messagebox.showerror('Error', f'Unexpected error: {e}', parent=insert_window)

                show_order()


        insert_window=Toplevel()
        insert_window.title('insert order id')
        insert_window.grab_set()
        insert_window.resizable(False,False)
        idLable=Label(insert_window,text='Id',font=('times in roman',20,'bold'))
        idLable.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        idEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        idEntry.grid(row=0,column=1,pady=15,padx=10)

    
        customerLable=Label(insert_window,text='Customer Name',font=('times in roman',20,'bold'))
        customerLable.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        customerEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        customerEntry.grid(row=1,column=1,pady=15,padx=10)
        
        customerName_values=[f"{row[0]}-{row[1]}" for row in fetch_data('select id,name FROM customer')]
        customer_dropdown=ttk.Combobox(insert_window, values=customerName_values)
        customer_dropdown.set("Select Customer")
        customer_dropdown.grid(row=2,column=1)
        customer_dropdown.bind("<<ComboboxSelected>>",lambda e: on_select_customerName(customer_dropdown,customerEntry))
        def on_select_customerName(customer_dropdown,customerEntry):
            selected_name=customer_dropdown.get()
            customer_id, customer_name = selected_name.split('-', 1)  # Splitting the ID and Name
            customerEntry.delete(0, tk.END)
            customerEntry.insert(0, customer_id)

        menuLable=Label(insert_window,text='menu item',font=('times in roman',20,'bold'))
        menuLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        menuEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        menuEntry.grid(row=3,column=1,pady=15,padx=10)

        menuName_values=[f"{row[0]}-{row[1]}" for row in fetch_data('select id,name FROM menu')]
        menu_dropdown=ttk.Combobox(insert_window, values=menuName_values)
        menu_dropdown.set("Select Menu")
        menu_dropdown.grid(row=4,column=1)
        menu_dropdown.bind("<<ComboboxSelected>>",lambda e: on_select_menuName(menu_dropdown,menuEntry))
        def on_select_menuName(menu_dropdown,menuEntry):
            selected_name=menu_dropdown.get()
            menu_id, menu_name = selected_name.split('-', 1)  # Splitting the ID and Name
            menuEntry.delete(0, tk.END)
            menuEntry.insert(0, menu_id)

    

        insert_menu_button=ttk.Button(insert_window,text='insert',command=insert_data)
        insert_menu_button.grid(row=6,column=1,pady=15)


    show_order()
    insertButton=ttk.Button(rightFrame,text='Insert',width=25,command=insert_order)
    insertButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    deleteButton=ttk.Button(rightFrame,text='Delete',width=25,command=delete_order)
    deleteButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)
