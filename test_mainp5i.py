from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import scrolledtext
from tkinter import messagebox

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()
    
    def init_main(self):
        toolbar_2 = tk.Frame(bg="#0000CD", bd=5)
        toolbar_2.pack(side=tk.TOP, fill=tk.X)
        toolbar = tk.Frame(bg="#0000CD", bd=5)
        toolbar.pack(side=tk.TOP, fill=tk.X) 

        
#дополнительное меню
        tab_control = ttk.Notebook(toolbar_2)  
        tab1 = ttk.Frame(tab_control)  
        tab2 = ttk.Frame(tab_control)  
        tab_control.add(tab1, text='Вход')  
        tab_control.add(tab2, text='Регистрация') 
        tab_control.pack(expand=0, fill='both')

        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='update.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='delete.gif')
        btn_delete = tk.Button(toolbar, text='Удалить позицию', bg='#d7d8e0', bd=0, image=self.delete_img,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='search.gif')
        btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, image=self.refresh_img,
                               compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        self.v_img = tk.PhotoImage(file='v.gif')
        btn_v = tk.Button(toolbar, text='Заказать', bg='#d7d8e0', bd=0, image=self.v_img,
                               compound=tk.TOP, command=self.viv_dialog)
        btn_v.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'femali', 'worc', 'primechanie', 'description', 'costs', 'total'), height=15, show='headings')

        self.tree.column('ID', width=20, anchor=tk.CENTER)
        self.tree.column('femali', width=90, anchor=tk.CENTER)
        self.tree.column('worc', width=90, anchor=tk.CENTER)
        self.tree.column('primechanie', width=400, anchor=tk.NW)
        self.tree.column('description', width=100, anchor=tk.CENTER )
        self.tree.column('costs', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=90, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('femali', text = 'Фамилия')
        self.tree.heading('worc', text = 'Должность')
        self.tree.heading('primechanie', text = 'Примечание')
        self.tree.heading('description', text='Наименование')
        self.tree.heading('costs', text='Статья дохода/расхода')
        self.tree.heading('total', text='Сумма')

        self.tree.pack()

    def records(self, femali, worc, primechanie, description, costs, total):
        self.db.insert_data(femali, worc, primechanie, description, costs, total)
        self.view_records()

    def update_record(self, femali, worc, primechanie, description, costs, total):
        self.db.c.execute('''UPDATE vojg SET femali=?, worc=?, primechanie=?, description=?, costs=?, total=? WHERE ID=?''',
                          (femali, worc, primechanie, description, costs, total, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM vojg''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM vojg WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()
# Поиск по Фамилии
    def search_records(self, femali):
        femali = ('%' + femali + '%',)
        self.db.c.execute('''SELECT * FROM vojg WHERE femali LIKE ?''', femali)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()

    def viv_dialog(self):
        Child()   

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить доходы/расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_femali = tk.Label(self, text='Фамилия:')
        label_femali.place(x=50, y=10)
        label_worc = tk.Label(self, text='Должность:')
        label_worc.place(x=50, y=40)
        label_primechanie = tk.Label(self, text='Примечание')
        label_primechanie.place(x=50, y=70)
        label_description = tk.Label(self, text='Наименование:')
        label_description.place(x=50, y=100) 
        label_select = tk.Label(self, text='Статья дохода/расхода:')
        label_select.place(x=50, y=130)
        label_sum = tk.Label(self, text='Сумма:')
        label_sum.place(x=50, y=160)

        self.entry_femali = ttk.Entry(self)
        self.entry_femali.place(x=200, y= 10)

        self.entry_worc = ttk.Entry(self)
        self.entry_worc.place(x=200, y=40)

        self.entry_primechanie = ttk.Entry(self)
        self.entry_primechanie.place(x=200, y=70)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=100)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=160)

        self.combobox = ttk.Combobox(self, values=['', u'Доход', u'Расход', u'Баланс'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=130)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=190)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=190)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_femali.get(),
                                                                       self.entry_worc.get(),
                                                                       self.entry_primechanie.get(),                                                 
                                                                       self.entry_description.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_money.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=190)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_femali.get(),
                                                                          self.entry_worc.get(),
                                                                          self.entry_primechanie.get(),
                                                                          self.entry_description.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_money.get()))

        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM vojg WHERE id=?''', (self.view.tree.set(self.view.tree.selection()[0], '#1' ),))
        row = self.db.c.fetchone()
        self.entry_femali.insert(0, row[1])                                                                
        self.entry_worc.insert(0, row[2])
        self.entry_primechanie.insert(0, row[3])
        self.entry_description.insert(0, row[4])
        if row[4] != 'Доход':
            self.combobox.current(1)
        self.entry_money.insert(0, row[6])




class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('vojg.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS vojg (id integer primary key, femali text, worc text, primechanie text, description text, costs text, total real)''')
        self.conn.commit()

    def insert_data(self, femali, worc, primechanie, description, costs, total):
        self.c.execute('''INSERT INTO vojg(femali, worc, primechanie, description, costs, total) VALUES (?, ?, ?, ?, ?, ?)''',
                       (femali, worc, primechanie, description, costs, total))
        self.conn.commit()
        print(femali)


