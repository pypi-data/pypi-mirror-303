import os
import sys
import pytest
import numpy as np

WORKSPACE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(WORKSPACE_PATH)

from src.Marker import Marker
from src.RigidBody import RigidBody

def test_marker_initialization():
    marker = Marker(1.0, 2.0, 3.0, label="TestMarker")
    assert np.allclose(marker.get_position(), [1.0, 2.0, 3.0])
    assert marker.label == "TestMarker"

def test_get_position():
    marker = Marker(1.0, 2.0, 3.0)
    position = marker.get_position()
    assert np.allclose(position, [1.0, 2.0, 3.0])

def test_set_position():
    marker = Marker(1.0, 2.0, 3.0)
    marker.set_position(4.0, 5.0, 6.0)
    assert np.allclose(marker.get_position(), [4.0, 5.0, 6.0])

def test_distance_to():
    marker1 = Marker(0.0, 0.0, 0.0)
    marker2 = Marker(3.0, 4.0, 0.0)
    distance = marker1.distance_to(marker2)
    assert pytest.approx(distance, 0.001) == 5.0  # 3-4-5 triangle

def test_distance_to_invalid_marker():
    marker = Marker(0.0, 0.0, 0.0)
    with pytest.raises(TypeError):
        marker.distance_to("not_a_marker")  # Invalid input

def test_move_by():
    marker = Marker(1.0, 2.0, 3.0)
    marker.move_by(1.0, -1.0, 0.5)
    assert np.allclose(marker.get_position(), [2.0, 1.0, 3.5])

def test_apply_transformation():
    marker = Marker(1.0, 2.0, 3.0)
    transformation_matrix = np.array([
        [1, 0, 0, 5],
        [0, 1, 0, -2],
        [0, 0, 1, 3],
        [0, 0, 0, 1]
    ])
    marker.apply_transformation(transformation_matrix)
    assert np.allclose(marker.get_position(), [6.0, 0.0, 6.0])

def test_apply_invalid_transformation():
    marker = Marker(1.0, 2.0, 3.0)
    invalid_matrix = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])  # Invalid shape (not 4x4)
    with pytest.raises(ValueError):
        marker.apply_transformation(invalid_matrix)

def test_marker_multiplication_invalid_type():
    marker = Marker(1.0, 2.0, 3.0)
    with pytest.raises(TypeError):
        marker * "not_a_rigidbody"  # Invalid input for multiplication

def test_repr():
    marker = Marker(1.0, 2.0, 3.0, label="TestMarker")
    repr_string = repr(marker)
    assert repr_string == "Marker(Label: TestMarker, Position: [1. 2. 3.])"

def test_repr_no_label():
    marker = Marker(1.0, 2.0, 3.0)
    repr_string = repr(marker)
    assert repr_string == "Marker(No Label, Position: [1. 2. 3.])"

