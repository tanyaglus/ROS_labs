#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("there are a %s", msg.data)

rospy.init_node('listener')
rospy.Subscriber('my_topic', String, callback, queue_size=10)
rospy.spin()