spisok = ['власов', 'маслов', 'чиграшов', 'успенский', 'закурдяев']

for sp in spisok:
    z = str(sp.title()) + " Водитель " + str(len(spisok))
    print(z)
# Преобразование текста   


with open('124.txt') as rusers_db:
        users_data = rusers_db.read()
        users = str(users_data)
            

with open('124.json') as vojg_db:
    vojg_data = vojg_db.read()
    rusers = vojg_data


r_s = []
p_s = []
r_s.append(rusers)
p_s.append(users)
y = ("Постоянныхх сотрудников 124.json " + str(len(r_s)))

for p in p_s:
    s = p.title()
    x = ("Временных сотрудников 124.txt " + str(len(r_s)))
for r in r_s:
    d = r.title()
print('\n124.txt\n\t' + s)
print('\n 124.json\n\t' + d)
print('\n' + z)


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Household financ")
    root.geometry("950x700+20+20")
    root.resizable(False, False)

    text = Text(width=75, height=50,bg="darkgreen",
            fg='white', wrap=WORD )

    label_femali = tk.Label(text="version: 0.0.1 Test.", fg='white', bg='#0000CD')
    label_femali.place(x=850, y=40)

    text.pack(side=LEFT)
    text.insert(1.0, "Список персонала!\n" + z + ':\n' + x + '\n' + y + '\n' + d +  ':\n' + s  )
    text.tag_add('title', 0.4, '1.end')
    text.tag_config('title', font=("Verdana", 15, 'bold'), justify=LEFT)

    def addItem():
        lbox.insert(END, entry.get())
        entry.delete(0, END)
 
    def delList():
        select = list(lbox.curselection())
        select.reverse()
        for i in select:
            lbox.delete(i)
 
    def saveList():
        a = [1, 2, 3, 4]
        f = open('124.json', 'a')
        f_2 = open('124.txt', 'a')
        f.writelines("\n".join(lbox.get(0, END)))
        f.close()
        f_2.writelines("\n".join(lbox.get(0, END)))
        f_2.close()
    
    lbox = Listbox(width=30, height=10)
    lbox.pack(side=LEFT)
    scroll = Scrollbar(command=lbox.yview)
    scroll.pack(side=RIGHT, fill=Y)
    lbox.config(yscrollcommand=scroll.set)
 
    f = Frame()
    f.pack(side=LEFT, padx=5)
    entry = Entry(f)
    entry.pack(anchor=N)
    badd = Button(f, text="Добавить", bg='green', command=addItem)
    badd.pack(fill=X)
    bdel = Button(f, text="Удалить", bg='red', command=delList)
    bdel.pack(fill=X)
    bsave = Button(f, text="Сохранить", bg='#d7d8e0', command=saveList)
    bsave.pack(fill=X)

    root.mainloop()
