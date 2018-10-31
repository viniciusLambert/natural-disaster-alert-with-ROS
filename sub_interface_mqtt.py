try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
try:
    from tkinter import *
except:
    from Tkinter import *

import paho.mqtt.client as mqtt
import time
import pygubu
import rospy

from std_msgs.msg import String

client = mqtt.Client()



class Application:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial", "12")

        self.mqtt = Frame(master, relief=SUNKEN, background="gray")
        self.mqtt["pady"] = 5
        self.mqtt["padx"] = 5

        self.mqtt.pack()

        self.uName = Frame(self.mqtt, background="white")
        self.uName.pack()

        self.username = Label(self.uName, text="Username:", width=10, font=self.fontePadrao, anchor=W, background="white")
        self.username.pack(side=LEFT)
        self.userEntry = Entry(self.uName,width=30, font=self.fontePadrao)
        self.userEntry.pack(side=LEFT)

        self.uSenha = Frame(self.mqtt, background="white")
        self.uSenha.pack()

        self.senha = Label(self.uSenha, text="Senha:", width=10, font=self.fontePadrao, anchor=W, background="white")
        self.senha.pack(side=LEFT)
        self.senhaEntry = Entry(self.uSenha, width=30, font=self.fontePadrao, show="*")
        self.senhaEntry.pack(side=LEFT)

        self.uPort = Frame(self.mqtt, background="white")
        self.uPort.pack()

        self.port = Label(self.uPort, text="Port:", width=10, font=self.fontePadrao, anchor=W, background="white")
        self.port.pack(side=LEFT)
        self.portEntry = Entry(self.uPort, width=30, font=self.fontePadrao)
        self.portEntry.pack(side=LEFT)

        self.uHost = Frame(self.mqtt, background="white")
        self.uHost.pack()

        self.host = Label(self.uHost, text="Host:", width=10, font=self.fontePadrao, anchor=W, background="white")
        self.host.pack(side=LEFT)
        self.hostEntry = Entry(self.uHost, width=30, font=self.fontePadrao)
        self.hostEntry.pack(side=LEFT)

        self.userEntry.insert(0, "bbgeduns")
        self.senhaEntry.insert(0, "XZP22UwH0eRt")
        self.portEntry.insert(0, 18044)
        self.hostEntry.insert(0, "m15.cloudmqtt.com")

        self.wPolo = Frame(master)
        self.wPolo["pady"] = 20
        self.wPolo["padx"] = 20
        self.wPolo.pack()

        self.dpolo = Label(self.wPolo, text="Digite o polo: ", font=self.fontePadrao)
        self.dpolo.pack(side=LEFT)
        self.polo = Entry(self.wPolo, width=30, font=self.fontePadrao)
        self.polo.pack(side=LEFT)
        self.inscr = Button(self.wPolo, text="submit", font="Arial 10 bold", activebackground="green", activeforeground="white", width=8)
        self.inscr["command"] = self.registrar_polo
        self.inscr.pack(side=LEFT)

        self.wid = Frame(master)
        self.wid.pack()
        self.lab = Label(self.wid, text=" Polos inscritos:", font=self.fontePadrao, width=70, anchor=W)
        self.lab.pack()

        self.scrollbar2 = Scrollbar(self.wid)
        self.scrollbar2.pack(side=LEFT, fill=Y)
        self.listbox2 = Listbox(self.wid, yscrollcommand=self.scrollbar2.set, width=14, font="Arial 12 bold")
        self.listbox2.pack(side=LEFT)
        self.scrollbar2.config(command=self.listbox2.yview)

        self.scrollbar = Scrollbar(self.wid)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.wid, yscrollcommand=self.scrollbar.set, fg='red', width=55, font=self.fontePadrao)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.insert(END, "Avisos!")

        self.wSair = Frame(master)
        self.wSair["padx"] = 10
        self.wSair["pady"] = 10
        self.wSair.pack()
        self.sair = Button(self.wSair, text="Sair", font=self.fontePadrao)
        self.sair["command"] = self.mqtt.quit
        self.sair.pack()


    def get_polo(self):
        text = self.polo.get()
        return text

    def registrar_polo(self):
        self.listbox2.insert(END, self.polo.get())
        main(self)

    def inserir_numero(self):
        self.listboxN.insert(END, self.num.get())
        main(self)

    def warn(self, local, desastre, data, horario):
        client.on_connect = on_connect
        client.on_message = on_message

        print(self.userEntry.get(), self.senhaEntry.get(),self.hostEntry.get(), int(self.portEntry.get()))
        client.username_pw_set(self.userEntry.get(), self.senhaEntry.get())
        client.connect(self.hostEntry.get(), int(self.portEntry.get()))

        client.loop_start()
        time.sleep(1)

        client.publish("Teste", 'Evacuar area de %s previsao de %s no dia %s as %s' % (local, desastre, data, horario))
        time.sleep(5)

        client.loop_stop()
        client.disconnect()


        texto1 = ('-----------------------------AVISO-------------------------------------')
        texto2 = ('Evacuar area de %s previsao de %s no dia %s as %s' % (local, desastre, data, horario))
        self.listbox.insert(END, "")
        self.listbox.insert(END, texto1)
        self.listbox.insert(END, texto1)
        self.listbox.insert(END, texto2)
        self.listbox.yview(END)

def on_connect( client, userdata, flags, rc):
	print ("Conectado com o codigo:" +str(rc))
	#Topico Subscribe
	client.subscribe("Teste/#")

def on_message( client, userdata, msg):
	print ( str(msg.payload) )


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
