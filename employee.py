from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
from db_connect import fetch_data,execute_query


def load_employee(rightFrame):
    for widget in rightFrame.winfo_children():
        widget.destroy()
    scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
    scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
    cafeTable=ttk.Treeview(rightFrame,columns=('Id','Name','Gender','Position','Salary','Contact'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
    scrollBarX.config(command=cafeTable.xview)
    scrollBarY.config(command=cafeTable.yview)
    cafeTable.config(show='headings')

    scrollBarX.pack(side=BOTTOM,fill=X)
    scrollBarY.pack(side=RIGHT,fill=Y)

    cafeTable.pack(side=BOTTOM,fill=BOTH,expand=1)
    cafeTable.heading('Id',text='Id')
    cafeTable.heading('Name',text='Name')
    cafeTable.heading('Gender',text='Gender')
    cafeTable.heading('Position',text='Position')
    cafeTable.heading('Salary',text='Salary')
    cafeTable.heading('Contact',text='Contact')

    cafeTable.column('Id',width=50,anchor=CENTER)
    cafeTable.column('Name',width=300,anchor=CENTER)
    cafeTable.column('Gender',width=300,anchor=CENTER)
    cafeTable.column('Position',width=400,anchor=CENTER)
    cafeTable.column('Salary',width=400,anchor=CENTER)
    cafeTable.column('Contact',width=100,anchor=CENTER)

    def update_employee():
        def update_data():
            query='update employee set name=%s,gender=%s,position=%s,salary=%s,contact=%s where id=%s'
            execute_query(query,(nameEntry.get(),genderEntry.get(),positionEntry.get(),salaryEntry.get(),contactEntry.get(),idEntry.get()))
            messagebox.showinfo('Success',f'Id{idEntry.get()} is modifed successfully')
            search_window.destroy()
            show_employee()


        search_window=Toplevel()
        search_window.title('update employee')
        search_window.grab_set()
        search_window.resizable(False,False)
        idLable=Label(search_window,text='Id',font=('times in roman',20,'bold'))
        idLable.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        idEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        idEntry.grid(row=0,column=1,pady=15,padx=10)

    
        nameLable=Label(search_window,text='Name',font=('times in roman',20,'bold'))
        nameLable.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        nameEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        nameEntry.grid(row=1,column=1,pady=15,padx=10)

        genderLable=Label(search_window,text='Gender',font=('times in roman',20,'bold'))
        genderLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        genderEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        genderEntry.grid(row=2,column=1,pady=15,padx=10)

        positionLable=Label(search_window,text='Position',font=('times in roman',20,'bold'))
        positionLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        positionEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        positionEntry.grid(row=4,column=1,pady=15,padx=10)


        salaryLable=Label(search_window,text='Salary',font=('times in roman',20,'bold'))
        salaryLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        salaryEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        salaryEntry.grid(row=3,column=1,pady=15,padx=10)


        contactLable=Label(search_window,text='Contact',font=('times in roman',20,'bold'))
        contactLable.grid(row=5,column=0,padx=30,pady=15,sticky=W)
        contactEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        contactEntry.grid(row=5,column=1,pady=15,padx=10)

        update_menu_button=ttk.Button(search_window,text='update',command=update_data)
        update_menu_button.grid(row=6,column=1,pady=15)

        indexing=cafeTable.focus()
        print(indexing)
        content=cafeTable.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        genderEntry.insert(0,listdata[2])
        positionEntry.insert(0,listdata[3])
        salaryEntry.insert(0,listdata[4])
        contactEntry.insert(0,listdata[5])

    def show_employee():
        query='select * from employee'
        cafeTable.delete(*cafeTable.get_children())
        fetched_data=fetch_data(query)
        for data in fetched_data:
            cafeTable.insert('',END,values=data)

    def delete_employee():
        indexing=cafeTable.focus()
        print(indexing)
        content=cafeTable.item(indexing)
        content_id=content['values'][0]
        query='delete from employee where id=%s'
        execute_query(query,(content_id,))
        messagebox.showinfo('Deleted',f'id{content_id} id is deleted successfully')
        query='select * from employee'
        fetched_data=fetch_data(query)
        cafeTable.delete(*cafeTable.get_children())
        for data in fetched_data:
            cafeTable.insert('',END,values=data)

    def search_employee():
        def search_data():
            query='select * from employee where id=%s or name=%s or gender=%s or position=%s or salary=%s or contact=%s'
            fetched_data=fetch_data(query,(idEntry.get(),nameEntry.get(),genderEntry.get(),positionEntry.get(),salaryEntry.get(),contactEntry.get()))
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

    
        nameLable=Label(search_window,text='Name',font=('times in roman',20,'bold'))
        nameLable.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        nameEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        nameEntry.grid(row=1,column=1,pady=15,padx=10)

        genderLable=Label(search_window,text='Gender',font=('times in roman',20,'bold'))
        genderLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        genderEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        genderEntry.grid(row=2,column=1,pady=15,padx=10)

        positionLable=Label(search_window,text='Position',font=('times in roman',20,'bold'))
        positionLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        positionEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        positionEntry.grid(row=4,column=1,pady=15,padx=10)


        salaryLable=Label(search_window,text='Salary',font=('times in roman',20,'bold'))
        salaryLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        salaryEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        salaryEntry.grid(row=3,column=1,pady=15,padx=10)


        contactLable=Label(search_window,text='Contact',font=('times in roman',20,'bold'))
        contactLable.grid(row=5,column=0,padx=30,pady=15,sticky=W)
        contactEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
        contactEntry.grid(row=5,column=1,pady=15,padx=10)

        search_menu_button=ttk.Button(search_window,text='search',command=search_data)
        search_menu_button.grid(row=6,column=1,pady=15)

    def insert_employee():
        def insert_data():
            if idEntry.get()=='' or nameEntry.get()=='' or genderEntry.get()=='' or  positionEntry.get()=='' or salaryEntry.get()=='' or contactEntry.get()=='':
                messagebox.showerror('Error','All feilds are required',parent=insert_window)
            else:
                try:
                    execute_query('insert into employee values (%s,%s,%s,%s,%s,%s)',(idEntry.get(),nameEntry.get(),genderEntry.get(),positionEntry.get(),salaryEntry.get(),contactEntry.get()))
                    result=messagebox.askyesno('conform','Data added successfully. Do you whant to clean the form?',parent=insert_window)
                    if result:
                        idEntry.delete(0,END)
                        nameEntry.delete(0,END)
                        genderEntry.delete(0,END)
                        positionEntry.delete(0,END)
                        salaryEntry.delete(0,END)
                        contactEntry.delete(0,END)
                    else:
                        pass
                except mysql.connector.IntegrityError:
                    messagebox.showerror('Error', 'ID cannot be repeated', parent=insert_window)
                except Exception as e:
                    messagebox.showerror('Error', f'Unexpected error: {e}', parent=insert_window)

                query='select * from employee'
                fetched_data=fetch_data(query)
                cafeTable.delete(*cafeTable.get_children())
                for data in fetched_data:
                    cafeTable.insert('',END,values=data)


        insert_window=Toplevel()
        insert_window.title('insert employee')
        insert_window.grab_set()
        insert_window.resizable(False,False)
        idLable=Label(insert_window,text='Id',font=('times in roman',20,'bold'))
        idLable.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        idEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        idEntry.grid(row=0,column=1,pady=15,padx=10)

    
        nameLable=Label(insert_window,text='Name',font=('times in roman',20,'bold'))
        nameLable.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        nameEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        nameEntry.grid(row=1,column=1,pady=15,padx=10)

        genderLable=Label(insert_window,text='Gender',font=('times in roman',20,'bold'))
        genderLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        genderEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        genderEntry.grid(row=2,column=1,pady=15,padx=10)

        positionLable=Label(insert_window,text='Position',font=('times in roman',20,'bold'))
        positionLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        positionEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        positionEntry.grid(row=4,column=1,pady=15,padx=10)


        salaryLable=Label(insert_window,text='Salary',font=('times in roman',20,'bold'))
        salaryLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        salaryEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        salaryEntry.grid(row=3,column=1,pady=15,padx=10)


        contactLable=Label(insert_window,text='Contact',font=('times in roman',20,'bold'))
        contactLable.grid(row=5,column=0,padx=30,pady=15,sticky=W)
        contactEntry=Entry(insert_window,font=('roman',15,'bold'),width=24)
        contactEntry.grid(row=5,column=1,pady=15,padx=10)

        insert_menu_button=ttk.Button(insert_window,text='insert',command=insert_data)
        insert_menu_button.grid(row=6,column=1,pady=15)


    show_employee()
    insertButton=ttk.Button(rightFrame,text='Insert',width=15,command=insert_employee)
    insertButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    searchButton=ttk.Button(rightFrame,text='Search',width=15,command=search_employee)
    searchButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    updateButton=ttk.Button(rightFrame,text='Update',width=15,command=update_employee)
    updateButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    deleteButton=ttk.Button(rightFrame,text='Delete',width=15,command=delete_employee)
    deleteButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)

    showButton=ttk.Button(rightFrame,text='Show',width=15,command=show_employee)
    showButton.pack(side=BOTTOM and LEFT,fill=BOTH,expand=1)