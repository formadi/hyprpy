""":class:`Window` objects represent individual windows in Hyprland."""

from hyprpy.data.models import WindowData
from hyprpy.components import instances, workspaces
from hyprpy.components.common import ParentNotFoundException


class Window:
    """Represents a window in the Hyprland compositor."""

    def __init__(self, window_data: dict, instance: 'instances.Instance'):
        data = WindowData.model_validate(window_data)

        version = "hyprland 0.42.x"

        if version == "hyprland 0.43.x":
            self.address          : str       = data.address
            self.is_mapped        : bool      = data.is_mapped
            self.is_hidden        : bool      = data.is_hidden
            self.position_x       : int       = data.position_x
            self.position_y       : int       = data.position_y
            self.width            : int       = data.width
            self.height           : int       = data.height
            self.workspace_id     : int       = data.workspace_id
            self.workspace_name   : str       = data.workspace_name
            self.is_floating      : bool      = data.is_floating
            self.monitor_id       : int       = data.monitor_id
            self.wm_class         : str       = data.wm_class
            self.title            : str       = data.title
            self.initial_wm_class : str       = data.initial_wm_class
            self.initial_title    : str       = data.initial_title
            self.pid              : int       = data.pid
            self.is_xwayland      : bool      = data.is_xwayland
            self.is_pinned        : bool      = data.is_pinned
            self.is_fullscreen    : int       = data.is_fullscreen
            self.fullscreen_client: int       = data.fullscreen_client
            self.grouped          : list[str] = data.grouped
            self.tags             : list[str] = data.tags
            self.swallowing       : str       = data.swallowing
            self.focus_history_id : int       = data.focus_history_id
        else :
            self.address          : str       = data.address
            self.is_mapped        : bool      = data.is_mapped
            self.is_hidden        : bool      = data.is_hidden
            self.position_x       : int       = data.position_x
            self.position_y       : int       = data.position_y
            self.width            : int       = data.width
            self.height           : int       = data.height
            self.workspace_id     : int       = data.workspace_id
            self.workspace_name   : str       = data.workspace_name
            self.is_floating      : bool      = data.is_floating
            self.pseudo           : bool      = data.pseudo
            self.monitor_id       : int       = data.monitor_id
            self.wm_class         : str       = data.wm_class
            self.title            : str       = data.title
            self.initial_wm_class : str       = data.initial_wm_class
            self.initial_title    : str       = data.initial_title
            self.pid              : int       = data.pid
            self.is_xwayland      : bool      = data.is_xwayland
            self.is_pinned        : bool      = data.is_pinned
            self.is_fullscreen    : bool      = data.is_fullscreen
            self.fullscreen_mode  : int       = data.fullscreen_mode
            self.is_fakefullscreen: bool      = data.is_fakefullscreen
            self.grouped          : list[str] = data.grouped
            self.tags             : list[str] = data.tags
            self.swallowing       : str       = data.swallowing
            self.focus_history_id : int       = data.focus_history_id

        #: The :class:`~hyprpy.components.instances.Instance` managing this window.
        self._instance = instance




    @property
    def workspace(self) -> 'workspaces.Workspace':
        """The :class:`~hyprpy.components.workspace.Workspace` which this window is in."""

        workspace = self._instance.get_workspace_by_id(self.workspace_id)
        if not workspace:
            raise ParentNotFoundException(f"Parent workspace {self.workspace_id=} not found.")
        return workspace


    @property
    def address_as_int(self) -> int:
        """The integer representation of the window's :attr:`~hyprpy.data.models.WindowData.address` property."""

        return int(self.address, 16)


    def __repr__(self):
        max_title_length = 24
        title_repr = self.title if len(self.title) <= max_title_length else self.title[:max_title_length-3] + "..."
        return f"<Window(address={self.address!r}, wm_class={self.wm_class!r}, title={title_repr!r})>"
