from typing import List, Optional, Tuple

from gr_urchin import Joint, JointLimit, Link, xyz_rpy_to_matrix
from greenstream_config.merge_cameras import merge_cameras
from greenstream_config.types import Camera, CameraOverride


def get_camera_urdf(
    camera: Camera,
    links: List[Link],
    joints: List[Joint],
    namespace_prefix: str = "",
    add_optical_frame: bool = True,
    has_duplicate_camera_link: bool = False,
) -> Tuple[List[Link], List[Joint]]:
    # This is the camera urdf from the gama/lookout greenstream.launch.py
    # We need to generate this from the camera config

    # Only generate camera link if it currently doesn't exist. This checks for multiple cameras within the same housing
    # etc: bow camera has both visible and thermal cameras, it is assumed that they are connected via the same ptz system
    if not has_duplicate_camera_link:
        camera_xyz_rpy = (
            [
                camera.offsets.forward or 0.0,
                camera.offsets.left or 0.0,
                camera.offsets.up or 0.0,
                camera.offsets.roll or 0.0,
                camera.offsets.pitch or 0.0,
                camera.offsets.yaw or 0.0,
            ]
            if camera.offsets
            else [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        )

        links.append(
            Link(
                name=f"{namespace_prefix}{camera.name}_link",
                inertial=None,
                visuals=None,
                collisions=None,
            )
        )
        joints.append(
            Joint(
                name=f"{namespace_prefix}{camera.name}_joint",
                parent=f"{namespace_prefix}base_link",
                child=f"{namespace_prefix}{camera.name}_link",
                joint_type="fixed",
                origin=xyz_rpy_to_matrix(camera_xyz_rpy),
            )
        )

        if camera.ptz:
            for ptz_component in camera.ptz.ptz_components:
                parent_link = links[-1].name
                if ptz_component.move_type == "pan":
                    links.append(
                        Link(
                            name=f"{namespace_prefix}{camera.name}_pan_link",
                            inertial=None,
                            visuals=None,
                            collisions=None,
                        ),
                    )

                    if ptz_component.joint_limits:
                        pan_joint_limit = JointLimit(
                            lower=ptz_component.joint_limits.min,
                            upper=ptz_component.joint_limits.max,
                            effort=0.0,
                            velocity=0.0,
                        )

                    camera_pan_xyz_rpy = (
                        [
                            ptz_component.joint_offsets.forward or 0.0,
                            ptz_component.joint_offsets.left or 0.0,
                            ptz_component.joint_offsets.up or 0.0,
                            ptz_component.joint_offsets.roll or 0.0,
                            ptz_component.joint_offsets.pitch or 0.0,
                            ptz_component.joint_offsets.yaw or 0.0,
                        ]
                        if ptz_component.joint_offsets
                        else [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                    )

                    # add home position to pan joint origin
                    if ptz_component.home:
                        camera_pan_xyz_rpy[5] += ptz_component.home

                    joints.append(
                        Joint(
                            name=f"{namespace_prefix}{camera.name}_pan_joint",
                            parent=parent_link,
                            child=f"{namespace_prefix}{camera.name}_pan_link",
                            joint_type="revolute" if ptz_component.joint_limits else "continuous",
                            limit=pan_joint_limit if ptz_component.joint_limits else None,
                            origin=xyz_rpy_to_matrix(camera_pan_xyz_rpy),
                            axis=[0, 0, 1],
                        )
                    )

                elif ptz_component.move_type == "tilt":
                    links.append(
                        Link(
                            name=f"{namespace_prefix}{camera.name}_tilt_link",
                            inertial=None,
                            visuals=None,
                            collisions=None,
                        ),
                    )

                    if ptz_component.joint_limits:
                        tilt_joint_limit = JointLimit(
                            lower=ptz_component.joint_limits.min,
                            upper=ptz_component.joint_limits.max,
                            effort=0.0,
                            velocity=0.0,
                        )

                    camera_tilt_xyz_rpy = (
                        [
                            ptz_component.joint_offsets.forward or 0.0,
                            ptz_component.joint_offsets.left or 0.0,
                            ptz_component.joint_offsets.up or 0.0,
                            ptz_component.joint_offsets.roll or 0.0,
                            ptz_component.joint_offsets.pitch or 0.0,
                            ptz_component.joint_offsets.yaw or 0.0,
                        ]
                        if ptz_component.joint_offsets
                        else [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                    )

                    # add home position to tilt joint origin
                    if ptz_component.home:
                        camera_tilt_xyz_rpy[4] += ptz_component.home

                    joints.append(
                        Joint(
                            name=f"{namespace_prefix}{camera.name}_tilt_joint",
                            parent=parent_link,
                            child=f"{namespace_prefix}{camera.name}_tilt_link",
                            joint_type="revolute" if ptz_component.joint_limits else "continuous",
                            limit=tilt_joint_limit if ptz_component.joint_limits else None,
                            origin=xyz_rpy_to_matrix(camera_tilt_xyz_rpy),
                            axis=[0, 1, 0],
                        )
                    )

    if add_optical_frame:

        if has_duplicate_camera_link:
            # search for the parent link of another camera frame bounded by the same camera link (i.e. color, thermal within the same housing)
            for joint in reversed(joints):
                # account for namespace prefix
                unprefixed_child_link_name = joint.child.lstrip(namespace_prefix)
                if (
                    unprefixed_child_link_name.startswith(camera.name)
                    and unprefixed_child_link_name.endswith("frame")
                    and "optical" not in unprefixed_child_link_name
                ):
                    parent_link = joint.parent
                    break
        else:
            parent_link = links[-1].name

        links.append(
            Link(
                name=f"{namespace_prefix}{camera.name}_{camera.type}_frame",
                inertial=None,
                visuals=None,
                collisions=None,
            )
        )
        links.append(
            Link(
                name=f"{namespace_prefix}{camera.name}_{camera.type}_optical_frame",
                inertial=None,
                visuals=None,
                collisions=None,
            )
        )
        # fixed transforms between camera frame and optical frame FRD -> NED
        joints.append(
            Joint(
                name=f"{parent_link}_to_{camera.type}_frame",
                parent=f"{parent_link}",
                child=f"{namespace_prefix}{camera.name}_{camera.type}_frame",
                joint_type="fixed",
                origin=xyz_rpy_to_matrix([0, 0, 0, 0, 0, 0]),
            )
        )
        joints.append(
            Joint(
                name=f"{namespace_prefix}{camera.name}_{camera.type}_frame_to_optical_frame",
                parent=f"{namespace_prefix}{camera.name}_{camera.type}_frame",
                child=f"{namespace_prefix}{camera.name}_{camera.type}_optical_frame",
                joint_type="fixed",
                origin=xyz_rpy_to_matrix([0, 0, 0, -1.570796, 0, -1.570796]),
            )
        )

    return (links, joints)


def get_cameras_urdf(
    cameras: List[Camera],
    camera_overrides: List[Optional[CameraOverride]],
    add_optical_frame: bool = True,
    namespace: str = "",
) -> Tuple[List[Link], List[Joint]]:

    links: List[Link] = []
    joints: List[Joint] = []
    cameras = merge_cameras(cameras, camera_overrides)
    namespace_prefix = f"{namespace}_" if namespace != "" else ""

    # assume cameras have already been merged with overrides
    for camera in cameras:

        # skip duplicate camera links, only add optical frame of camera of a different type (i.e. color, thermal)
        if camera.name in [prev_camera.name for prev_camera in cameras[: cameras.index(camera)]]:
            links, joints = get_camera_urdf(
                camera,
                links,
                joints,
                namespace_prefix,
                add_optical_frame,
                has_duplicate_camera_link=True,
            )
        else:
            links, joints = get_camera_urdf(
                camera,
                links,
                joints,
                namespace_prefix,
                add_optical_frame,
                has_duplicate_camera_link=False,
            )

    return links, joints
