from typing import List, Optional

from greenstream_config.types import Camera, CameraOverride


def merge_cameras(
    cameras: List[Camera], overrides: List[Optional[CameraOverride]]
) -> List[Camera]:
    """
    The gama_vessel may contain camera overrides.
    If it does, we need to merge them with the default cameras.
    """

    if overrides is None:
        return cameras

    overriden_cameras: List[Camera] = cameras
    for idx, override in enumerate(overrides):
        # If override is null/None, we don't want to override the default camera
        if override:
            if idx < len(overriden_cameras):

                # applies changes to the camera only if attribute is not None
                overriden_cameras[idx] = Camera(
                    name=override.name or cameras[idx].name,
                    order=override.order or cameras[idx].order,
                    elements=override.elements or cameras[idx].elements,
                    offsets=override.offsets or cameras[idx].offsets,
                    pixel_width=override.pixel_width or cameras[idx].pixel_width,
                    pixel_height=override.pixel_height or cameras[idx].pixel_height,
                    k_intrinsic=override.k_intrinsic or cameras[idx].k_intrinsic,
                    distortion_model=override.distortion_model or cameras[idx].distortion_model,
                    distortion_parameters=override.distortion_parameters
                    or cameras[idx].distortion_parameters,
                    camera_frame_topic=override.camera_frame_topic
                    or cameras[idx].camera_frame_topic,
                    camera_info_topic=override.camera_info_topic or cameras[idx].camera_info_topic,
                    type=override.type or cameras[idx].type,
                    ros_throttle_time=override.ros_throttle_time or cameras[idx].ros_throttle_time,
                    undistort_image=override.undistort_image or cameras[idx].undistort_image,
                )

    return overriden_cameras
