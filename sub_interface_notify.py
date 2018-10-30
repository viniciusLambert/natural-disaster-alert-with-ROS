try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
try:
    from tkinter import *
except:
    from Tkinter import *

import time
import pygubu
import rospy
from notify_run import Notify
notify = Notify()
from std_msgs.msg import String

class Application:
    def __init__(self, master = None):

        self.fontePadrao = ("Arial", "12")

        self.notify = Frame(master)
        self.notify["pady"] = 10
        self.notify["padx"] = 10
        self.notify.pack()

        self.w1 = Frame(master)
        self.w1["pady"] = 6
        self.w1["padx"] = 20
        self.w1.pack()

        self.lNot = Label(self.notify, text="Notify: ", width=10, font=self.fontePadrao)
        self.lNot.pack(side=LEFT)
        self.link = Listbox(self.notify, width=60, height=1, font=self.fontePadrao)
        self.link.pack(side=LEFT, fill=BOTH, expand=True)
        self.link.insert(END,notify.info().channel_page)

        self.registrar = Button(self.notify, text="Novo Link", font=self.fontePadrao)
        self.registrar["command"] = self.registrar_push
        self.registrar.pack(side=RIGHT)

        self.w11 = Frame(master)
        self.w11["pady"] = 0
        self.w11["padx"] = 20
        self.w11.pack()


        self.w2 = Frame(master)
        self.w2["padx"] = 10
        self.w2["pady"] = 10
        self.w2.pack()
        self.ll = Label(self.w2, text="Polos inscritos:", font=self.fontePadrao, width=85, justify=LEFT, anchor=W)
        self.ll.pack()

        self.scrollbar2 = Scrollbar(self.w2)
        self.scrollbar2.pack(side=LEFT, fill=Y)
        self.listbox2 = Listbox(self.w2, yscrollcommand=self.scrollbar2.set, width=14, font="Arial 12 bold")
        self.listbox2.pack(side=LEFT)
        self.scrollbar2.config(command=self.listbox2.yview)

        self.scrollbar = Scrollbar(self.w2)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.w2, yscrollcommand=self.scrollbar.set, fg='red', width=55, font=self.fontePadrao)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)

        self.w4 = Frame(master)
        self.w4["padx"] = 10
        self.w4["pady"] = 10
        self.w4.pack()

        self.dpolo = Label(self.w1, text="Digite o polo", font=self.fontePadrao)
        self.dpolo.pack(side=LEFT)
        self.polo = Entry(self.w1, width=30, font=self.fontePadrao)
        self.polo.pack(side=LEFT)
        self.inscr = Button(self.w1, text="inscrever", font=self.fontePadrao)
        self.inscr["command"] = self.registrar_polo
        self.inscr.pack(side=LEFT)

        self.listbox.insert(END, "Avisos!")

        self.sair = Button(self.w4, text="Sair", font=self.fontePadrao)
        self.sair["command"] = self.w2.quit
        self.sair.pack()


    def get_polo(self):
        text = self.polo.get()
        return text

    def registrar_push(self):
        notify.register()
        self.link.delete(0,END)
        self.link.insert(END,notify.info().channel_page)
        return
    def registrar_polo(self):
        self.listbox2.insert(END, self.polo.get())
        main(self)

    
    def warn(self, local, desastre, data, horario):
        texto1 = ('-----------------------------AVISO-------------------------------------')
        texto2 = ('-----------------------------AVISO-------------------------------------')
        texto3 = ('Evacuar area de %s previsao de %s no dia %s as %s' % (local, desastre, data, horario))
        notify.send('Evacuar area de %s previsao de %s no dia %s as %s' % (local, desastre, data, horario))
        self.listbox.insert(END, "")
        self.listbox.insert(END, texto1)
        self.listbox.insert(END, texto2)
        self.listbox.insert(END, texto3)
        self.listbox.yview(END)

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
