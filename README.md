# The Robot is given a target position  

To run the code and see the output, you have to create another package in the ros_ws/src folder by using the catkin_create_pkg command in ROS. Write the following code to create the package be careful as the name of the package also should be same.

*catkin_create_pkg* *secondassign* *rospy*

Then you have to clone these codes and copy them inside the package secondassign and go back to the folder ros_ws and run the command catkin_make to make it ready to run.

Now to run the code, write the following command:

*roslaunch* *assignment_2_2022* *assignment1.launch*

To run the three nodes you open another three command prompt windows and run the following commands in respected windows:

*rosrun* *secondassign* *c_pub.py*

*rosrun* *secondassign* *print.py*

But for the third node you have to set the parameter */publish_speed* by the following command

*rosparam* *set* *publish_speed* *10*

And run the following command to start the third node:

*rosrun* *secondassign* *distance.py*


Note: The third node will show the exact distance only if you give input "3" in the menu of the first node to publish the location of the robot
Note: the second node will show you the number of reached goals and canceled goals only if you call the service which can be done by opening another command prompt window and running the command:

*rosservice* *call* */reached_canceled_disp*   



In the first node there is a menu that you can select one, which are sending the target position to the robot through the action server, and also you can cancel it and also you can publish it on the custom message file and also exit the node.
 
In the second node, if started, will count the number of reached target and canceled target and to display you need to call a service called **/reached_canceled_disp** by the command that I mentioned Then it is displayed.

The third node is to calculate the distance between the robot and the target position, both are requested from the action server and calculated. But you have to set the parameter.



Below is the flowchart that shows how the first node is running. 

![Tux, the Linux mascot](/image/flowchart.png)

To compile and run all the codes in one command then you can run the following command:

*roslaunch* *secondassign* *2ndAssign.launch*
