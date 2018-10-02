import rospy

from std_msgs.msg import String



def main():
    pub = rospy.Publisher('China', String, queue_size=1)
    rospy.init_node("China_pub", anonymous=True)

    msg = "terremoto in china at 2:30"
    while True:
        pub.publish(msg)



if __name__ == '__main__':
    main()
