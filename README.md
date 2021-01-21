# ROS2 Quality of Service Converter
By modifying qos_converter/qos_converter.py accordingly to the topic which QoS needs to be changed and to the QoS needed, this ROS2 Package will deploy a node called "/qos_converter" which will listen to the original topic and will publish on a custom topic (which name can be changed) of the same type, the same message it received but using a more fitting QoS profile. Currently, the available profile are the default ones available in the "rclpy.qos" library.

# Execution
1- Run "colcon build" in the root folder.
2- Source the workspace by running "source install/setup.bash" in the root folder (in order to source automatically run 'echo "source install/setup.bash" >> ~/.bashrc').
3- Execute the ROS2 node by entering the command "ros2 run qos_converter converter".

# Checks
To check whether the node is running use the command "ros2 node list", you should see the node /qos_converter among the others listed.

In order to check if the node is correctly subscribed to the initial topic, run "ros2 topic info -v <topic_name>".

Do the same on the topic published by /qos_converter and you should see that it is among the publishers of the said topic. 
