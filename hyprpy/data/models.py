"""Data classes used for parsing, validating and storing JSON output received
from the Hyprland command socket.

Classes:
    - :class:`WindowData`: data for Hyprland windows.
    - :class:`WorkspaceData`: data for Hyprland workspaces.
    - :class:`MonitorData`: data for Hyprland monitors.
    - :class:`InstanceData`: data for Hyprland instances.
"""

from typing import List

from pydantic import BaseModel, Field, AliasPath

from hyprpy.data.validators import HexString, NonEmptyString


class WindowData(BaseModel):
    """Deserialization and validation of ``hyprctl`` window (client) data."""

    version = "hyprland 0.42.x"

    if version == "hyprland 0.43.x":
        address          : HexString
        is_mapped        : bool      = Field(..., alias            = "mapped")
        is_hidden        : bool      = Field(..., alias            = "hidden")
        position_x       : int       = Field(..., validation_alias = AliasPath("at", 0))
        position_y       : int       = Field(..., validation_alias = AliasPath("at", 1))
        width            : int       = Field(..., validation_alias = AliasPath("size", 0))
        height           : int       = Field(..., validation_alias = AliasPath("size", 1))
        workspace_id     : int       = Field(..., validation_alias = AliasPath("workspace", "id"))
        workspace_name   : str       = Field(..., validation_alias = AliasPath("workspace", "name"))
        is_floating      : bool      = Field(..., alias            = "floating")
        monitor_id       : int       = Field(..., alias            = "monitor")
        wm_class         : str       = Field(..., alias            = "class")
        title            : str
        initial_wm_class : str       = Field(..., alias            = "initialClass")
        initial_title    : str       = Field(..., alias            = "initialTitle")
        pid              : int
        is_xwayland      : bool      = Field(..., alias            = "xwayland")
        is_pinned        : bool      = Field(..., alias            = "pinned")
        is_fullscreen    : int       = Field(..., alias            = "fullscreen")
        fullscreen_client: int       = Field(..., alias            = "fullscreenClient")
        grouped          : list[str] = Field(..., alias            = "grouped")
        tags             : list[str] = Field(..., alias            = "tags")
        swallowing       :HexString  = Field(...,alias             = "swallowing")
        focus_history_id : int       = Field(...,alias             = "focusHistoryID")
    else :
        address          : HexString
        is_mapped        : bool      = Field(..., alias            = "mapped")
        is_hidden        : bool      = Field(..., alias            = "hidden")
        position_x       : int       = Field(..., validation_alias = AliasPath("at", 0))
        position_y       : int       = Field(..., validation_alias = AliasPath("at", 1))
        width            : int       = Field(..., validation_alias = AliasPath("size", 0))
        height           : int       = Field(..., validation_alias = AliasPath("size", 1))
        workspace_id     : int       = Field(..., validation_alias = AliasPath("workspace", "id"))
        workspace_name   : str       = Field(..., validation_alias = AliasPath("workspace", "name"))
        is_floating      : bool      = Field(..., alias            = "floating")
        pseudo           : bool      = Field(..., alias            = "pseudo")
        monitor_id       : int       = Field(..., alias            = "monitor")
        wm_class         : str       = Field(..., alias            = "class")
        title            : str       = Field(..., alias            = "title")
        initial_wm_class : str       = Field(..., alias            = "initialClass")
        initial_title    : str       = Field(..., alias            = "initialTitle")
        pid              : int
        is_xwayland      : bool      = Field(..., alias            = "xwayland")
        is_pinned        : bool      = Field(..., alias            = "pinned")
        is_fullscreen    : bool      = Field(..., alias            = "fullscreen")
        fullscreen_mode  : int       = Field(..., alias            = "fullscreenMode")
        is_fakefullscreen: bool      = Field(..., alias            = "fakeFullscreen")
        grouped          : list[str] = Field(..., alias            = "grouped")
        tags             : list[str] = Field(..., alias            = "tags")
        swallowing       : HexString = Field(...,alias             = "swallowing")
        focus_history_id : int       = Field(...,alias             = "focusHistoryID")


class WorkspaceData(BaseModel):
    """Deserialization and validation of ``hyprctl`` workspace data."""

    version = "hyprland 0.42.x"

    if version == "hyprland 0.43.x":
        id                 : int
        name               : str
        monitor_name       : str       = Field(..., alias = "monitor")
        last_window_address: HexString = Field(..., alias = "lastwindow")
        last_window_title  : str       = Field(..., alias = "lastwindowtitle")
        window_count       : int       = Field(..., alias = "windows")
        has_fullscreen     : bool      = Field(..., alias = "hasfullscreen")
    else                   :
        id                 : int
        name               : str
        monitor_name       : str       = Field(..., alias = "monitor")
        monitor_id         : int       = Field(..., alias = "monitorID")
        window_count       : int       = Field(..., alias = "windows")
        has_fullscreen     : bool      = Field(..., alias = "hasfullscreen")
        last_window_address: HexString = Field(..., alias = "lastwindow")
        last_window_title  : str       = Field(..., alias = "lastwindowtitle")


class MonitorData(BaseModel):
    """Deserialization and validation of ``hyprctl`` monitor data."""

    id                   : int
    name                 : str
    description          : str
    make                 : str
    model                : str
    serial               : str
    width                : int
    height               : int
    refresh_rate         : float = Field(..., alias            = "refreshRate")
    position_x           : int   = Field(..., alias            = "x")
    position_y           : int   = Field(..., alias            = "y")
    active_workspace_id  : int   = Field(..., validation_alias = AliasPath("activeWorkspace", "id"))
    active_workspace_name: str   = Field(..., validation_alias = AliasPath("activeWorkspace", "name"))
    reserved             : List[int]
    scale                : float
    transform            : int
    is_focused           : bool  = Field(..., alias            = "focused")
    uses_dpms            : bool  = Field(..., alias            = "dpmsStatus")
    vrr                  : bool


class InstanceData(BaseModel):
    """Deserialization and validation of ``hyprctl`` instance data."""

    #: `Instance signature <https://wiki.hyprland.org/IPC/#hyprland-instance-signature-his>`_ of the Hyprland instance.
    signature: NonEmptyString
