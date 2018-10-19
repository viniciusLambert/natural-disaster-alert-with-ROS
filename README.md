# natural-disaster-alert-with-ROS
A ROS program and interface to alert people that live in natural disasters risk areas


### System settings
Python 2.7
ubuntu 16.04 (Ros kinect)
ubuntu 18.04 (Ros Melodic)

### How to run
## Runing Local
In distinct terminals

1°
```
roscore
```
2° On the project folder
```
python subscriber.py
```
or
```
python publisher.py

```
## Runing in multiple machines

M1 is the master machine
M2 is the secundary machines

M1

first of all, start the master in one terminal
```
ssh M1
roscore
```
So in another terminal
```
ssh M1
export ROS_MASTER_URI=http://m1:11311
python publisher.py
```
M2

```
ssh M2
export ROS_MASTER_URI=http://m1:11311
python subscriber.py
```
