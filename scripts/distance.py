#! /usr/bin/env python
import rospy
import math
import assignment_2_2022
from std_srvs.srv import Empty,EmptyResponse
from secondassign.msg import custom
count = 0
tar_distance = 0
temp_vel = 0
avg_vel = 0

#function to get the target position and the robot positions and calculate the distance
def callback_subscriber(data):
    #position of target
    tar_x = rospy.get_param("/des_pos_x")
    tar_y = rospy.get_param("/des_pos_y")
    #position of robot
    cur_x = data.x
    cur_y = data.y
    cur_vel_x = data.vel_x
    cur_vel_y = data.vel_y
    cur_vel = math.sqrt(((cur_vel_x)**2)+((cur_vel_y)**2))
    #global variables
    global count
    global tar_distance
    global temp_vel
    global avg_vel
    if count < 5:
        temp_vel = temp_vel + cur_vel
        count += 1
    elif count == 5:
        count = 0
        temp_vel /= 5
        avg_vel = temp_vel
        temp_vel = 0
    tar_distance = math.sqrt(((tar_x - cur_x)**2) + ((tar_y - cur_y)**2))

#function to start the node and get the parameter print_interval value and display the distance 
if __name__ == "__main__":
    rospy.logwarn("finding distance started")
    #initiating the node
    rospy.init_node("distance")
    #getting the parameter publish_speed
    rate = rospy.Rate(rospy.get_param("/publish_speed"))
    rospy.Subscriber("chatter", custom, callback_subscriber)
    while not rospy.is_shutdown():
    	#displaying the calculated distance
        print(f"distance: {tar_distance : .2f}")
        print(f"average velocity: {avg_vel: .2f}")
        #sleep according to the time interval of parameter publish_speed
        rate.sleep()
