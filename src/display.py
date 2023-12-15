import rospy
from nav_msgs.msg import MapMetaData

def metadata_callback(metadata_msg):
    # Hàm callback được gọi mỗi khi nhận được thông tin metadata từ topic
    rospy.loginfo("Received map metadata")
    rospy.loginfo("Map resolution: {}".format(metadata_msg.resolution))
    rospy.loginfo("Map width: {}".format(metadata_msg.width))
    rospy.loginfo("Map height: {}".format(metadata_msg.height))
    # Thực hiện xử lý thông tin metadata ở đây

def my_metadata_subscriber():
    rospy.init_node('my_metadata_subscriber')
    rospy.Subscriber("/map_metadata", MapMetaData, metadata_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        my_metadata_subscriber()
    except rospy.ROSInterruptException:
        pass
