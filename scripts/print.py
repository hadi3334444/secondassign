#! /usr/bin/env python
import rospy
import assignment_2_2022.msg
from std_srvs.srv import Empty,EmptyResponse
goal =0
cancel = 0

#function to count if canceled and if reached the target
def callback_subscriber(data):
    if data.status.status == 2:
        global cancel
        cancel += 1
    elif data.status.status == 3:
        global goal
        goal += 1

#call and print calculated canceled and reached targets
def callback(req):
    global goal,cancel
    print(f"canceled goals: {cancel} \neached goals: {goal}")
    return EmptyResponse()

if __name__ == "__main__":
    rospy.logwarn("counting started")
    #initializing the node
    rospy.init_node("print")
    rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, callback_subscriber)
    rospy.Service("reached_canceled_disp", Empty, callback)
    rospy.spin()
