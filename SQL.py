import sqlite3
from tkinter import *


def results(text, score):
    write_connection = sqlite3.connect("my_database.db")
    write_cursor = write_connection.cursor()
    write_cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
        username TEXT,
        userscore INTEGER
        )""")
    username = str(text)
    userscore = int(score)
    write_cursor.execute('INSERT INTO Users (username, userscore) VALUES (?, ?)',
                         (username, userscore))
    write_connection.commit()
    write_connection.close()


def get_data():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users')
    query = "SELECT username, userscore FROM Users ORDER BY userscore DESC LIMIT 10"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    print(data)
    return data


def save_data(text_entry, scores):
    write_connection = sqlite3.connect("my_database.db")
    write_cursor = write_connection.cursor()
    write_cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
           username TEXT NOT NULL,
           userscore INTEGER
           )""")
    username = str(text_entry.get())
    userscore = int(scores.amount_friends)
    write_cursor.execute('INSERT INTO Users (username, userscore) VALUES (?, ?)',
                         (username, userscore))
    write_connection.commit()
    write_connection.close()
    print("Сохраненный текст:")
    print(username)


def name(scores):
    window = Tk()
    window.title("Введите имя вашего персонажа")
    window.geometry("300x250")
    frame = Frame(window, padx=50, pady=25)
    frame.pack(expand=True)
    text_entry = Entry(frame)
    text_entry.grid(row=4, column=1, pady=5)

    save_button = Button(
        frame,
        text="Сохранить",
        command=lambda: save_data(text_entry, scores)
    )
    save_button.grid(row=5, column=1)
    window.mainloop()
