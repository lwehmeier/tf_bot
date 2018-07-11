#!/usr/bin/env python  
import roslib
#roslib.load_manifest('learning_tf')
import rospy

import tf
import turtlesim.msg

def callback(event):
    br = tf.TransformBroadcaster()
    br.sendTransform((0.04, 0.04, 0),
                     tf.transformations.quaternion_from_euler(0, 0, 0),
                     rospy.Time(0),
                     "odom_frame",
                     "base_footprint")
    br.sendTransform((0.04, 0.04, 0	),
                     tf.transformations.quaternion_from_euler(0, 0, 0),
                     rospy.Time.now(),
                     "laser_frame",
                     "base_footprint")
if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    rospy.Timer(rospy.Duration(0.05), callback)
    rospy.spin()

