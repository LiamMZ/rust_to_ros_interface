import socket
import json
from roslibpy import Ros, Topic

# UDP server settings
udp_server_address = ('127.0.0.1', 8069)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(udp_server_address)

# ROS settings
ros = Ros(host='localhost', port=9090)
ros.run()

# Create a ROS topic to publish received messages
topic_name = '/udp_received'
message_type = 'std_msgs/String'
udp_topic = Topic(ros, topic_name, message_type)

try:
    while True:
        try:
            data, _ = udp_socket.recvfrom(1024)
            if not data:
                continue

            received_message = json.loads(data.decode())

            # Convert the received message to ROS message format
            ros_message = {'data': received_message['content']}

            # Publish the message to the ROS topic
            udp_topic.publish(ros_message)
            print(f"Published to {topic_name}: {ros_message}")

        except json.JSONDecodeError:
            print("Received invalid JSON data")
        except Exception as e:
            print(f"An error occurred: {e}")

except KeyboardInterrupt:
    pass
finally:
    udp_socket.close()
    ros.terminate()
