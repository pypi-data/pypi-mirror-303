import sys
import os
import math
import numpy as np
from scipy.spatial.transform import Rotation as R

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FILE_DIR)

from RigidBody import RigidBody

class Marker:
    def __init__(self, x: float, y: float, z: float, label: str = None):
        """Initialize a Marker with position (x, y, z) and an optional label.
        
        :param x: X coordinate of the marker.
        :param y: Y coordinate of the marker.
        :param z: Z coordinate of the marker.
        :param label: Optional label or identifier for the marker.
        """
        if not(math.isfinite(x)):
            raise ValueError("x must be finite")
        if not(math.isfinite(y)):
            raise ValueError("y must be finite")
        if not(math.isfinite(z)):
            raise ValueError("z must be finite")
        self.position = np.array([x, y, z])
        self.label = label
    
    def get_position(self):
        """Return the position of the marker as a numpy array (x, y, z)."""
        return self.position

    def set_position(self, x: float, y: float, z: float):
        """Set a new position for the marker."""
        self.position = np.array([x, y, z])

    def distance_to(self, other):
        """Compute the Euclidean distance between this marker and another marker.
        
        :param other: Another Marker object.
        :return: The Euclidean distance between the two markers.
        """
        if not isinstance(other, Marker):
            raise TypeError("Can only compute distance to another Marker.")
        
        return np.linalg.norm(self.position - other.position)

    def move_by(self, dx: float, dy: float, dz: float):
        """Move the marker by a given amount in the x, y, and z directions."""
        self.position += np.array([dx, dy, dz])

    def apply_transformation(self, transformation_matrix: np.ndarray):
        """Apply a 4x4 transformation matrix to the marker's position.
        
        :param transformation_matrix: A 4x4 transformation matrix that includes rotation and translation.
        """
        if transformation_matrix.shape != (4, 4):
            raise ValueError("Transformation matrix must be a 4x4 matrix.")
        
        # Convert the position to homogeneous coordinates (x, y, z, 1)
        homogeneous_position = np.append(self.position, 1.0)
        
        # Apply the transformation matrix
        transformed_position = transformation_matrix @ homogeneous_position
        
        # Update the position (ignoring the homogeneous coordinate)
        self.position = transformed_position[:3]

    def __mul__(self, other):
        """Multiply the Marker by a RigidBody's transformation matrix.
        
        :param other: A RigidBody object.
        :return: A new Marker object with the transformed position.
        """
        if isinstance(other, RigidBody):
            transformation_matrix = other.get_transformation_matrix()
            new_marker = Marker(*self.position, self.label)
            new_marker.apply_transformation(transformation_matrix)
            return new_marker
        else:
            raise TypeError("Can only multiply with a RigidBody.")

    def __repr__(self):
        """String representation of the Marker."""
        pos_str = f"Position: {self.position}"
        label_str = f"Label: {self.label}" if self.label else "No Label"
        return f"Marker({label_str}, {pos_str})"
