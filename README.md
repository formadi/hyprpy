# Hyprpy

 This is a modified version for "personal" use, and it is a repository to support Hyprland >= 0.42.0. The changes are as follows.
- Changed signal name to Hyprland event name.
- Added signals for Hyprland events.
- Fixed an issue that occurred when switching windows to fullscreen mode.

## Usage:
1. Install the original version first:
```
pip3 install hyprpy
```

2. Download the source code from this repository using git clone and overwrite the installed original source with it.
for example:
```
git clone https://github.com/formadi/hyprpy.git
cd hyprpy
cp -Rf hyprpy /path/to/pythonX.XX/site-packages/
```

3. The default setting is for Hyprland 0.42.x. To use it with version 0.43.x, you need to find all instances of version = "hyprland 0.42.x" and change them to version = "hyprland 0.43.x"
