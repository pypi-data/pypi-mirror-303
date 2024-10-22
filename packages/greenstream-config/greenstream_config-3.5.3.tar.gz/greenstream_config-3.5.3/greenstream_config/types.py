from dataclasses import dataclass, field
from typing import List, Literal, Optional

from pydantic import BaseModel, field_validator


class Offsets(BaseModel):
    # in radians in FLU
    roll: Optional[float] = None
    pitch: Optional[float] = None
    yaw: Optional[float] = None
    forward: Optional[float] = None
    left: Optional[float] = None
    up: Optional[float] = None


class PTZLimits(BaseModel):
    min: float  # in radians if pan/tilt, fraction if zoom
    max: float  # in radians if pan/tilt, fraction if zoom


class PTZComponent(BaseModel):
    move_type: Literal["pan", "tilt", "zoom"]
    home: float  # in radians if pan/tilt, fraction if zoom
    joint_offsets: Optional[Offsets] = None
    joint_limits: Optional[PTZLimits] = None
    joystick_axis_index: Optional[int] = None
    reverse_joystick_input: bool = False


class PTZControlSettings(BaseModel):
    absolute_move_tolerance: Optional[float] = 0.0175  # radians
    query_timeout: Optional[int] = 2  # seconds
    check_camera_rate: Optional[float] = 1.0  # period in seconds
    publish_rate: Optional[float] = 10.0  # period in seconds
    wsdl_dir: Optional[str] = "/home/ros/.local/lib/python3.12/site-packages/wsdl"
    continuous_state_publishing: Optional[bool] = True
    # Whether to transform the camera from FRD (for ptz) to FLU
    frd_to_flu_transform: bool = True


class PTZOnvif(BaseModel):
    ip_address: str
    port: int
    username: str
    password: str
    # joystick topic to listen to for PTZ control
    joystick_topic: Optional[str]
    # List of PTZ components that the camera has, order is important as it will determine joint hierarchy
    ptz_components: List[PTZComponent]
    settings: PTZControlSettings = PTZControlSettings()

    # Ensure that only one of each ptz move type is defined
    @field_validator("ptz_components")
    def check_unique_move_types(cls, v):
        move_types = [component.move_type for component in v]
        if len(move_types) != len(set(move_types)):
            raise ValueError("Duplicate move types in PTZ components")
        return v

    @field_validator("ptz_components")
    def check_has_components(cls, v):
        if len(v) == 0:
            raise ValueError("No PTZ components defined")
        return v


class Camera(BaseModel):
    # This will become the name of frame-id, ros topic and webrtc stream
    name: str
    # Used to order the stream in the UI
    order: int
    # An array of gstream source / transform elements e.g.
    # ["v4l2src", "video/x-raw, format=RGB,width=1920,height=1080"]
    elements: List[str]

    pixel_width: int
    pixel_height: int
    # Published ros topic names
    camera_frame_topic: Optional[str]
    camera_info_topic: Optional[str]
    # Camera intrinsics and distortion parameters from callibration
    k_intrinsic: Optional[List[float]] = field(
        default_factory=lambda: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    )
    distortion_parameters: Optional[List[float]] = field(
        default_factory=lambda: [0.0, 0.0, 0.0, 0.0, 0.0]
    )
    distortion_model: str = "plumb_bob"
    # If false, it expects the camera_info topic published somewhere else e.g. from rosbag
    publish_camera_info: bool = True
    # Free scaling parameter for undistorted image between 0 (all pixels are valid), and 1 (all source pixels are retained i.e. max distortion FOV)
    distortion_kmat_alpha: float = 0.5
    # The camera's position relative to the vessel base_link
    offsets: Optional[Offsets] = None
    type: str = "color"
    ros_throttle_time: float = 0.0000001
    # Whether to undistort the image in gstreamer pipeline before publishing
    undistort_image: bool = False
    # Whether the camera has a pan-tilt-zoom system enabled.
    ptz: Optional[PTZOnvif] = None


class CameraOverride(BaseModel):
    # This will become the name of frame-id, ros topic and webrtc stream
    name: Optional[str]
    order: Optional[int]
    # An array of gstream source / transform elements e.g.
    # ["v4l2src", "video/x-raw, format=RGB,width=1920,height=1080"]
    elements: Optional[List[str]]
    pixel_width: Optional[int]
    pixel_height: Optional[int]
    # Published ros topic names
    camera_frame_topic: Optional[str]
    camera_info_topic: Optional[str]
    # Camera intrinsics and distortion parameters from callibration
    k_intrinsic: Optional[List[float]] = None
    distortion_parameters: Optional[List[float]] = None
    distortion_model: str = "plumb_bob"
    # The camera's position relative to the vessel base_link
    offsets: Optional[Offsets] = None
    type: Optional[str] = "color"
    ros_throttle_time: Optional[float] = 0.0000001
    # Whether to undistort the image in gstreamer pipeline before publishing
    undistort_image: Optional[bool] = False


class GreenstreamConfig(BaseModel):
    cameras: List[Camera]
    camera_overrides: Optional[List[Optional[CameraOverride]]] = None
    signalling_server_port: int = 8443
    namespace: str = "greenstream"  # eg. vessel_1
    ui_port: int = 8000
    mode: str = "simulator"
    debug: bool = False
    diagnostics_topic: str = "diagnostics"
