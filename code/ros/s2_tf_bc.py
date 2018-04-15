#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')

import rospy
import tf
import math

theta_2 = 45
l_2 = 10

def grad_to_deg(val):
    return (val * math.pi)/180

if __name__ == '__main__':
    rospy.init_node('s2_tf_bc')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        x_2 = l_2 * math.cos(grad_to_deg(theta_2))
        y_2 = l_2 * math.sin(grad_to_deg(theta_2))
        br.sendTransform((x_2, y_2, 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "s2",
                         "s1")
        rate.sleep()
