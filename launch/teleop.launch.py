# teleop_control.launch.py
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'articubot_one'  # Change to your package name

    # Get the twist_mux params
    twist_mux_params = os.path.join(get_package_share_directory(package_name),'config','twist_mux.yaml')

    # Create twist_mux node
    twist_mux = Node(
        package="twist_mux",
        executable="twist_mux",
        name="twist_mux",
        parameters=[twist_mux_params],
        remappings=[('/cmd_vel_out','/diff_cont/cmd_vel_unstamped')]
    )

    # Create teleop node
    teleop_node = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard',
        output='screen',
        prefix='xterm -e',  # This opens the teleop in a separate terminal
        remappings=[('/cmd_vel', '/cmd_vel_keyboard')]
    )

    return LaunchDescription([
        twist_mux,
        teleop_node
    ])