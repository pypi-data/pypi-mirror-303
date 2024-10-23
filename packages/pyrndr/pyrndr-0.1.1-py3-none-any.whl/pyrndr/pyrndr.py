"""
This module provides functionality to render 3D meshes or scenes into 2D images
using different rendering modes, including color rendering, ID rendering,
normal-based rendering, and coordinate rendering.

The rendering supports optional shading using ambient, diffuse, and specular components,
as well as the calculation of depth buffers. It leverages the trimesh library for ray-mesh
intersection and rendering tasks.
"""

from enum import Enum

import numpy as np
import trimesh
from scipy.sparse import csr_array, find

# Constant light direction used for shading calculations
_LIGHT_DIRECTION = np.array([0, 0, -1.0])

# Constant transforming the pose between difference coordinate system.
OPENGL2OPENCV = np.eye(4)
OPENGL2OPENCV[[1, 2], [1, 2]] = -1


class RenderMode(Enum):
    """Enumeration for different rendering modes."""

    COLOR = 1
    """Renders the mesh with its assigned colors."""

    ID = 2
    """Renders the mesh with unique ID values for each mesh."""

    NORMAL = 3
    """Renders the mesh using its face normals."""

    COORD = 4
    """Renders the intersection coordinates of rays and mesh surfaces."""


class CameraPoseMode(Enum):
    """
    Enumeration for different camera pose modes used in rendering systems.

    OpenGL and OpenCV share the same right-handed coordinate system, but they differ in how their initial camera
    poses are defined:

    - **OpenGL:** The camera starts with the y-axis pointing up, and the z-axis
      going backward from the screen (negative z-direction).

    - **OpenCV:** The camera starts with the y-axis pointing down, and the z-axis
      going forward from the screen (positive z-direction).
    """

    OpenGL = 1
    """Camera pose in the OpenGL-like coordinate system, with the x-axis to the right,
    y-axis upward, and z-axis pointing backward from the screen."""

    OpenCV = 2
    """Camera pose in the OpenCV-like coordinate system, with the x-axis to the right,
    y-axis downward, and z-axis pointing forward from the screen."""


