from tkinter import *
import desktop_database_app.backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        pass

def view_command():
    list1.delete(0,END)
    for row in desktop_database_app.backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in desktop_database_app.backend.search(title_text.get(),author_name.get(),year_value.get(),ISBN_value.get()):
        list1.insert(END,row)

def add_command():
    desktop_database_app.backend.insert(title_text.get(),author_name.get(),year_value.get(),ISBN_value.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_name.get(),year_value.get(),ISBN_value.get()))

def delete_command():
    desktop_database_app.backend.delete(selected_tuple[0])

def update_command():
    desktop_database_app.backend.update(selected_tuple[0],title_text.get(),author_name.get(),year_value.get(),ISBN_value.get())
    print(selected_tuple[0],title_text.get(),author_name.get(),year_value.get(),ISBN_value.get())

window = Tk()
window.wm_title("Book Store")
l1 = Label(window, text = 'Title')
l1.grid(row=0, column=0)

l2 = Label(window, text = "Author")
l2.grid(row=0, column=2)

l3 = Label(window, text = "Year")
l3.grid(row=1, column=0 )

l4 = Label(window, text = 'ISBN')
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row=0, column=1)

author_name = StringVar()
e2 = Entry(window, textvariable = author_name)
e2.grid(row=0, column=3)

year_value = StringVar()
e3 = Entry(window, textvariable = year_value)
e3.grid(row=1, column=1)

ISBN_value = StringVar()
e4 = Entry(window, textvariable = ISBN_value)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text = "Add entry", width = 12, command = add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text = "Update", width = 12, command = update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text = "Delete", width = 12,command = delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text = "Close", width = 12, command= window.destroy)
b6.grid(row=7, column=3)
window.mainloop()
