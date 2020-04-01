from tkinter import *
import sqlite3

root = Tk()
root.title('Codemy.com - Learn to code')
root.geometry("400x400")

conn = sqlite3.connect('adressbook')
c = conn.cursor()
'''
c.execute("""CREATE TABLE adresses(
        first_name text,
        last_name text,
        adress text,
        city text,
        zipcode integer)""")
'''


def update():
    conn = sqlite3.connect('adressbook')
    c = conn.cursor()
    record_id = delete_box.get()


    c.execute("""UPDATE adresses SET 
        first_name = :first,
        last_name = :last,
        adress = :record_id = 1,
        city = :city,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
        'first': f_name_edit.get(),
        'last ': l_name_edit.get(),
        'address': address_edit.get(),
        #'city': city_edit.get(),
        #'zipcode': zipcode_edit.get(),
        
        #'oid': record_id
        })



    conn.commit()
    conn.close()



def edit():
    editor = Tk()
    editor.title('Update a Record')
    editor.geometry("400x600")

    conn = sqlite3.connect('adressbook')
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("SELECT * FROM adresses WHERE oid = " + record_id)
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record) +"\n"

    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global zipcode_edit
 

    f_name_edit = Entry(editor, width=30)
    f_name_edit.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_edit = Entry(editor, width=30)
    l_name_edit.grid(row=1, column=1, padx=20)

    address_edit = Entry(editor, width=30)
    address_edit.grid(row=2, column=1, padx=20)

    city_edit = Entry(editor, width=30)
    city_edit.grid(row=3, column=1, padx=20)

    zipcode_edit = Entry(editor, width=30)
    zipcode_edit.grid(row=4, column=1, padx=20)





    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Adress")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=4, column=0)

    for record in records:
        f_name_edit.insert(0, record[0])
        l_name_edit.insert(0, record[1])
        address_edit.insert(0, record[2])
        city_edit.insert(0, record[3])
        zipcode_edit.insert(0, record[4])

    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)



def delete():
    conn = sqlite3.connect('adressbook')
    c = conn.cursor()


    c.execute("DELETE from adresses WHERE oid = " + delete_box.get())
    delete_box.delete(0, END)


    conn.commit()
    conn.close()






def submit():
    conn = sqlite3.connect('adressbook')
    c = conn.cursor()

    c.execute("INSERT INTO adresses VALUES(:f_name, :l_name, :address, :city, :zipcode)",
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'zipcode':zipcode.get()
            })


    conn.commit()
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)

def query():
    conn = sqlite3.connect('adressbook')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM adresses")
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record) +"\n"

    query_lable = Label(root, text=print_records)
    query_lable.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=4, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)






f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Adress")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=4, column=0)

delete_box_lable = Label(root, text="ID Number")
delete_box_lable.grid(row=9, column=0, pady=5)


submit_btn = Button(root, text= "Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

update_btn = Button(root, text="Update Record", command=edit)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

conn.commit()
conn.close()





root.mainloop()