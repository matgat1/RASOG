# RASOG (Robotic Arm Simulator On Gazebo)

The goal of this project is to provide a ROS2 simulation of a robotic arm in Gazebo.

## Robotic Arm

We will simulate the [Franka Production 3](https://download.franka.de/Franka-Production-3_Datasheet.pdf) manipulator.
The corresponding robot model files can be found in this repo : [franka_description](https://github.com/frankarobotics/franka_description)

## How to use :

- Generate the URDF file :

```bash
./scripts/create_urdf.sh <robot_id> 
```

```bash
./scripts/create_urdf.sh <robot_id> 
```

With robot_id : { fp3, fr3, fr3v2, fr3v2.1 } 

- To visualize the robotic arm using RViz2 :

```bash
./scripts/visualize_franka.sh arm_id:=<robot_id> 
```