"""`Monitor` objects represent monitors in Hyprland."""

from typing import List

from hyprpy.data.models import MonitorData
from hyprpy.components import instances, workspaces

class Monitor:
    """Represents a monitor within Hyprland."""

    def __init__(self, monitor_data: str, instance: 'instances.Instance'):
        data = MonitorData.model_validate(monitor_data)

        self.id                   : int       = data.id
        self.name                 : str       = data.name
        self.description          : str       = data.description
        self.make                 : str       = data.make
        self.model                : str       = data.model
        self.serial               : str       = data.serial
        self.width                : int       = data.width
        self.height               : int       = data.height
        self.refresh_rate         : float     = data.refresh_rate
        self.position_x           : int       = data.position_x
        self.position_y           : int       = data.position_y
        self.active_workspace_id  : int       = data.active_workspace_id
        self.active_workspace_name: str       = data.active_workspace_name
        self.reserved             : List[int] = data.reserved
        self.scale                : float     = data.scale
        self.transform            : int       = data.transform
        self.is_focused           : bool      = data.is_focused
        self.uses_dpms            : bool      = data.uses_dpms
        self.vrr                  : bool      = data.vrr

        #: The :class:`~hyprpy.components.instances.Instance` managing this monitor.
        self._instance = instance


    @property
    def workspaces(self) -> List['workspaces.Workspace']:
        """All :class:`~hyprpy.components.workspace.Workspace`\\ s located on this monitor."""

        workspaces = []
        for workspace in self._instance.get_workspaces():
            if workspace.monitor_name == self.name:
                workspaces.append(workspace)
        return workspaces


    def __repr__(self):
        return f"<Monitor(id={self.id}, name={self.name!r}, width={self.width}, height={self.height})>"
