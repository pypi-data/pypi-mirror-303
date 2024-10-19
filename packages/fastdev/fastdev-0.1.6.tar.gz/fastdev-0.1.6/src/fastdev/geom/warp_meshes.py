# mypy: disable-error-code="valid-type"
# ruff: noqa: F821
from typing import List, Optional, Tuple, Union

import numpy as np
import torch
import trimesh
import warp as wp
from beartype import beartype
from jaxtyping import Float, Int

from fastdev.geom.warp_sdf_fns import query_sdf_on_meshes
from fastdev.xform import inverse_tf_mat, transform_points

Device = Optional[Union[str, torch.device]]  # from torch.types import Device  # make mypy happy


@beartype
class WarpMeshes:
    """A lightweight wrapper for batched warp meshes."""

    def __init__(self, warp_meshes: List[wp.Mesh], warp_meshes_first_idx: Int[torch.Tensor, "num_scenes"]):
        self._meshes = warp_meshes
        self._device_wp = warp_meshes[0].device
        self._mesh_ids_wp = wp.array([m.id for m in self._meshes], dtype=wp.uint64, device=self._device_wp)
        self._meshes_first_idx_wp = wp.from_torch(warp_meshes_first_idx.to(torch.int32), dtype=wp.int32)
        if wp.get_device(str(warp_meshes_first_idx.device)) != self._device_wp:
            raise ValueError(f"Device mismatch: {warp_meshes_first_idx.device} vs {self._device_wp}")

    @staticmethod
    def from_files(filenames: List[str], filenames_first_idx: Int[torch.Tensor, "num_scenes"], device: Device = "cpu"):
        warp_meshes = []
        device_wp = wp.get_device(str(device))
        for filename in filenames:
            mesh = trimesh.load(filename, process=False, force="mesh")
            v, f = mesh.vertices.view(np.ndarray), mesh.faces.view(np.ndarray)  # type: ignore
            warp_meshes.append(
                wp.Mesh(
                    points=wp.array(v, dtype=wp.vec3, device=device_wp),
                    indices=wp.array(np.ravel(f), dtype=int, device=device_wp),
                )
            )
        return WarpMeshes(warp_meshes=warp_meshes, warp_meshes_first_idx=filenames_first_idx.to(device))

    @staticmethod
    def from_trimesh_meshes(
        meshes: List[trimesh.Trimesh], meshes_first_idx: Int[torch.Tensor, "num_scenes"], device: Device = "cpu"
    ) -> "WarpMeshes":
        warp_meshes = []
        device_wp = wp.get_device(str(device))
        for mesh in meshes:
            v, f = mesh.vertices.view(np.ndarray), mesh.faces.view(np.ndarray)
            warp_meshes.append(
                wp.Mesh(
                    points=wp.array(v, dtype=wp.vec3, device=device_wp),
                    indices=wp.array(np.ravel(f), dtype=int, device=device_wp),
                )
            )
        return WarpMeshes(warp_meshes=warp_meshes, warp_meshes_first_idx=meshes_first_idx.to(device))

    @property
    def num_scenes(self) -> int:
        return self._meshes_first_idx_wp.shape[0]

    @property
    def num_meshes(self) -> int:
        return self._mesh_ids_wp.shape[0]

    def query_signed_distances(
        self,
        query_points: Float[torch.Tensor, "num_points 3"],
        query_points_first_idx: Int[torch.Tensor, "num_scenes"],
        mesh_poses: Optional[Float[torch.Tensor, "num_meshes 4 4"]] = None,
        mesh_scales: Optional[Float[torch.Tensor, "num_meshes"]] = None,
        max_dist: float = 1e6,
    ) -> Tuple[
        Float[torch.Tensor, "num_points"], Float[torch.Tensor, "num_points 3"], Float[torch.Tensor, "num_points 3"]
    ]:
        """Query signed distances.

        Returns:
            torch.Tensor: differentiable signed distances (num_points).
            torch.Tensor: normals (num_points, 3).
            torch.Tensor: closest points (num_points, 3).
        """
        if query_points_first_idx.shape[0] != self.num_scenes:
            raise ValueError(f"Number of scenes mismatch: {query_points_first_idx.shape[0]} vs {self.num_scenes}.")
        if mesh_poses is not None and mesh_poses.shape[0] != self.num_meshes:
            raise ValueError(f"Number of meshes mismatch: {mesh_poses.shape[0]} vs {self.num_meshes}.")
        if mesh_scales is not None and mesh_scales.shape[0] != self.num_meshes:
            raise ValueError(f"Number of meshes mismatch: {mesh_scales.shape[0]} vs {self.num_meshes}.")

        full_query_points_first_idx = torch.cat(
            [query_points_first_idx, torch.tensor([query_points.shape[0]], device=query_points.device)]
        )
        max_num_pts_per_scene = torch.diff(full_query_points_first_idx).max().item()

        sdf = torch.empty_like(query_points[..., 0], requires_grad=False)
        normals = torch.empty_like(query_points, requires_grad=False)
        clst_pts = torch.empty_like(query_points, requires_grad=False)

        if mesh_poses is not None:
            inv_mesh_poses = inverse_tf_mat(mesh_poses)
            inv_mesh_poses_wp = wp.from_torch(inv_mesh_poses, dtype=wp.mat44, requires_grad=False)
        else:
            inv_mesh_poses_wp = None
        if mesh_scales is not None:
            mesh_scales_wp = wp.from_torch(mesh_scales, dtype=wp.float32, requires_grad=False)
        else:
            mesh_scales_wp = None

        if mesh_poses is not None or mesh_scales is not None:
            clst_pts_in_mesh_coord = torch.empty_like(query_points, requires_grad=False)
            clst_pts_in_mesh_coord_wp = wp.from_torch(clst_pts_in_mesh_coord.view(-1, 3), dtype=wp.vec3)
            clst_mesh_indices = torch.empty_like(query_points[..., 0], dtype=torch.int32, requires_grad=False)
            clst_mesh_indices_wp = wp.from_torch(clst_mesh_indices.view(-1), dtype=wp.int32)
        else:
            clst_pts_in_mesh_coord_wp = None
            clst_mesh_indices_wp = None

        wp.launch(
            kernel=query_sdf_on_meshes,
            dim=(max_num_pts_per_scene, self.num_scenes),
            inputs=[
                wp.from_torch(query_points.contiguous().view(-1, 3), dtype=wp.vec3, requires_grad=False),
                wp.from_torch(query_points_first_idx.contiguous().to(torch.int32), dtype=wp.int32, requires_grad=False),
                self._mesh_ids_wp,
                self._meshes_first_idx_wp,
                inv_mesh_poses_wp,
                mesh_poses is not None,
                mesh_scales_wp,
                mesh_scales is not None,
                max_dist,
                wp.from_torch(sdf.view(-1), dtype=wp.float32),
                wp.from_torch(normals.view(-1, 3), dtype=wp.vec3),
                wp.from_torch(clst_pts.view(-1, 3), dtype=wp.vec3),
                clst_pts_in_mesh_coord_wp,
                clst_mesh_indices_wp,
            ],
            device=wp.device_from_torch(query_points.device),
        )
        if clst_mesh_indices_wp is not None:
            clst_mesh_indices = clst_mesh_indices.to(torch.long)
        if mesh_poses is not None:
            inv_closest_mesh_poses = torch.index_select(
                inv_mesh_poses,
                dim=0,
                index=clst_mesh_indices.view(-1),
            )
            pts_in_mesh_coord = transform_points(query_points.unsqueeze(-2), inv_closest_mesh_poses).squeeze(-2)
        else:
            pts_in_mesh_coord = query_points
        if mesh_scales is not None:
            pts_in_mesh_coord = pts_in_mesh_coord / mesh_scales[clst_mesh_indices].unsqueeze(-1)
        if mesh_poses is None and mesh_scales is None:
            clst_pts_in_mesh_coord = clst_pts

        diff_sdf = torch.sign(sdf) * torch.norm(pts_in_mesh_coord - clst_pts_in_mesh_coord, p=2, dim=-1)
        if mesh_scales is not None:
            diff_sdf = diff_sdf * mesh_scales[clst_mesh_indices]

        return (
            diff_sdf.view(query_points.shape[:-1]),
            normals.view(query_points.shape),
            clst_pts.view(query_points.shape),
        )

    def __repr__(self) -> str:
        return f"WarpMeshes(num_scenes={self.num_scenes}, num_meshes={self.num_meshes})"

    def __str__(self) -> str:
        return self.__repr__()


__all__ = ["WarpMeshes"]
