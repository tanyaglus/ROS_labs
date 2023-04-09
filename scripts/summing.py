#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Int8MultiArray
rospy.init_node('summing')

def callback(msg):
  mass = msg.data
  rospy.loginfo('Summing: %s', mass)
  sumel = sum(mass)
  sum_msg = Int8()
  sum_msg.data = sumel
  rospy.loginfo('Summing sends: %s', sum_msg.data)
  pub.publish(sum_msg)
  
pub = rospy.Publisher('sumreq', Int8, queue_size=10)
rospy.Subscriber('polsum', Int8MultiArray, callback, queue_size=10)
rospy.spin()
