#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# for your packages to be recognized by python
d = generate_distutils_setup(
 packages=['atrv_moveit_planning_scene_ros'],
 package_dir={'atrv_moveit_planning_scene_ros': 'ros/src/atrv_moveit_planning_scene_ros'}
)

setup(**d)