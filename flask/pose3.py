from pyniryo import *
from os import chdir


robot = NiryoRobot("169.254.200.200")
#NiryoRobot.release_with_tool()

robot.calibrate_auto()


#j1 -3.053 +3.053
#j2 -1.91 +0.64
#j3 -1.39 +1.57
#j4 -3.049 +3.053
#j5 -1.744 +1.919
#j6 -2.529 +2.529


#x -0.455 +0.455 / Avant-Arrière
#y -0.455 +0.455 / Gauche-Droite
#z +0.135  +0.640 / Haut-Bas

robot.joints = [0.735, -0.360, -0.593, 0.921, 1.126, -0.143]
robot.move_joints([-1.191, -0.536, -0.471, -1.305, 1.560, -0.163])
robot.move_joints([-0.037, -1.137, 0.196, -0.053, 0.922, -0.256])
robot.move_joints([-0.065, -0.514, -1.086, -0.023, 1.009, -0.225])




robot.update_tool()

