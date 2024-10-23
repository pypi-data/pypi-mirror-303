import sys

__version__ = '0.0.1'
__all__ = ["RigidBody", "Marker"]

if sys.version_info.major < 3:
    raise Exception("PyRigidBody requires at least python 3.X to run.")

from .Marker import Marker
from .RigidBody import RigidBody