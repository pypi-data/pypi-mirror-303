from typing import List
from math import radians
from gama_config.gama_vessel import GamaVesselConfig, Variant
from greenstream_config import Camera, Offsets, get_cameras_urdf
from gr_urchin import URDF, Joint, Material, Link, xyz_rpy_to_matrix, Visual, Mesh, Geometry


def prefix_joints_and_links(urdf: URDF, prefix: str) -> URDF:
    if prefix == "":
        return urdf

    for joint in urdf.joints:
        joint.name = f"{prefix}_{joint.name}"
        joint.parent = f"{prefix}_{joint.parent}"
        joint.child = f"{prefix}_{joint.child}"
    for link in urdf.links:
        link.name = f"{prefix}_{link.name}"

    return urdf


def generate_urdf(
    config: GamaVesselConfig,
    cameras: List[Camera] | None,
    ins_offset: Offsets,
    mesh_path: str | None = None,
    waterline=0.0,  # meters between the waterline and the base_link
    radar_height=6.552,
    add_optical_frame: bool = True,
):
    file_path = f"/tmp/vessel_{config.variant.value}_{config.mode.value}.urdf"
    camera_links, camera_joints = get_cameras_urdf(
        cameras or [], [None], add_optical_frame, config.namespace_vessel
    )

    urdf = URDF(
        name="origins",
        materials=[
            Material(name="grey", color=[0.75, 0.75, 0.75, 1]),
            Material(name="blue", color=[0, 0, 1, 1]),
        ],
        links=[
            Link(name="ins_link", inertial=None, visuals=None, collisions=None),
            Link(
                name="waterline_link",
                inertial=None,
                visuals=None,
                collisions=None,
            ),
            Link(
                name="base_link",
                inertial=None,
                visuals=None,
                collisions=None,
            ),
            Link(
                name="visual_link",
                inertial=None,
                visuals=(
                    [
                        Visual(
                            name="visual",
                            geometry=Geometry(
                                mesh=Mesh(
                                    filename=mesh_path, combine=False, lazy_filename=mesh_path
                                )
                            ),
                            material=Material(name="grey"),
                        )
                    ]
                    if mesh_path
                    else []
                ),
                collisions=None,
            ),
        ],
        joints=[
            Joint(
                name="base_to_visual",
                parent="base_link",
                child="visual_link",
                joint_type="fixed",
                origin=xyz_rpy_to_matrix([0, 0, 0, -radians(90), 0, 0]),
            ),
            Joint(
                name="base_to_ins",
                parent="base_link",
                child="ins_link",
                joint_type="fixed",
                origin=xyz_rpy_to_matrix(
                    [
                        ins_offset.forward,
                        ins_offset.left,
                        ins_offset.up,
                        ins_offset.roll,
                        ins_offset.pitch,
                        ins_offset.yaw,
                    ]
                ),
            ),
            Joint(
                name="base_to_waterline",
                parent="base_link",
                child="waterline_link",
                joint_type="fixed",
                origin=xyz_rpy_to_matrix([0, 0, -waterline, 0, 0, 0]),
            ),
        ],
    )
    # Add a radar
    if config.variant == Variant.ARMIDALE:
        urdf._links.append(
            Link(
                name="radar",
                inertial=None,
                visuals=[],
                collisions=None,
            )
        )
        urdf._joints.append(
            Joint(
                name="baselink_to_radar",
                parent="base_link",
                child="radar",
                joint_type="fixed",
                origin=xyz_rpy_to_matrix([0.0, 0.0, radar_height, 0.0, 0.0, radians(-1.5)]),
            )
        )

    # Prefix all joints and links
    urdf = prefix_joints_and_links(urdf, config.namespace_vessel)

    # These are already prefixed
    urdf._joints.extend(camera_joints)
    urdf._links.extend(camera_links)

    urdf.save(file_path)

    # stringify urdf response for robot description
    with open(file_path) as infp:
        robot_description = infp.read()

    return robot_description
