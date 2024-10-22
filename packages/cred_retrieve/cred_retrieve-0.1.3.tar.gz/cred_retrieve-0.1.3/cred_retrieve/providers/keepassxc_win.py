import os
import winreg
import subprocess
from reg_query import WIN64READ, traverse

from ..provider import CredentialProvider

def match_displayname(app_name: str):
    """Return a function to match registry entries by display name."""
    def match(subkey):
        display_name = winreg.QueryValueEx(subkey, 'DisplayName')[0]
        if app_name.lower() in display_name.lower():
            install_location = winreg.QueryValueEx(subkey, 'InstallLocation')[0]
            if install_location:
                return True, install_location
        return False, None
    return match

registry_paths = (
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
    r"HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
)

def get_keepassxc_install_path() -> str:
    """Retrieve the installation path for KeePassXC."""
    match = match_displayname('keepassxc')
    rv = traverse(registry_paths[0], match, WIN64READ)
    if not rv:
        rv = traverse(registry_paths[1], match, WIN64READ)
    return rv

def get_keepassxc_path() -> str:
    """Get the path to the KeePassXC CLI executable."""
    base = get_keepassxc_install_path()
    if not base:
        return None
    return os.path.join(base, 'keepassxc-cli.exe')
