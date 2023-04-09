#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8MultiArray
rospy.init_node('polynomial')

def callback(msg):
  var = msg.data
  rospy.loginfo('Polynomial hears: %s', var)
  pol = [0, 0, 0] 
  
  for i in range(len(var)):
    pol[i] = var[i] ** (3 - i)
    
  pol_msg = Int8MultiArray()
  pol_msg.data = pol
  rospy.loginfo('Pol sends: %s', pol_msg.data)
  pub.publish(pol_msg)
  
pub = rospy.Publisher('polsum', Int8MultiArray, queue_size=10)
rospy.Subscriber('reqpol', Int8MultiArray, callback, queue_size=10)
rospy.spin()
