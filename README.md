# RASOG
Robotic Arm Simulator On Gazebo

The goal of this project is to provide a ROS2 simulation of a robotic arm on Gazebo.

## Robotic Arm

We will use a Fraka robotic arm, available here : [franka_description](https://github.com/frankarobotics/franka_description)

## How to use :

- Generate the URDF file :
```bash
./scripts/create_urdf.sh <robot_id> 
```

With robot_id : { fp3, fr3, fr3v2, fr3v2.1 } 

- To visualize the robotic arm using RViz2 :

```bash
./scripts/visualize_franka.sh arm_id:=<robot_id> 
```