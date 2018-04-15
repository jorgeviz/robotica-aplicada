#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')

import rospy
import tf
import math
import geometry_msgs.msg

global theta_1
theta_1 = 45
l_1 = 10

def grad_to_deg(val):
    return (val * math.pi)/180

def callback(msg):
    global theta_1
    print 'Recibi mensaje'
    theta_1 = float(msg.angular.z)
    print 'Angulo recibido : '+ str(theta_1)

if __name__ == '__main__':
    rospy.init_node('s1_tf_bc')
    br = tf.TransformBroadcaster()
    art_sub = rospy.Subscriber('articulaciones', geometry_msgs.msg.Twist, callback)
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        x_1 = l_1 * math.cos(grad_to_deg(theta_1))
        y_1 = l_1 * math.sin(grad_to_deg(theta_1))
        br.sendTransform((x_1, y_1, 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "s1",
                         "world")
        rate.sleep()
