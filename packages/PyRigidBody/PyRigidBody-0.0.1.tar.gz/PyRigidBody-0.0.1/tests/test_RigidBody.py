import os
import sys
import pytest
import numpy as np
from scipy.spatial.transform import Rotation as R

WORKSPACE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(WORKSPACE_PATH)

from src.RigidBody import RigidBody

def test_initialization_with_euler():
    body = RigidBody(1.0, 2.0, 3.0, orientation=[np.pi/2, 0, 0])
    assert np.allclose(body.position, [1.0, 2.0, 3.0])
    assert np.allclose(body.as_euler(), [np.pi/2, 0, 0], atol=1e-6)

def test_initialization_with_quaternion():
    quaternion = R.from_euler('xyz', [np.pi/2, 0, 0], degrees=False).as_quat()
    body = RigidBody(1.0, 2.0, 3.0, orientation=quaternion, is_quaternion=True)
    assert np.allclose(body.position, [1.0, 2.0, 3.0])
    assert np.allclose(body.as_quaternion(), quaternion, atol=1e-6)

def test_default_initialization():
    body = RigidBody(0.0, 0.0, 0.0)
    assert np.allclose(body.position, [0.0, 0.0, 0.0])
    assert np.allclose(body.as_euler(), [0.0, 0.0, 0.0])

def test_transformation_matrix():
    body = RigidBody(1.0, 2.0, 3.0, orientation=[0, 0, np.pi/2])
    matrix = body.get_transformation_matrix()
    
    expected_matrix = np.array([[0, -1, 0, 1],
                                [1,  0, 0, 2],
                                [0,  0, 1, 3],
                                [0,  0, 0, 1]])
    
    assert np.allclose(matrix, expected_matrix, atol=1e-6)

def test_inverse_transformation_matrix():
    body = RigidBody(1.0, 2.0, 3.0, orientation=[0, 0, np.pi/2])
    inv_matrix = body.get_inverse_transformation_matrix()
    
    expected_inv_matrix = np.array([[ 0,  1,  0, -2],
                                    [-1,  0,  0,  1],
                                    [ 0,  0,  1, -3],
                                    [ 0,  0,  0,  1]])
    
    assert np.allclose(inv_matrix, expected_inv_matrix, atol=1e-6)

def test_multiplication():
    body1 = RigidBody(1.0, 2.0, 3.0, orientation=[np.pi/2, 0, 0])
    body2 = RigidBody(0.0, 1.0, 0.0, orientation=[0, 0, np.pi/2])
    
    combined_body = body1 * body2
    
    expected_position = [1.0, 2.0, 3.0 + 1.0]  # Applying rotation from body1 to body2's position
    expected_orientation = R.from_euler('xyz', [np.pi/2, -np.pi/2, 0.0], degrees=False).as_quat()
    
    assert np.allclose(combined_body.position, expected_position, atol=1e-6)
    assert np.allclose(combined_body.as_quaternion(), expected_orientation, atol=1e-6)

def test_update_position():
    body = RigidBody(0.0, 0.0, 0.0)
    body.update_position(5.0, 6.0, 7.0)
    assert np.allclose(body.position, [5.0, 6.0, 7.0])

def test_update_orientation():
    body = RigidBody(0.0, 0.0, 0.0)
    new_orientation = [3*np.pi/4.0, 0, 0]
    body.update_orientation(new_orientation)
    assert np.allclose(body.as_euler(), new_orientation, atol=1e-6)

