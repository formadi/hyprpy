""":class:`Workspace` objects represent individual workspaces in Hyprland."""

from typing import List

from hyprpy.data.models import WorkspaceData
from hyprpy.components import instances, windows, monitors
from hyprpy.components.common import ParentNotFoundException


class Workspace:
    """Represents a workspace in Hyprland."""

    def __init__(self, workspace_data: dict, instance: 'instances.Instance'):
        data = WorkspaceData.model_validate(workspace_data)

        version = "hyprland 0.42.x"

        if version == "hyprland 0.43.x":
            self.id                 : int  = data.id
            self.name               : str  = data.name
            self.monitor_name       : str  = data.monitor_name
            self.last_window_address: str  = data.last_window_address
            self.last_window_title  : str  = data.last_window_title
            self.window_count       : int  = data.window_count
            self.has_fullscreen     : bool = data.has_fullscreen
        else :
            self.id                 : int  = data.id
            self.name               : str  = data.name
            self.monitor_name       : str  = data.monitor_name
            self.monitor_id         : int  = data.monitor_id
            self.window_count       : int  = data.window_count
            self.has_fullscreen     : bool = data.has_fullscreen
            self.last_window_address: str  = data.last_window_address
            self.last_window_title  : str  = data.last_window_title

        #: The :class:`~hyprpy.components.instances.Instance` managing this workspace.
        self._instance = instance


    @property
    def monitor(self) -> 'monitors.Monitor':
        """The :class:`~hyprpy.components.monitor.Monitor` this workspace is on."""

        monitor = self._instance.get_monitor_by_name(self.monitor_name)
        if not monitor:
            raise ParentNotFoundException(f"Parent monitor {self.monitor_name=!r} not found.")
        return monitor


    @property
    def windows(self) -> List['windows.Window']:
        """The list of all :class:`~hyprpy.components.window.Window`\\ s on this workspace."""

        windows = []
        for window in self._instance.get_windows():
            if window.workspace_id == self.id:
                windows.append(window)
        return windows


    @property
    def last_window_address_as_int(self) -> int:
        """The integer representation of the workspace's :attr:`~hyprpy.data.models.WorkspaceData.last_window_address` property."""

        return int(self.last_window_address, 16)


    def __repr__(self):
        return f"<Workspace(id={self.id}, name={self.name!r})>"
