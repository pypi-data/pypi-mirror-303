from . import jocv
from pathlib import Path
import numpy as np

Point3D = jocv.Point3D
Camera = jocv.Camera
Image = jocv.Image

class Dict(dict):
    def __str__(self):
        smallest, biggest = min(self.keys()), max(self.keys())
        return str({smallest:self[smallest], "...": f"{len(self.keys())} other points", biggest:self[biggest]})
    def __repr__(self) -> str:
        return self.__str__()
    
def read_images_bin(path: str | Path) -> dict:
    """
    Read images from a binary file.

    Args:
        path (str | Path): The path to the binary file.

    Returns:
        dict: A dictionary containing the images read from the file.
    """
    return jocv.read_images_bin(str(path))

def read_points3D_bin(path: str | Path) -> Dict:
    """
    Read 3D points from a binary file.

    Args:
        path (str or Path): The path to the binary file.

    Returns:
        dict: A dictionary containing the 3D points.

    """
    return jocv.read_points3D_bin(str(path))

def read_cameras_bin(path: str | Path) -> dict:
    """
    Reads camera data from a binary file.

    Args:
        path (str or Path): The path to the binary file.

    Returns:
        dict: A dictionary containing the camera data.

    """
    return jocv.read_cameras_bin(str(path))

def read_reconstruction_bin(path: str | Path) -> dict:
    """
    Reads reconstruction data from a binary file.

    Args:
        path (str or Path): The path to the binary file.

    Returns:
        dict: A tuple (cams, ims, points3D) containing the reconstruction data.

    """
    cams, ims, points3D = jocv.read_reconstruction_bin(str(path)) #wrap points3D in Dict to prevent printing all points
    return cams, ims, Dict(points3D)

def compute_overlaps(points3D: dict[int, dict[int, Point3D]]) -> dict:
    """
    Compute the overlaps between 3D points.

    Args:
        points3D (dict): A dictionary containing 3D points.

    Returns:
        dict: A dictionary containing the computed overlaps.

    """
    return jocv.compute_overlaps(points3D)


def compute_overlap_percentages(points3D: dict[int, dict[int, Point3D]]) -> dict:
    """
    Compute the overlap percentages between 3D points.

    Args:
        points3D (dict): A dictionary containing 3D points.

    Returns:
        dict: A dictionary containing the computed overlaps.

    """
    return jocv.compute_overlap_percentages(points3D)


def compute_relative_pose(image_A: Image, image_B: Image) -> np.ndarray:
    """
    Compute the relative pose A->B between two images A and B.

    Args:
        image_A (Image): The first image (from).
        image_B (Image): The second image (to).

    Returns:
        tuple: A tuple containing the rotation and translation matrices.

    """
    R, t = image_B.relative_pose_from(image_A)
    return np.array(R), np.array(t)

def K(camera: Camera) -> np.ndarray:
    """
    Get the camera matrix K.

    Args:
        camera (Camera): The camera.

    Returns:
        np.ndarray: The camera matrix K.

    """
    return np.array(camera.K())

def get_tracked_points(image: Image) -> np.ndarray:
    """
    Get the tracked points of an image.

    Args:
        image (Image): The image.

    Returns:
        np.ndarray: The tracked points.

    """
    return np.array(image.get_tracked_points2D())