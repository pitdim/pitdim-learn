import configparser
from tkinter import *
import csv
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
step = 1
mass = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def PutButton(Obj,Stroka, Stolb):
    global step

    if step == 1:
        if Obj["text"] == "":
            Obj.config(text="x")
            step = 0

    elif step == 0:
        if Obj["text"] == "":
            Obj.config(text="o")
            step = 1


    mass[Stroka][Stolb] = Obj["text"]

    with open("game_save.csv", "w") as f:
        csv_writer = csv.writer(f, lineterminator='\r')
        csv_writer.writerows(mass)
        # csv_writer.writerows(mass[1])
        # csv_writer.writerows(mass[2])

    for i in range(2):
        if mass[i][0] == mass[i][1] and mass[i][0] == mass[i][2]:
            #print("выйграл", mass[i][0])
            win_or_not = Label(window, font="Tahoma 20", text="Выйграл " + str(mass[i][0]))
            win_or_not.place(x=350, y=50, width=300, height=33)
        if mass[0][i] == mass[1][i] and mass[0][i] == mass[2][i]:
            #print("выйграл", mass[i][0])
            win_or_not = Label(window, font="Tahoma 20", text="Выйграл " + str(mass[1][i]))
            win_or_not.place(x=350, y=50, width=300, height=33)

    if mass[0][0] == mass[1][1] and mass[0][0] == mass[2][2]:
        #print("выйграл", mass[0][0])
        win_or_not = Label(window, font="Tahoma 20", text="Выйграл " + str(mass[0][0]))
        win_or_not.place(x=350, y=50, width=300, height=33)
    if mass[0][2] == mass[1][1] and mass[0][2] == mass[2][0]:
        #print("выйграл", mass[0][2])
        win_or_not = Label(window, font="Tahoma 20", text="Выйграл " + str(mass[0][2]))
        win_or_not.place(x=350, y=50, width=300, height=33)


def change_name(event):
    with open("config.ini", "w") as f:
        my_config = configparser.ConfigParser()
        my_config.add_section("main")
        my_config.set("main", "name", text2.get())
        my_config.write(f)


window = Tk()
window.title("Window")
window.geometry("800x600")

my_config = configparser.ConfigParser()
my_config.read("config.ini")




try:
    name_games = my_config["main"]["name"]

    label = Label(window, text="Приветствую! " + name_games, font="Tahoma 19")
    label.place(x=100, y=0, width=800, height=33)
except KeyError:
    label = Label(window, text="Представься:", font="Tahoma 19")
    label.pack()

    text2 = Entry(window, font="Tahoma 20")
    text2.place(x=300, y=50, width=800, height=33)
    text2.bind('<Return>', change_name)

tt = create_engine("sqlite:///game_base.db")
base = declarative_base(bind=tt)
ses = sessionmaker(bind=tt)
Session = scoped_session(ses)

class Player(base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    playername = Column(String(32), unique=True)
    wines = Column(Integer)


user = Player(playername="Kolya")
session = Session()
session.add(user)
session.close()

with open("game_save.csv") as f:
    mass = []
    csv_reader = csv.reader(f)
    for row in csv_reader:
        mass.append(row)
    print(mass)

def returne_mass_count(x, y):
    if mass[x][y] == "x" or mass[x][y] == "o":
     return mass[x][y]
    else:
     return ""

button1 = Button(window, text=returne_mass_count(0, 0), command=lambda: PutButton(button1, 0, 0), font="Tahoma 60")
button1.place(x=0, y=0, width=100, height=100)

button2 = Button(window, text=returne_mass_count(0, 1), command=lambda: PutButton(button2, 0, 1), font="Tahoma 60")
button2.place(x=100, y=0, width=100, height=100)

button3 = Button(window, text=returne_mass_count(0, 2), command=lambda: PutButton(button3, 0, 2), font="Tahoma 60")
button3.place(x=200, y=0, width=100, height=100)

button4 = Button(window, text=returne_mass_count(1, 0), command=lambda: PutButton(button4, 1, 0), font="Tahoma 60")
button4.place(x=0, y=100, width=100, height=100)

button5 = Button(window, text=returne_mass_count(1, 1), command=lambda: PutButton(button5, 1, 1), font="Tahoma 60")
button5.place(x=100, y=100, width=100, height=100)

button6 = Button(window, text=returne_mass_count(1, 2), command=lambda: PutButton(button6, 1, 2), font="Tahoma 60")
button6.place(x=200, y=100, width=100, height=100)

button7 = Button(window, text=returne_mass_count(2, 0), command=lambda: PutButton(button7, 2, 0), font="Tahoma 60")
button7.place(x=0, y=200, width=100, height=100)

button8 = Button(window, text=returne_mass_count(2, 1), command=lambda: PutButton(button8, 2, 1), font="Tahoma 60")
button8.place(x=100, y=200, width=100, height=100)

button9 = Button(window, text=returne_mass_count(2, 2), command=lambda: PutButton(button9, 2, 2), font="Tahoma 60")
button9.place(x=200, y=200, width=100, height=100)


window.mainloop()


