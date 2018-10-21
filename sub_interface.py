try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
try:
    from tkinter import *
except:
    from Tkinter import *

import pygubu
import rospy

from std_msgs.msg import String

class Application:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial", "10")
        self.w1 = Frame(master)
        self.w1["pady"] = 10
        self.w1.pack()
        self.w2 = Frame(master)
        self.w2["pady"] = 10
        self.w2.pack()
        self.w3 = Frame(master)
        self.w3["pady"] = 10
        self.w3.pack()

        self.dpolo = Label(self.w1, text="Digite o polo", font=self.fontePadrao)
        self.dpolo.pack(side=LEFT)
        self.polo = Entry(self.w1, width=40, font=self.fontePadrao)
        self.polo.pack(side=LEFT)

        self.inscr = Button(self.w1, text="Inscrever polo", font=self.fontePadrao)
        self.inscr["command"] = self.registrar_polo
        self.inscr.pack(side=LEFT)

        self.aviso = Label(self.w2, text="Avisos!", font=self.fontePadrao)
        self.aviso.pack()

        self.sair = Button(self.w3, text="Sair", font=self.fontePadrao)
        self.sair["command"] = self.w2.quit
        self.sair.pack()


    def get_polo(self):
        text = self.polo.get()
        return text

    def registrar_polo(self):
        main(self)

    def warn(self, local, desastre, data, horario):
        self.aviso["text"] = self.aviso.cget("text")+('\n-----------------------------AVISO----------------------------------------\n'+
                            '-----------------------------AVISO----------------------------------------\n'+
                            'Evacuar area previsao de %s no dia %s as %s\n' % (desastre, data, horario))
        self.aviso['bg'] = "red"


def descripto(msg):
    index = 0
    local = ""
    desastre = ""
    horario = ""
    data = ""

    while(msg[index]!='~'):
        local += msg[index]
        index += 1
    index += 1
    while(msg[index]!='~'):
        desastre += msg[index]
        index += 1
    index += 1

    while(msg[index]!='~'):
        data += msg[index]
        index += 1
    index += 1
    for x in msg[index:]:
        horario += x

    return local, desastre, data, horario

def mostrarmsg(local, desastre, data, horario):
    app.warn(local, desastre, data, horario)


def callback(x):
    local, desastre, data, horario = descripto(x.data)
    mostrarmsg(local, desastre, data, horario)


def main(app):
    local = ""
    horario = ""
    data = ""
    desastre = ""
    flag = ""

    local = app.get_polo()


    rospy.init_node("SD_sub", anonymous=True)
    rospy.Subscriber(local, String, callback)
    print("registro realizado")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
