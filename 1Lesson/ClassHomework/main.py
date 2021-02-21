from dataclasses import dataclass
import configparser
from tkinter import *
import csv
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.exc import NoResultFound

step = 1
mass = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

window = Tk()
window.title("Window")
window.geometry("500x500")

tt = create_engine("sqlite:///game_base.db")
base = declarative_base(bind=tt)

ses = sessionmaker(bind=tt)
Session = scoped_session(ses)

def Return_player_of_leter(bukv):
    if bukv == "x":
        return player_x
    else:
        return player_o


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

    # with open("game_save.csv", "w") as f:
    #     csv_writer = csv.writer(f, lineterminator='\r')
    #     csv_writer.writerows(mass)

    for i in range(3):
        if mass[i][0] == mass[i][1] and mass[i][0] == mass[i][2]:
            #print("выйграл", mass[i][0])\
            PlayerG = Return_player_of_leter(mass[i][0]).base_player
            PlayerG.wines += 1
            win_or_not = Label(window, font="Tahoma 20", text="Выйграл " + PlayerG.playername + " (" + str(PlayerG.wines) + ")")
            win_or_not.place(x=50, y=325, width=200, height=33)
            reset_game()

            session.commit()
        if mass[0][i] == mass[1][i] and mass[0][i] == mass[2][i]:
            #print("выйграл", mass[i][0])\
            PlayerG = Return_player_of_leter(mass[1][i]).base_player
            PlayerG.wines += 1
            win_or_not = Label(window, font="Tahoma 20", text="Выйграл " + PlayerG.playername + " (" + str(PlayerG.wines) + ")")
            win_or_not.place(x=50, y=325, width=200, height=33)
            reset_game()

            session.commit()

    if mass[0][0] == mass[1][1] and mass[0][0] == mass[2][2]:
        #print("выйграл", mass[0][0])\
        PlayerG = Return_player_of_leter(mass[0][0]).base_player
        PlayerG.wines += 1
        win_or_not = Label(window, font="Tahoma 20", text="Выйграл " + PlayerG.playername + " (" + str(PlayerG.wines) + ")")
        win_or_not.place(x=50, y=325, width=200, height=33)
        reset_game()

        session.commit()

    if mass[0][2] == mass[1][1] and mass[0][2] == mass[2][0]:
        #print("выйграл", mass[0][2])\
        PlayerG = Return_player_of_leter(mass[0][2]).base_player
        PlayerG.wines += 1
        win_or_not = Label(window, font="Tahoma 20", text="Выйграл " + PlayerG.playername + " (" + str(PlayerG.wines) + ")")
        win_or_not.place(x=50, y=325, width=200, height=33)
        reset_game()
        session.commit()

    have_cifr = False

    for i in mass:
        for g in i:
            rez = str(g).isdigit()
            if rez:
                have_cifr = True

    if not have_cifr:
       reset_game()

def creat_table_base():
    meta = MetaData()

    students = Table(
        'player', meta,
        Column('id', Integer, primary_key=True),
        Column('playername', String, unique=True),
        Column('wines', Integer, default=0),
    )

    meta.create_all(tt)

