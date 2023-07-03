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

robot.open_gripper()
robot.joints = [1.533, -0.026, -1.061, -0.026, 0.135, -0.593]
robot.close_gripper()
robot.move_joints([1.533, 0.226, -1.055, -0.026, 0.135, -0.593])
robot.move_joints([-0.949, -0.427, -0.961, -0.009, 1.315, -0.383])
robot.move_joints([-0.926, -0.531, -0.987, 0.046, 1.451, -0.348])
robot.open_gripper()


robot.update_tool()

