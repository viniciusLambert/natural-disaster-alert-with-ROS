import os
import rospy
from std_msgs.msg import String


try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import pygubu


CURDIR = os.path.dirname(__file__)
UI_FILE = os.path.join(CURDIR, 'view/publisher.ui')

def cripto(local, desastre, data, horario):
    return local + "~" + desastre + "~" + data +"~"+ horario


class Application:

    def __init__(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()
        #2: Load an ui file
        builder.add_from_file(UI_FILE)
        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainwindow')
        #4: connect callbacks
        self.builder.connect_callbacks(self)

    def envia_aviso(self):
        local = ""
        horario = ""
        data = ""
        desastre = ""
        flag = ""

        entry = self.builder.get_object('lbl_local')
        local = entry.get()
        entry = self.builder.get_object('lbl_tipo')
        desastre = entry.get()
        entry = self.builder.get_object('lbl_dia')
        data = entry.get()
        entry = self.builder.get_object('lbl_mes')
        data += "/" + entry.get()
        entry = self.builder.get_object('lbl_ano')
        data += "/" + entry.get()
        entry = self.builder.get_object('lbl_hora')
        horario = entry.get()

        msg = cripto(local, desastre, data, horario)
        pub.publish(msg)

    def registrar_polo(self):
        local = ""
        entry = self.builder.get_object('lbl_local')
        local = entry.get()

        global pub
        pub = rospy.Publisher(local, String, queue_size=1)

    def run(self):
        self.mainwindow.mainloop()



if __name__ == '__main__':
    rospy.init_node("pub_UNIFEI", anonymous=True)
    app = Application()
    app.run()
