# gazebo_teleop.launch.py
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Create teleop node that publishes directly to the topic expected by the simulator
    teleop_node = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard',
        output='screen',
        prefix='xterm -e',  # This opens the teleop in a separate terminal
        remappings=[('/cmd_vel', '/diff_cont/cmd_vel_unstamped')]  # Direct remapping to the topic needed by Gazebo
    )

    return LaunchDescription([
        teleop_node
    ])
