import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
 
 
if __name__ == '__main__':
    create_connection(r"D:\Curs Python\databse-proiect.db")



def adauga_ang():
    try:
        sqliteConnection = sqlite3.connect("databse-proiect.db")
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO `Angajat`
                            ('CNP', 'Nume', 'Salar') 
                            VALUES 
                            (%s, %s, %s)"""

        count = cursor.execute(sqlite_insert_query, e_cnp.get(), e_nume.get(), e_salariu.get())
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")



def query():
    try:
        sqliteConnection = sqlite3.connect('databse-proiect.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT *, oid from Angajat"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        print_records = ''        

        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + '\n'

        query_label = Label(window, text = print_records)
        query_label.grid(row = 6, column = 0, columnspan = 2)


        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


from tkinter import *

window = Tk()
window.title('Proiect Jurchela Andrei')

def adauga():
    add_window = Tk()
    add_window.title('Adauga angajat')
    l1 = Label(add_window, text = "Adauga un angajat")
    l1.grid(row = 0, column = 0)

    l_cnp = Label(add_window, text = "CNP")
    l_cnp.grid(row = 1, column = 0)

    e_cnp = Entry(add_window)
    e_cnp.grid(row = 1, column = 1)

    l_nume = Label(add_window, text = "Nume")
    l_nume.grid(row = 2, column = 0)

    e_nume = Entry(add_window)
    e_nume.grid(row = 2, column = 1)

    l_salariu = Label(add_window, text = "Salariu")
    l_salariu.grid(row = 3, column = 0)

    e_salariu = Entry(add_window)
    e_salariu.grid(row = 3, column = 1)

    def adauga_ang():
        try:
            sqliteConnection = sqlite3.connect("databse-proiect.db")
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")

            
            count = cursor.execute('INSERT INTO Angajat values (?, ?, ?)', (e_cnp.get(), e_nume.get(), e_salariu.get()))
            sqliteConnection.commit()
            print("Record inserted successfully into Angajat table ", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                add_window.destroy()
                print("The SQLite connection is closed")
    
    b_ok = Button(add_window, text = "Ok", command = adauga_ang)
    b_ok.grid(row = 4, column = 0)

def delete():
    del_window = Tk()
    del_window.title('Sterge Angajat')
    def del_ang():
        conn = sqlite3.connect('databse-proiect.db')
        c = conn.cursor()
        print("Connected to SQLite")

        c.execute("DELETE from Angajat WHERE oid = " + e_delete.get())
        e_delete.delete(0, END)

        del_window.destroy()

        conn.commit()
        conn.close()

    l_delete = Label(del_window, text = "Introduceti ID-ul angajatului pe care doriti sa il stergeti: ")
    l_delete.grid(row = 0, column = 0, padx = (10, 0), pady = (0, 10))

    e_delete = Entry(del_window)
    e_delete.grid(row = 1, column = 0, padx = (10, 0), pady = (0, 10))

    b_del_ok = Button(del_window, text = "Ok", command = del_ang)
    b_del_ok.grid(row = 2, column = 0, padx = (10, 0), pady = (0,10))


def save():
    conn = sqlite3.connect('databse-proiect.db')
    c = conn.cursor()
    print("Conectat la SQLite")

    record_id = e_edit.get() 

    c.execute("""UPDATE Angajat SET 
        CNP = :cnp,
        Nume = :nume,
        Salar = :salariu

        WHERE oid = :oid""",
        {
            'cnp' :  e_cnp_edit.get(),
            'nume' : e_nume_edit.get(),
            'salariu' : e_salariu_edit.get(),

            'oid' : record_id
        })


    conn.commit()
    conn.close()

    edit_new_win.destroy()
    edit_window.destroy()

 
def edit():
    global edit_window
    edit_window = Tk()
    edit_window.title('Modifica date')
    l_edit = Label(edit_window, text = "Introduceti ID: ")
    l_edit.grid(row = 0, column = 0, padx = (10, 0), pady = (0, 10))

    global e_edit
    e_edit = Entry(edit_window)
    e_edit.grid(row = 1, column = 0, padx = 10, pady = (0, 10))

    def edit_new():
        global edit_new_win
        edit_new_win = Tk()
        edit_new_win.title('Modifica date')

        
        conn = sqlite3.connect('databse-proiect.db')
        c = conn.cursor()
        print("Connected to SQLite")

        record_id = e_edit.get()

        sqlite_select_query = ("SELECT * FROM Angajat WHERE oid = " + record_id)
        c.execute(sqlite_select_query)
        records = c.fetchall()

        conn.commit()
        conn.close()

        global e_cnp_edit
        global e_nume_edit
        global e_salariu_edit

        l_cnp_edit = Label(edit_new_win, text = "CNP")
        l_cnp_edit.grid(row = 1, column = 0)

        e_cnp_edit = Entry(edit_new_win)
        e_cnp_edit.grid(row = 1, column = 1, padx = 10, pady = (10, 0))

        l_nume_edit = Label(edit_new_win, text = "Nume")
        l_nume_edit.grid(row = 2, column = 0)

        e_nume_edit = Entry(edit_new_win)
        e_nume_edit.grid(row = 2, column = 1, padx = 10, pady = (10, 0))

        l_salariu_edit = Label(edit_new_win, text = "Salariu")
        l_salariu_edit.grid(row = 3, column = 0)

        e_salariu_edit = Entry(edit_new_win)
        e_salariu_edit.grid(row = 3, column = 1, padx = 10, pady = 10)

        b_save = Button(edit_new_win, text = "Salvati modificarile", command = save)
        b_save.grid(row= 4, column = 0, padx = 10, pady = 10)

        #Loop prin rezultate
        for record in records:
            e_cnp_edit.insert(0, record[0])
            e_nume_edit.insert(0, record[1])
            e_salariu_edit.insert(0, record[2])

    b_ok_edit = Button(edit_window, text = "Ok", command = edit_new)
    b_ok_edit.grid(row = 2, column = 0, padx = 10, pady = (10,0))

def sal_5():
    conn = sqlite3.connect('databse-proiect.db')
    c = conn.cursor()
    print("Conectat la SQLite")


    c.execute('UPDATE Angajat SET Salar = Salar - (0.05 * Salar)')
    
    conn.commit()
    conn.close()


b1 = Button(window, text = "Adauga angajat", width = 30, command = adauga)
b1.grid(row = 0, column = 0, padx = 20, pady = (10, 2))

b2 = Button(window, text = "Sterge angajat", width = 30, command = delete)
b2.grid(row= 1, column = 0, padx = 5, pady = 2)

b2 = Button(window, text = "Modifica datele angajatilor", width = 30, command = edit)
b2.grid(row= 2, column = 0, padx = 5, pady = 2)

b2 = Button(window, text = "Vezi toti angajatii + datele", width = 30, command = query)
b2.grid(row= 3, column = 0, padx = 5, pady = 2)

b2 = Button(window, text = "Scade salariul cu 5% (tuturor)", width = 30, command = sal_5)
b2.grid(row= 4, column = 0, padx = 5, pady = (2,10))
window.mainloop()