class Player(base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    playername = Column(String(32), unique=True)
    wines = Column(Integer, default=0)

    def __str__(self):
        return f"Игрок - {self.playername}, счет у этого игрока - {self.wines}"

    def __repr__(self):
        return str(self)

def creat_new_user(name):
    player_data = Player(playername=name)
    session.add(player_data)
    session.commit()
    return player_data

def change_name(event):
    a = text2.get()
    try:
        user_bd = session.query(Player).filter_by(playername=a).one()
    except NoResultFound:
        user_bd = creat_new_user(a)

    if label2["text"] == "":
        player_x.base_player = user_bd
        player_x.symbol = "x"
        label2["text"] = f"игрок x: {player_x.base_player.playername} ({player_x.base_player.wines})"
        label["text"] = "Представься o:"
        text2.delete(0, END)
    else:
        player_o.base_player = user_bd
        player_o.symbol = "o"
        label2["text"] = f"игрок x: {player_x.base_player.playername} ({player_x.base_player.wines}), игрок o: {player_o.base_player.playername} ({player_o.base_player.wines})"
        hide_hello()
        show_button()


@dataclass
class Player_game:
    base_player: Player
    symbol: str

# with open("game_save.csv") as f:
#     mass = []
#     csv_reader = csv.reader(f)
#     for row in csv_reader:
#         mass.append(row)
#     print(mass)

def returne_mass_count(x, y):
    if mass[x][y] == "x" or mass[x][y] == "o":
     return mass[x][y]
    else:
     return ""

def show_hello():
    label.place(x=0, y=10, width=200, height=33)
    text2.place(x=200, y=10, width=300, height=33)
    label2.place(x=0, y=350, width=400, height=33)
    # label3.place(x=0, y=70, width=200, height=33)

def hide_hello():
    label.place_forget()
    text2.place_forget()
    # label2.place_forget()
    # label3.place_forget()

def show_button():
    button1.place(x=0, y=0, width=100, height=100)
    button2.place(x=100, y=0, width=100, height=100)
    button3.place(x=200, y=0, width=100, height=100)
    button4.place(x=0, y=100, width=100, height=100)
    button5.place(x=100, y=100, width=100, height=100)
    button6.place(x=200, y=100, width=100, height=100)
    button7.place(x=0, y=200, width=100, height=100)
    button8.place(x=100, y=200, width=100, height=100)
    button9.place(x=200, y=200, width=100, height=100)

def hide_button():
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    button7.place_forget()
    button8.place_forget()
    button9.place_forget()

def reset_game():
    global mass
    button1["text"] = ""
    button2["text"] = ""
    button3["text"] = ""
    button4["text"] = ""
    button5["text"] = ""
    button6["text"] = ""
    button7["text"] = ""
    button8["text"] = ""
    button9["text"] = ""

    mass = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # with open("game_save.csv", "w") as f:
    #     csv_writer = csv.writer(f, lineterminator='\r')
    #     csv_writer.writerows(mass)

"""
Описания приветствия.
"""
tt = Player()
player_x = Player_game(tt, "")
player_o = Player_game(tt, "")

label = Label(window, text=f"Представься x:", font="Tahoma 19")
text2 = Entry(window, font="Tahoma 20")
text2.bind('<Return>', change_name)

label2 = Label(window, text="", font="Tahoma 19")
label3 = Label(window, text="", font="Tahoma 19")

"""
Описание кнопок
"""

button1 = Button(window, text=returne_mass_count(0, 0), command=lambda: PutButton(button1, 0, 0), font="Tahoma 60")
button2 = Button(window, text=returne_mass_count(0, 1), command=lambda: PutButton(button2, 0, 1), font="Tahoma 60")
button3 = Button(window, text=returne_mass_count(0, 2), command=lambda: PutButton(button3, 0, 2), font="Tahoma 60")
button4 = Button(window, text=returne_mass_count(1, 0), command=lambda: PutButton(button4, 1, 0), font="Tahoma 60")
button5 = Button(window, text=returne_mass_count(1, 1), command=lambda: PutButton(button5, 1, 1), font="Tahoma 60")
button6 = Button(window, text=returne_mass_count(1, 2), command=lambda: PutButton(button6, 1, 2), font="Tahoma 60")
button7 = Button(window, text=returne_mass_count(2, 0), command=lambda: PutButton(button7, 2, 0), font="Tahoma 60")
button8 = Button(window, text=returne_mass_count(2, 1), command=lambda: PutButton(button8, 2, 1), font="Tahoma 60")
button9 = Button(window, text=returne_mass_count(2, 2), command=lambda: PutButton(button9, 2, 2), font="Tahoma 60")

show_hello()

"""
Открытие сессии
"""

session = Session()

# try:
#     user_bd = session.query(Player).filter_by(playername=my_name).one()
# except NoResultFound:
#     user_bd = creat_new_user(my_name)
#
# user_bd.wines = 2
# print(user_bd.wines)
# print(user_bd.playername)
#
# session.commit()
#
# session.close()

window.mainloop()


