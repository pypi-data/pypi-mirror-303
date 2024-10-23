import os
import sys
import pytest
import numpy as np

WORKSPACE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(WORKSPACE_PATH)

from src.Marker import Marker
from src.RigidBody import RigidBody

def test_marker_with_very_large_values():
    # Test initialization with very large coordinates
    large_value = 1e12
    marker = Marker(large_value, large_value, large_value)
    assert np.allclose(marker.get_position(), [large_value, large_value, large_value])

def test_marker_with_very_small_values():
    # Test initialization with very small coordinates
    small_value = 1e-12
    marker = Marker(small_value, small_value, small_value)
    assert np.allclose(marker.get_position(), [small_value, small_value, small_value])

def test_distance_with_large_values():
    marker1 = Marker(0.0, 0.0, 0.0)
    marker2 = Marker(1e12, 1e12, 1e12)
    distance = marker1.distance_to(marker2)
    expected_distance = np.sqrt(3 * (1e12)**2)
    assert pytest.approx(distance, 0.1) == expected_distance

def test_distance_with_small_values():
    marker1 = Marker(0.0, 0.0, 0.0)
    marker2 = Marker(1e-12, 1e-12, 1e-12)
    distance = marker1.distance_to(marker2)
    expected_distance = np.sqrt(3 * (1e-12)**2)
    assert pytest.approx(distance, 1e-20) == expected_distance

def test_marker_with_nan_position():
    # Initialize a marker with NaN values in position
    with pytest.raises(ValueError):
        marker = Marker(float('nan'), 0.0, 0.0)

def test_marker_with_infinite_position():
    # Initialize a marker with infinite values in position
    with pytest.raises(ValueError):
        marker = Marker(float('inf'), 0.0, 0.0)

def test_distance_to_nan_position():
    marker1 = Marker(0.0, 0.0, 0.0)
    with pytest.raises(ValueError):
        marker2 = Marker(float('nan'), 0.0, 0.0)

def test_distance_to_infinite_position():
    marker1 = Marker(0.0, 0.0, 0.0)
    with pytest.raises(ValueError):
        marker2 = Marker(float('inf'), 0.0, 0.0)
        marker1.distance_to(marker2)

def test_apply_transformation_with_large_values():
    marker = Marker(1e12, 1e12, 1e12)
    transformation_matrix = np.array([
        [1, 0, 0, 1e12],
        [0, 1, 0, -1e12],
        [0, 0, 1, 1e12],
        [0, 0, 0, 1]
    ])
    marker.apply_transformation(transformation_matrix)
    assert np.allclose(marker.get_position(), [2e12, 0.0, 2e12])

def test_apply_transformation_with_small_values():
    marker = Marker(1e-12, 1e-12, 1e-12)
    transformation_matrix = np.array([
        [1, 0, 0, 1e-12],
        [0, 1, 0, -1e-12],
        [0, 0, 1, 1e-12],
        [0, 0, 0, 1]
    ])
    marker.apply_transformation(transformation_matrix)
    assert np.allclose(marker.get_position(), [2e-12, 0.0, 2e-12], atol=1e-20)

def test_marker_move_by_large_values():
    marker = Marker(1e12, 1e12, 1e12)
    marker.move_by(1e12, -1e12, 0.0)
    assert np.allclose(marker.get_position(), [2e12, 0.0, 1e12])

def test_marker_move_by_small_values():
    marker = Marker(1e-12, 1e-12, 1e-12)
    marker.move_by(1e-12, -1e-12, 0.0)
    assert np.allclose(marker.get_position(), [2e-12, 0.0, 1e-12], atol=1e-20)

