#!/usr/bin/env python
import math
import sys
import os
import time
import argparse
import pybullet as p
from onshape_to_robot.simulation import Simulation

robotPath = 'urdf/phantomx.urdf'
sim = Simulation(robotPath, gui=True, panels=True, useUrdfInertia=False)
pos, rpy = sim.getRobotPose()
sim.setRobotPose([0, 0, 0.5], [0,0,0,1])

controls = {}
for name in sim.getJoints():
    if 'c1' in name or 'thigh' in name or 'tibia' in name:
        controls[name] = p.addUserDebugParameter(name, -math.pi, math.pi, 0)

while True:
    targets = {}
    for name in controls.keys():
        targets[name] = p.readUserDebugParameter(controls[name])
    sim.setJoints(targets)

    sim.tick()

