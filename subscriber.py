import rospy

from std_msgs.msg import String

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
    print('\033[31m'+"--------------------AVISO-------------------------"+'\033[0;0m');
    print('\033[31m'+"--------------------AVISO-------------------------"+'\033[0;0m');
    print('\033[31m'+"--------------------AVISO-------------------------"+'\033[0;0m');
    print("Evacuar area previsao de %s no dia %s as %s\n" % (desastre, data, horario))


def callback(x):
    local, desastre, data, horario = descripto(x.data)
    mostrarmsg(local, desastre, data, horario)


def main():
    local = ""
    horario = ""
    data = ""
    desastre = ""
    flag = ""

    while(True):
        print("Bem vindo a central de avisos, para registrar em um polo digite 'r'")
        flag = raw_input()
        if(flag == 'r'):
            local = raw_input("digite o local onde deseja se registrar\n")
            flag = raw_input("para confirmar o registro em %s digite 'r'\n" % (local))
            if(flag == 'r'):
                rospy.init_node("SD_sub", anonymous=True)
                rospy.Subscriber(local, String, callback)
                print("registro realizado")
                rospy.spin()
            else:
                print("registro cancelado")


if __name__ == '__main__':
    main()
