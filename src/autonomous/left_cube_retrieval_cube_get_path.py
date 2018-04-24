import math
import os
import pathfinder as pf
from constants import X_ROBOT_LENGTH, Y_ROBOT_WIDTH, Y_WALL_TO_EXCHANGE_FAR, \
    X_WALL_TO_SWITCH_NEAR, Y_WALL_TO_SWITCH_NEAR
from utilities.functions import GeneratePath


class settings():
    order = pf.FIT_HERMITE_QUINTIC
    samples = 1000000
    period = 0.01
    maxVelocity = 7.0
    maxAcceleration = 10
    maxJerk = 30


# The waypoints are entered as X, Y, and Theta. Theta is measured clockwise from the X-axis and
# is in units of radians. It is important to generate the paths in a consistent manner to those
# used by the controller. For example, use either metric or imperial units.  Also, use a
# consistent frame of reference. This means that +X is forward, -X is backward, +Y is right, and
# -Y is left, +headings are going from +X towards +Y, and -headings are going from +X to -Y.
waypoints = [
    pf.Waypoint(0, 0, 0),
    pf.Waypoint(50 / 12, 0, 0),
]

GeneratePath(os.path.dirname(__file__), "left_cube_retrieval_cube_get", waypoints, settings, False, True, -45.0)
