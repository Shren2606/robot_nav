
#!/usr/bin/env python

import rospy
from nav_msgs.msg import OccupancyGrid

def map_callback(map_msg):
    # Hàm callback được gọi mỗi khi nhận được bản đồ từ topic
    rospy.loginfo("Received map data")
    # Thực hiện xử lý với bản đồ ở đây

def my_node():
    rospy.init_node('my_map_subscriber')
    rospy.Subscriber("/map", OccupancyGrid, map_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        my_node()
    except rospy.ROSInterruptException:
        pass
