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

        self.mqtt = Frame(master)
        self.mqtt["pady"] = 10
        self.mqtt["padx"] = 10
        self.mqtt.pack()

        self.uName = Frame(self.mqtt)
        self.uName.pack()

        self.username = Label(self.uName, text="Username:", width=10, font=self.fontePadrao, anchor=W)
        self.username.pack(side=LEFT)
        self.userEntry = Entry(self.uName,width=30, font=self.fontePadrao)
        self.userEntry.pack(side=LEFT)


        self.uSenha = Frame(self.mqtt)
        self.uSenha.pack()

        self.senha = Label(self.uSenha, text="Senha:", width=10, font=self.fontePadrao, anchor=W)
        self.senha.pack(side=LEFT)
        self.senhaEntry = Entry(self.uSenha, width=30, font=self.fontePadrao, show="*")
        self.senhaEntry.pack(side=LEFT)

        self.uPort = Frame(self.mqtt)
        self.uPort.pack()

        self.port = Label(self.uPort, text="Port:", width=10, font=self.fontePadrao, anchor=W)
        self.port.pack(side=LEFT)
        self.portEntry = Entry(self.uPort, width=30, font=self.fontePadrao)
        self.portEntry.pack(side=LEFT)

        self.uHost = Frame(self.mqtt)
        self.uHost.pack()

        self.host = Label(self.uHost, text="Host:", width=10, font=self.fontePadrao, anchor=W)
        self.host.pack(side=LEFT)
        self.hostEntry = Entry(self.uHost, width=25, font=self.fontePadrao)
        self.hostEntry.pack(side=LEFT)

        self.userEntry.insert(0, "bbgeduns")
        self.senhaEntry.insert(0, "XZP22UwH0eRt")
        self.portEntry.insert(0, 18044)
        self.hostEntry.insert(0, "m15.cloudmqtt.com")


        self.go = Button(self.uHost, text="go", font=self.fontePadrao, anchor=E)
        #self.go["command"] =
        self.go.pack(side=LEFT)

        self.wSair = Frame(master)
        self.wSair["padx"] = 10
        self.wSair["pady"] = 10
        self.wSair.pack()

        self.w1 = Frame(master)
        self.w1["pady"] = 6
        self.w1["padx"] = 20
        self.w1.pack()

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

        client.publish("ALERTA", 'Evacuar area de %s previsao de %s no dia %s as %s' % (local, desastre, data, horario))
        time.sleep(5)

        client.loop_stop()
        client.disconnect()



        texto1 = ('-----------------------------AVISO-------------------------------------')
        texto2 = ('-----------------------------AVISO-------------------------------------')
        texto3 = ('Evacuar area de %s previsao de %s no dia %s as %s' % (local, desastre, data, horario))
        self.listbox.insert(END, "")
        self.listbox.insert(END, texto1)
        self.listbox.insert(END, texto2)
        self.listbox.insert(END, texto3)
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