def render(
    mesh: trimesh.Trimesh | trimesh.Scene | list[trimesh.Trimesh],
    image_size: tuple[int, int],
    intrinsic_matrix: np.ndarray,
    camera_pose: np.ndarray,
    background_value=0,
    ambient_weight=0.6,
    diffuse_weight=0.3,
    specular_weight=0.3,
    shininess=10,
    enable_shading=True,
    render_mode=RenderMode.COLOR,
    camera_pose_mode=CameraPoseMode.OpenGL,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Renders a 3D mesh or scene into a 2D image with optional shading and depth buffer.

    Parameters:
    -----------
    mesh : trimesh.Trimesh | trimesh.Scene | list[trimesh.Trimesh]
        The mesh or scene to be rendered. Can be a single mesh, a scene, or a list of meshes.
    image_size : tuple[int, int]
        The size of the output image as (width, height).
    intrinsic_matrix : np.ndarray
        The 3x3 camera intrinsic matrix for projecting 3D points to 2D.
    camera_pose : np.ndarray
        The 4x4 camera pose matrix defining the position and orientation of the camera in world coordinates.
    background_value : int | float, optional
        The background value for the image. Default is 0.
    ambient_weight : float, optional
        The ambient light weight for shading. Default is 0.6.
    diffuse_weight : float, optional
        The diffuse light weight for shading. Default is 0.3.
    specular_weight : float, optional
        The specular light weight for shading. Default is 0.3.
    shininess : int, optional
        The shininess factor for specular highlights. Default is 10.
    enable_shading : bool, optional
        Whether to enable shading in the rendering. Default is True.
    render_mode : RenderMode, optional
        The rendering mode. Options are:
        - RenderMode.COLOR: Render with colors.
        - RenderMode.ID: Render with mesh IDs.
        - RenderMode.NORMAL: Render with face normals.
        - RenderMode.COORD: Render with intersection coordinates.
        Default is RenderMode.COLOR.
    camera_pose_mode : CameraPoseMode, optional
        The mode of the camera pose that determines the coordinate system orientation.
        This parameter affects how the `camera_pose` is interpreted:

        - **CameraPoseMode.OpenGL:** Uses an OpenGL-like camera pose where the y-axis
          points upward, and the z-axis points backward from the screen.
        - **CameraPoseMode.OpenCV:** Uses an OpenCV-like camera pose where the y-axis
          points downward, and the z-axis points forward from the screen.
        Default is CameraPoseMode.OpenGL.

    Returns:
    --------
    image : np.ndarray
        The rendered 2D image as a numpy array.
    depth_buffer : np.ndarray
        The depth buffer as a numpy array with the same size as the image.

    Raises:
    -------
    NotImplementedError
        If the specified render_mode is not supported.

    Example:
    --------
    >>> mesh = trimesh.load('path_to_mesh.obj')
    >>> image_size = (640, 480)
    >>> intrinsic_matrix = np.eye(3)
    >>> camera_pose = np.eye(4)
    >>> image, depth = render(
    >>>     mesh, image_size, intrinsic_matrix, camera_pose, render_mode=RenderMode.COLOR
    >>> )
    """

    if camera_pose_mode == CameraPoseMode.OpenGL:
        camera_pose = camera_pose @ OPENGL2OPENCV

    if render_mode == RenderMode.COLOR:
        image = np.full([*image_size[::-1], 4], background_value, dtype=np.uint8)
    elif render_mode == RenderMode.ID:
        image = np.zeros(image_size[::-1], dtype=np.int64)
    elif render_mode in (RenderMode.NORMAL, RenderMode.COORD):
        image = np.zeros([*image_size[::-1], 3])
    else:
        raise NotImplementedError("Unsupported rendering mode")

    depth_buffer = np.zeros(image_size[::-1])

    if isinstance(mesh, trimesh.Scene):
        mesh_list = list(mesh.geometry.values())
    elif isinstance(mesh, (tuple, list)):
        mesh_list = mesh
    else:
        mesh_list = [mesh]

    disparity_map = None

    for mesh_index, current_mesh in enumerate(mesh_list):
        projected_vertices = (current_mesh.vertices - camera_pose[:3, 3]) @ camera_pose[:3, :3]
        projected_vertices = (projected_vertices[:, :2] / projected_vertices[:, 2:3]) * intrinsic_matrix[
            [0, 1], [0, 1]
        ] + intrinsic_matrix[[0, 1], [2, 2]]

        x_max, y_max = np.ceil(projected_vertices.max(0)).astype(int).clip(min=0, max=image_size)
        x_min, y_min = np.floor(projected_vertices.min(0)).astype(int).clip(min=0, max=image_size)

        ray_uv_coordinates = np.mgrid[y_min:y_max, x_min:x_max].reshape(2, -1)[[1, 0], :].T
        perturbed_ray_uvs = (
            ray_uv_coordinates.astype(np.float64) + (np.random.rand(*ray_uv_coordinates.shape) - 0.5) * 0.001
        )
        ray_directions = (perturbed_ray_uvs - intrinsic_matrix[[0, 1], [2, 2]]) / intrinsic_matrix[[0, 1], [0, 1]]
        ray_directions = np.concatenate([ray_directions, np.ones_like(ray_directions[:, :1])], axis=-1)

        world_ray_directions = ray_directions @ camera_pose[:3, :3].T
        ray_origin = camera_pose[:3, 3]

        intersection_points, ray_indices, face_indices = current_mesh.ray.intersects_location(
            np.repeat(ray_origin[None], len(world_ray_directions), axis=0), world_ray_directions, multiple_hits=False
        )

        if len(intersection_points) == 0:
            continue

        if render_mode == RenderMode.COLOR:
            if hasattr(current_mesh.visual, "uv"):
                barycentric_weights = trimesh.triangles.points_to_barycentric(
                    current_mesh.triangles[face_indices], intersection_points
                )
                uv_coords = current_mesh.visual.uv[current_mesh.faces[face_indices].reshape(-1)].reshape(-1, 3, 2)
                interpolated_uvs = (uv_coords * barycentric_weights[..., None]).sum(1)
                colors = trimesh.visual.color.uv_to_interpolated_color(
                    interpolated_uvs, current_mesh.visual.material.image
                )
            else:
                colors = current_mesh.visual.face_colors[face_indices]

            if enable_shading:
                face_normals = current_mesh.face_normals[face_indices]
                light_direction = _LIGHT_DIRECTION @ camera_pose[:3, :3].T

                diffuse_intensity = np.clip(face_normals @ light_direction, 0, 1)
                specular_intensity = np.power(diffuse_intensity, shininess)
                shading = ambient_weight + diffuse_weight * diffuse_intensity + specular_weight * specular_intensity
                colors[:, :3] = (colors[:, :3] * shading[:, None]).clip(0, 255)

        elif render_mode == RenderMode.ID:
            colors = mesh_index + 1
        elif render_mode == RenderMode.NORMAL:
            colors = current_mesh.face_normals[face_indices]
        elif render_mode == RenderMode.COORD:
            colors = intersection_points

        u, v = ray_uv_coordinates[ray_indices].T

        if disparity_map is None:
            depth_values = ((intersection_points - camera_pose[:3, 3]) @ camera_pose[:3, :3])[:, 2]
            disparity_map = csr_array((1 / depth_values, (u, v)), image_size)
            depth_buffer[v, u] = depth_values
            image[v, u] = colors
        else:
            new_depth_values = ((intersection_points - camera_pose[:3, 3]) @ camera_pose[:3, :3])[:, 2]
            new_disparity_map = csr_array((1 / new_depth_values, (u, v)), image_size)
            i, j, _ = find(disparity_map < new_disparity_map)

            if len(i) == 0:
                continue

            disparity_map[i, j] = new_disparity_map[i, j]
            depth_buffer[j, i] = csr_array((new_depth_values, (u, v)), image_size)[i, j]

            if render_mode in (RenderMode.COLOR, RenderMode.NORMAL, RenderMode.COORD):
                for channel_index, channel_color in enumerate(colors.T):
                    image[j, i, channel_index] = csr_array((channel_color, (u, v)), image_size)[i, j]
            else:
                image[j, i] = colors

    return image, depth_buffer
