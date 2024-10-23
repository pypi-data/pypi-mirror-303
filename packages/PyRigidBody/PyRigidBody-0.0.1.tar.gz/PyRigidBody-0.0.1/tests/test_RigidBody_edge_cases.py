import os
import sys
import pytest
import numpy as np
from scipy.spatial.transform import Rotation as R

WORKSPACE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(WORKSPACE_PATH)

from src.RigidBody import RigidBody

def test_invalid_quaternion_length():
    # Quaternion should have 4 elements, test with invalid lengths
    with pytest.raises(ValueError):
        RigidBody(0.0, 0.0, 0.0, orientation=[1, 0, 0], is_quaternion=True)  # Only 3 elements
    with pytest.raises(ValueError):
        RigidBody(0.0, 0.0, 0.0, orientation=[1, 0, 0, 0, 1], is_quaternion=True)  # 5 elements

def test_invalid_euler_angles_length():
    # Euler angles should have 3 elements
    with pytest.raises(ValueError):
        RigidBody(0.0, 0.0, 0.0, orientation=[np.pi, 0])  # Only 2 elements
    with pytest.raises(ValueError):
        RigidBody(0.0, 0.0, 0.0, orientation=[np.pi, 0, 0, 1])  # 4 elements

def test_non_numeric_position():
    # Position should be numeric (float or int)
    with pytest.raises(TypeError):
        RigidBody("a", 0.0, 0.0)  # Non-numeric X
    with pytest.raises(TypeError):
        RigidBody(0.0, "b", 0.0)  # Non-numeric Y
    with pytest.raises(TypeError):
        RigidBody(0.0, 0.0, "c")  # Non-numeric Z

def test_non_numeric_orientation():
    # Orientation should be numeric (either quaternion or Euler angles)
    with pytest.raises(TypeError):
        RigidBody(0.0, 0.0, 0.0, orientation=["a", 0, 0])  # Non-numeric Euler angle
    with pytest.raises(TypeError):
        RigidBody(0.0, 0.0, 0.0, orientation=["a", 0, 0, 1], is_quaternion=True)  # Non-numeric quaternion element

def test_multiplication_with_non_rigidbody():
    body = RigidBody(1.0, 2.0, 3.0, orientation=[0, 0, np.pi/2])
    
    with pytest.raises(TypeError):
        body * "not_a_rigidbody"  # Trying to multiply with a string

def test_update_position_invalid_values():
    body = RigidBody(0.0, 0.0, 0.0)
    
    with pytest.raises(TypeError):
        body.update_position("x", 1.0, 1.0)  # Non-numeric X
    with pytest.raises(TypeError):
        body.update_position(1.0, "y", 1.0)  # Non-numeric Y
    with pytest.raises(TypeError):
        body.update_position(1.0, 1.0, "z")  # Non-numeric Z

def test_update_orientation_invalid_values():
    body = RigidBody(0.0, 0.0, 0.0)
    
    with pytest.raises(ValueError):
        body.update_orientation([0.0, 0.0], is_quaternion=False)  # Euler angles with only 2 elements
    with pytest.raises(ValueError):
        body.update_orientation([0.0, 0.0, 0.0, 0.0, 1.0], is_quaternion=True)  # Quaternion with 5 elements
    
    with pytest.raises(TypeError):
        body.update_orientation([0.0, "b", 0.0], is_quaternion=False)  # Non-numeric Euler angle
    with pytest.raises(TypeError):
        body.update_orientation([0.0, 0.0, 0.0, "w"], is_quaternion=True)  # Non-numeric quaternion element

