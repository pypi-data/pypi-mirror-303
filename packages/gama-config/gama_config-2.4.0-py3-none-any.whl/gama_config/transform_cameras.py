from typing import List
from greenstream_config import Camera
from gama_config.gama_vessel import Mode


def transform_camera_pipelines(cameras: List[Camera], mode: Mode, namespace: str):
    """
    Transforms the camera pipelines based on the mode of operation.
    """

    if len(cameras) == 0:
        raise ValueError("No cameras found in the vessel config yml")

    if mode == Mode.STUBS:
        # Use a test pattern for the camera
        for camera in cameras:
            camera.elements = [
                "videotestsrc pattern=ball",
                "video/x-raw, format=RGB,width=1920,height=1080",
            ]
    elif mode == Mode.SIMULATOR:
        for camera in cameras:
            # Use the ROS image source for the camera
            camera.elements = [
                f"rosimagesrc ros-topic=sensors/cameras/{camera.name}_{camera.type}/image_raw ros-name='gst_rosimagesrc_{camera.name}_{camera.type}' ros-namespace='{namespace}'"
            ]
            # Don't publish the image back out to ROS as it came from there
            camera.camera_frame_topic = None

    return cameras
