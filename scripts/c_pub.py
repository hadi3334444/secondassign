#! /usr/bin/env python
import rospy
import math
import time
import os
import assignment_2_2022.msg
from geometry_msgs.msg import Point, Pose, Twist
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from secondassign.msg import custom
from tf import transformations
from std_srvs.srv import *
import actionlib
import actionlib_msgs
# function to get target position input from user and send to action server
def target_client():
    _x = input("enter x position:")
    _y = input("enter y position:")
    X = int(_x)
    Y = int(_y)
    print(f'entered position ({X},{Y})')
    # Create the SimpleActionClient, passing the type of the action
    global cl
    cl = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    print("\nWating for connection to the action server")
    cl.wait_for_server()
    # Create a goal and send to the action server
    goal = PoseStamped()
    goal.pose.position.x = X
    goal.pose.position.y = Y
    goal = assignment_2_2022.msg.PlanningGoal(goal)
    rospy.sleep(1)
    cl.send_goal(goal)
    print("\nGoal sent to the sever")
    rospy.sleep(1)
    #back to main function main menu
    main()

#function to send cancel request to action server
def cancel_target():
    cl.cancel_goal()
    print(f'target canceled')
    #back to main function main menu
    main()

#function to publish the position of robot into the custom message 
def subs(d):
    p = rospy.Publisher('chatter', custom, queue_size=50)
    m=custom()
    m.x = d.pose.pose.position.x
    m.y = d.pose.pose.position.y
    m.vel_x = d.twist.twist.linear.x
    m.vel_y = d.twist.twist.linear.y
    print(m)
    p.publish(m)
	
def pubxy(): 
    rospy.Subscriber("/odom", Odometry, subs)
    #back to main function main menu
    main()

#function to show the menu
def main():
    print("Choose from 1 - 4:")
    print("1: Enter the target position.")
    print("2: Cancel the target.")
    print("3: Publish the x and y positions.")
    print("4: Close!")
    choice = input()
    if(choice=="1"):
        target_client()
    elif(choice=="2"):
        cancel_target() 
    elif(choice=="3"):
        pubxy() 
    elif(choice=="4"):
        exit() 
    else:
        print("only 1 - 4\n")
        rospy.sleep(1)
        main()

if __name__ == '__main__':
    try:
        # Initialize a rospy node so that it can publish and subscribe over ROS.
        rospy.init_node('control_pub')        
        main()
    except rospy.ROSInterruptException:
    	print("program interrupted before completion", file=sys.stderr)

