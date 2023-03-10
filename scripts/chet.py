#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('my_topic', String, queue_size=10)
pub2 = rospy.Publisher('overflow_topic', String, queue_size=10)
rate = rospy.Rate(10)

def start_talker():
    msg = String()
    alr = String()
    k=0
    while not rospy.is_shutdown():
        
        hello_str = str(k)
        rospy.loginfo(hello_str)
        k=k+2
        if k>100:
             k=0
             alr.data = hello_str
             pub2.publish(alr)
             
        msg.data = hello_str 
        pub.publish(msg)

        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
