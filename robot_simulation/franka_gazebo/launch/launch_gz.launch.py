from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
import os

def generate_launch_description():
    pkg_desc = get_package_share_directory('franka_description')
    xacro_file = os.path.join(pkg_desc, 'robots', 'fp3', 'fp3.urdf.xacro')

    robot_description = Command([
        'xacro ', xacro_file, ' gazebo:=true'
    ])

    return LaunchDescription([
        # Lancer Gazebo vide
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # Robot state publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),

        # Spawn dans Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-topic', 'robot_description',
                '-entity', 'fp3'
            ],
            output='screen'
        )
    ])
