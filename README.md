# natural-disaster-alert-with-ROS
A ROS program and interface to alert people that live in natural disasters risk areas


### System settings



 Ubuntu -V | Ros -v      | Python -V
:-------:  |  :------:   | :---:
16.04      |    Kinect   |  2.7
18.04      |    Melodic  |  2.7

## How to run
### Runing Local
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

### after all install the ssh
```
sudo apt-get update
sudo apt-get install openssh-server
sudo apt-get install openssh-client
sudo ufw allow 22
```


M1 is the master machine
M2 is the secundary machines

M1 = machine 1 name   
M2 = machine 2 name

On M1, start the master in one terminal

```
roscore
```
So in another terminal
```
python publisher.py
or
python subscribe.py
```

M2

```
ssh M1@ip_M1

python publisher.py
or
python subscribe.py
```
