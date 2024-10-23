# mypy: disable-error-code="valid-type"
import warp as wp


@wp.func
def get_rotation_matrix(tf_mat: wp.mat44) -> wp.mat33:
    # fmt: off
    return wp.mat33(
        tf_mat[0, 0], tf_mat[0, 1], tf_mat[0, 2],
        tf_mat[1, 0], tf_mat[1, 1], tf_mat[1, 2],
        tf_mat[2, 0], tf_mat[2, 1], tf_mat[2, 2]
    )
    # fmt: on


@wp.kernel
def query_sdf_on_meshes(
    points: wp.array(dtype=wp.vec3),
    points_first_idx: wp.array(dtype=wp.int32),
    mesh_ids: wp.array(dtype=wp.uint64),
    mesh_ids_first_idx: wp.array(dtype=wp.int32),
    inv_mesh_poses: wp.array(dtype=wp.mat44),
    enable_inv_mesh_poses: bool,
    mesh_scales: wp.array(dtype=wp.float32),
    enable_mesh_scales: bool,
    max_dist: float,
    signed_dists: wp.array(dtype=wp.float32),
    normals: wp.array(dtype=wp.vec3),
    closest_points: wp.array(dtype=wp.vec3),
    closest_points_in_mesh_coord: wp.array(dtype=wp.vec3),
    closest_mesh_indices: wp.array(dtype=wp.int32),
):
    pt_local_idx, batch_idx = wp.tid()
    pts_begin_idx = points_first_idx[batch_idx]
    if batch_idx + 1 < points_first_idx.shape[0]:
        pts_end_idx = points_first_idx[batch_idx + 1]
    else:
        pts_end_idx = points.shape[0]
    pt_idx = pts_begin_idx + pt_local_idx
    if pt_idx >= pts_end_idx:
        return
    q_pt = points[pt_idx]

    m_begin_idx = mesh_ids_first_idx[batch_idx]
    if batch_idx + 1 < mesh_ids_first_idx.shape[0]:
        m_end_idx = mesh_ids_first_idx[batch_idx + 1]
    else:
        m_end_idx = mesh_ids.shape[0]

    min_dist = max_dist

    for m_idx in range(m_begin_idx, m_end_idx):
        if enable_inv_mesh_poses:
            q_pt_in_mesh_coord = wp.transform_point(inv_mesh_poses[m_idx], q_pt)
        else:
            q_pt_in_mesh_coord = q_pt
        if enable_mesh_scales:
            q_pt_in_mesh_coord /= mesh_scales[m_idx]

        query = wp.mesh_query_point(mesh_ids[m_idx], q_pt_in_mesh_coord, max_dist)

        if query.result:
            clst_pt_in_mesh_coord = wp.mesh_eval_position(mesh_ids[m_idx], query.face, query.u, query.v)
            unscaled_dist = wp.length(clst_pt_in_mesh_coord - q_pt_in_mesh_coord) * query.sign
            if enable_mesh_scales:
                dist = unscaled_dist * mesh_scales[m_idx]
            else:
                dist = unscaled_dist

            if dist < min_dist:
                min_dist = dist
                normal_in_mesh_coord = wp.mesh_eval_face_normal(mesh_ids[m_idx], query.face)

                # scaling doesn't effect normal
                if enable_mesh_scales:
                    clst_pt = clst_pt_in_mesh_coord * mesh_scales[m_idx]
                else:
                    clst_pt = clst_pt_in_mesh_coord

                if enable_inv_mesh_poses:
                    m_pose = wp.inverse(inv_mesh_poses[m_idx])
                    clst_pt = wp.transform_point(m_pose, clst_pt)
                    normal = wp.mul(get_rotation_matrix(m_pose), normal_in_mesh_coord)
                else:
                    # clst_pt = clst_pt
                    normal = normal_in_mesh_coord

                signed_dists[pt_idx] = dist
                normals[pt_idx] = normal
                closest_points[pt_idx] = clst_pt

                if enable_inv_mesh_poses or enable_mesh_scales:
                    closest_points_in_mesh_coord[pt_idx] = clst_pt_in_mesh_coord
                    closest_mesh_indices[pt_idx] = wp.int32(m_idx)
