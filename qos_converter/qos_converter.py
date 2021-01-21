#!/usr/bin/python
# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data, qos_profile_system_default

from sensor_msgs.msg import Image

default_depth = 10


class QosConverter(Node):

    def __init__(self):
        super().__init__('qos_converter')
        self.subscription_ = self.create_subscription(Image,
                'camera/image_raw', self.converter_callback,
                qos_profile_sensor_data)
        self.publisher_ = self.create_publisher(Image,
                'camera/reliable_image_raw', qos_profile_system_default)

    def converter_callback(self, msg):
        self.publisher_.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    qos_converter = QosConverter()

    rclpy.spin(qos_converter)

    rclpy.shutdown()


if __name__ == '__main__':
    main()

