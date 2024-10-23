import numpy as np
from scipy.spatial.transform import Rotation as R

class RigidBody:
    def __init__(self, x: float, y: float, z: float, orientation=None, is_quaternion=False, label: str = None):
        """Initialize a RigidBody with position (x, y, z) and orientation.
        
        :param x: X coordinate of the body.
        :param y: Y coordinate of the body.
        :param z: Z coordinate of the body.
        :param orientation: Orientation as either a quaternion or Euler angles in radians.
                            If None, default orientation is used (identity rotation).
        :param is_quaternion: If True, 'orientation' is treated as a quaternion, otherwise Euler angles (radians).
        """
        if isinstance(x, (float, int)) and isinstance(y, (float, int)) and isinstance(z, (float, int)):
            self.position = np.array([x, y, z])
        else:
            raise TypeError("Invalid input type for position arguments.")

        if orientation is not None and isinstance(orientation, (list, np.ndarray)):
            for item in orientation:
                if not isinstance(item, (float, int)):
                    raise TypeError("Invalid input type for quaternion arguments")
            if is_quaternion:
                # Assuming orientation is a quaternion (x, y, z, w)
                self.rotation = R.from_quat(orientation)
            else:
                # Assuming orientation is Euler angles in radians (x, y, z)
                self.rotation = R.from_euler('xyz', orientation, degrees=False)
        else:
            # Default identity rotation
            self.rotation = R.identity()
        
        self.label = label
    
    def as_quaternion(self):
        """Return the orientation as a quaternion (x, y, z, w)."""
        return self.rotation.as_quat()

    def as_euler(self, degrees=False):
        """Return the orientation as Euler angles (x, y, z) in degrees.

        :param degrees: Bool variable to choose if the return should be in degrees.
        """
        return self.rotation.as_euler('xyz', degrees=degrees)

    def get_transformation_matrix(self):
        """Return the 4x4 transformation matrix that includes both the rotation and the translation.

        The matrix is in the form:
        
        | R(3x3)  T(3x1)  |
        |  0 0 0    1     |
        """
        # Get the 3x3 rotation matrix
        rotation_matrix = self.rotation.as_matrix()
        
        # Create the 4x4 transformation matrix
        transformation_matrix = np.eye(4)  # Start with an identity matrix
        transformation_matrix[:3, :3] = rotation_matrix  # Set the top-left 3x3 as the rotation matrix
        transformation_matrix[:3, 3] = self.position     # Set the translation part
        
        return transformation_matrix

    def get_inverse_transformation_matrix(self):
        """Return the inverse of the 4x4 transformation matrix. The inverse is calculated as following.
        
        | R^T(3x3)    -R^T * T(3x1)  |
        |   0  0  0         1        |
        
        Where R^T is the transpose (inverse) of the rotation matrix, and T is the translation vector.
        """
        # Get the 3x3 rotation matrix and its transpose (inverse)
        rotation_matrix_inv = self.rotation.inv().as_matrix()
        
        # Get the translation vector
        translation_vector = self.position
        
        # Compute the inverse translation
        inverse_translation = -np.dot(rotation_matrix_inv, translation_vector)
        
        # Create the 4x4 inverse transformation matrix
        inverse_transformation_matrix = np.eye(4)
        inverse_transformation_matrix[:3, :3] = rotation_matrix_inv  # Set the top-left 3x3 as the inverted rotation matrix
        inverse_transformation_matrix[:3, 3] = inverse_translation   # Set the translation part
        
        return inverse_transformation_matrix

    def __mul__(self, other):
        """Multiply two RigidBody transformations.

        This represents the composition of transformations: first apply `self`, then `other`.
        
        :param other: Another RigidBody to multiply with.
        :return: A new RigidBody that represents the combined transformation.
        """
        if not isinstance(other, RigidBody):
            raise TypeError("Can only multiply with another RigidBody.")
        
        # Combine rotations
        combined_rotation = self.rotation * other.rotation
        
        # Transform the second body's position by the first body's rotation
        transformed_position = self.rotation.apply(other.position)
        
        # Combine positions (translation)
        combined_position = self.position + transformed_position
        
        # Return a new RigidBody with the combined transformation
        return RigidBody(combined_position[0], combined_position[1], combined_position[2], combined_rotation.as_quat(), is_quaternion=True)

    def __repr__(self):
        """String representation of the RigidBody."""
        label_str = self.label if self.label else ""
        position_str = f"Position: {self.position}"
        orientation_str = f"Orientation (quaternion): {self.as_quaternion()}"
        return f"RigidBody({label_str}, {position_str}, {orientation_str})"
    
    def update_position(self, x: float, y: float, z: float):
        """Update the position of the rigid body."""
        if isinstance(x, (float, int)) and isinstance(y, (float, int)) and isinstance(z, (float, int)):
            self.position = np.array([x, y, z])
        else:
            raise TypeError("Invalid input type for quaternion arguments")
    
    def update_orientation(self, orientation, is_quaternion=False):
        """Update the orientation of the rigid body."""
        for item in orientation:
            if not isinstance(item, (float, int)):
                raise TypeError("Invalid input type for quaternion arguments")
        if is_quaternion:
            self.rotation = R.from_quat(orientation)
        else:
            self.rotation = R.from_euler('xyz', orientation, degrees=False)
