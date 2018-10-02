import rospy

from std_msgs.msg import String

def callback(x):
    print(x.data);



def main():
    rospy.init_node("China_sub", anonymous=True)
    rospy.Subscriber("China", String, callback)
    rospy.spin()


if __name__ == '__main__':
    main()
