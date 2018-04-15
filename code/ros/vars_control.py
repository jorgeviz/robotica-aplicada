#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg


if __name__ == '__main__':
    rospy.init_node('vars_control')
    art_pub = rospy.Publisher('articulaciones', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        # Leer variables del robot
        q1 = raw_input('Escribe Theta:')
        cmd = geometry_msgs.msg.Twist()
        cmd.angular.z = float(q1)
        art_pub.publish(cmd)
        print 'Published '+str(float(q1))
        rate.sleep()

