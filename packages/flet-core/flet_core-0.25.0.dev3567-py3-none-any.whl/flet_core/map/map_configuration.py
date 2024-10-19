from dataclasses import dataclass, field
from enum import IntFlag
from typing import Optional, Union

from flet_core.animation import AnimationCurve
from flet_core.control import OptionalNumber
from flet_core.types import (
    DurationValue,
)


@dataclass
class MapLatitudeLongitude:
    latitude: Union[float, int]
    longitude: Union[float, int]


@dataclass
class MapLatitudeLongitudeBounds:
    corner_1: MapLatitudeLongitude
    corner_2: MapLatitudeLongitude


class MapInteractiveFlag(IntFlag):
    NONE = 0
    DRAG = 1 << 0
    FLING_ANIMATION = 1 << 1
    PINCH_MOVE = 1 << 2
    PINCH_ZOOM = 1 << 3
    DOUBLE_TAP_ZOOM = 1 << 4
    DOUBLE_TAP_DRAG_ZOOM = 1 << 5
    SCROLL_WHEEL_ZOOM = 1 << 6
    ROTATE = 1 << 7
    ALL = (
        (1 << 0)
        | (1 << 1)
        | (1 << 2)
        | (1 << 3)
        | (1 << 4)
        | (1 << 5)
        | (1 << 6)
        | (1 << 7)
    )


class MapMultiFingerGesture(IntFlag):
    NONE = 0
    PINCH_MOVE = 1 << 0
    PINCH_ZOOM = 1 << 1
    ROTATE = 1 << 2
    ALL = (1 << 0) | (1 << 1) | (1 << 2)


@dataclass
class MapInteractionConfiguration:
    enable_multi_finger_gesture_race: Optional[bool] = field(default=None)
    pinch_move_threshold: OptionalNumber = field(default=None)
    scroll_wheel_velocity: OptionalNumber = field(default=None)
    pinch_zoom_threshold: OptionalNumber = field(default=None)
    rotation_threshold: OptionalNumber = field(default=None)
    flags: Optional[MapInteractiveFlag] = field(default=None)
    rotation_win_gestures: Optional[MapMultiFingerGesture] = field(default=None)
    pinch_move_win_gestures: Optional[MapMultiFingerGesture] = field(default=None)
    pinch_zoom_win_gestures: Optional[MapMultiFingerGesture] = field(default=None)


@dataclass
class MapConfiguration:
    initial_center: Optional[MapLatitudeLongitude] = None
    initial_rotation: OptionalNumber = None
    initial_zoom: OptionalNumber = None
    interaction_configuration: Optional[MapInteractionConfiguration] = None
    bgcolor: Optional[str] = None
    keep_alive: Optional[bool] = None
    max_zoom: OptionalNumber = None
    min_zoom: OptionalNumber = None
    animation_curve: Optional[AnimationCurve] = None
    animation_duration: DurationValue = None
