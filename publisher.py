#!/usr/bin/env python
import rospy

from std_msgs.msg import String

def cripto(local, desastre, data, horario):
    return local + "~" + desastre + "~" + data +"~"+ horario



def main():
    local = ""
    horario = ""
    data = ""
    desastre = ""
    flag = ""

    local = raw_input("\n\ninsira o local onde se deseja criar uma central de aviso.\n")
    print("CENTRAL DE AVISO CRIADA COM SUCESSO.\n")

    pub = rospy.Publisher(local, String, queue_size=1)
    rospy.init_node("China_pub", anonymous=True)

    while(True):
        flag = raw_input("Para cria um aviso digite AVISO\n")

        if(flag == "AVISO"):
            desastre = raw_input("informe o tipo de desastre\n")
            data = raw_input("digite o dia(numero) do desastre\n")
            data += "/"
            data += raw_input("digite o mes do desatre\n")
            data += "/"
            data += raw_input("digite o ano do desastre\n")
            horario = raw_input("digite o horario do desaste (Hora:Minutos)\n")


            print("Informacoes: %s em %s no dia %s as %s" % (desastre, local, data, horario))
            flag = raw_input("para confirmar o aviso digite 'ENVIAR'\n")
            if(flag == "ENVIAR"):
                msg = cripto(local, desastre, data, horario)
                pub.publish(msg)
                print("AVISO ENVIADO")

            else:
                print("Aviso cancelado")
        else:
            print("Codigo nao identificado")



if __name__ == '__main__':
    main()
