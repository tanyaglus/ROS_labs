#!/usr/bin/env python3
import rospy

from std_msgs.msg import Int8
from std_msgs.msg import Int8MultiArray

rospy.init_node('request')
pub = rospy.Publisher('reqpol', Int8MultiArray, queue_size=10)
rate = rospy.Rate(1)

def callback(msg):
  rospy.loginfo('Summing res: %s', msg.data)
  rospy.Subscriber('sumreq' , Int8, callback, queue_size=10)
def Req():
  pol_msg = Int8MultiArray()
  var = [2, 4, 5]
  while not rospy.is_shutdown():
   pol_msg.data = var
   rospy.loginfo('Request sends: %s', pol_msg.data)
   pub.publish(pol_msg)
   rate.sleep()
try:
  Req()
except (rospy.ROSInterruptException, KeyboardInterrupt):
  rospy.logerr('Exception catched')
