# Enterprise-level OS Environment Detector
# This class provides comprehensive system information gathering capabilities
# suitable for large-scale deployments and complex infrastructure environments.

import platform
import os
import distro
import subprocess
import shutil
from fsd.util.utils import read_file_content, call_error_api

class OSEnvironmentDetector:
    def __init__(self):
        # The OSEnvironmentDetector gathers OS information when the class is instantiated
        self.os_data = self._gather_os_info()

    def _gather_os_info(self):
        """
        The OSEnvironmentDetector gathers comprehensive OS information for any platform (Windows, macOS, Linux, etc.) to support AI for dependency installation.
        """
        try:
            os_info = {
                "System": platform.system(),
                "Node Name": platform.node(),
                "Release": platform.release(),
                "Version": platform.version(),
                "Machine": platform.machine(),
                "Processor": platform.processor(),
                "Architecture": platform.architecture(),
                "Python Version": platform.python_version(),
                "Python Implementation": platform.python_implementation(),
                "Python Compiler": platform.python_compiler(),
                "Python Build": platform.python_build(),
                "OS Environment Variables": dict(os.environ),
                "User Home": os.path.expanduser('~'),
            }
        except Exception as e:
            call_error_api(f"Error gathering basic OS info: {str(e)}", "")
            os_info = {}

        # The OSEnvironmentDetector adds more detailed information based on the OS
        try:
            if os_info.get("System", "").lower() == "linux":
                os_info.update({
                    "Linux Distribution Name": distro.name(),
                    "Linux Distribution Version": distro.version(),
                    "Linux Distribution ID": distro.id(),
                    "Linux Distribution Codename": distro.codename(),
                    "Linux Distribution Like": distro.like(),
                    "Package Managers": {
                        "apt": self._get_version("apt"),
                        "yum": self._get_version("yum"),
                        "dnf": self._get_version("dnf"),
                        "pacman": self._get_version("pacman"),
                        "zypper": self._get_version("zypper"),
                    },
                })
            elif os_info.get("System", "").lower() == "darwin":
                os_info.update({
                    "macOS Version": platform.mac_ver()[0],
                    "Xcode Command Line Tools": self._get_xcode_cli_tools_version(),
                })
            elif os_info.get("System", "").lower() == "windows":
                os_info.update({
                    "Windows Version": platform.win32_ver()[0],
                    "PowerShell Version": self._get_powershell_version(),
                    "Chocolatey": self._get_version("choco"),
                    "Scoop": self._check_scoop_installed(),
                })
        except Exception as e:
            call_error_api(f"Error gathering OS-specific info: {str(e)}", "")

        # The OSEnvironmentDetector adds information about common package managers and development tools
        try:
            os_info.update({
                "Package Managers": {
                    "pip": self._get_version("pip"),
                    "npm": self._get_version("npm"),
                    "yarn": self._get_version("yarn"),
                    "pnpm": self._get_version("pnpm"),
                    "brew": self._get_version("brew"),
                    "conda": self._get_version("conda"),
                    "poetry": self._get_version("poetry"),
                    "cargo": self._get_version("cargo"),
                    "gem": self._get_version("gem"),
                    "composer": self._get_version("composer"),
                },
                "Development Tools": {
                    "git": self._get_version("git"),
                    "docker": self._get_version("docker"),
                    "kubectl": self._get_version("kubectl"),
                    "terraform": self._get_version("terraform"),
                    "ansible": self._get_version("ansible"),
                    "vagrant": self._get_version("vagrant"),
                },
                "Build Tools": {
                    "make": self._get_version("make"),
                    "cmake": self._get_version("cmake"),
                    "gradle": self._get_version("gradle"),
                    "maven": self._get_version("mvn"),
                },
            })
        except Exception as e:
            call_error_api(f"Error gathering tool versions: {str(e)}", "")

        # The OSEnvironmentDetector removes None values
        try:
            os_info["Package Managers"] = {k: v for k, v in os_info.get("Package Managers", {}).items() if v is not None}
            os_info["Development Tools"] = {k: v for k, v in os_info.get("Development Tools", {}).items() if v is not None}
            os_info["Build Tools"] = {k: v for k, v in os_info.get("Build Tools", {}).items() if v is not None}
        except Exception as e:
            call_error_api(f"Error cleaning up None values: {str(e)}", "")

        return os_info

    def _get_version(self, command):
        """Generic method to get version of a command-line tool."""
        try:
            result = subprocess.run([command, "--version"], capture_output=True, text=True, timeout=5)
            return result.stdout.strip() if result.returncode == 0 else None
        except Exception as e:
            call_error_api(f"Error getting version for {command}: {str(e)}", "")
            return None

    def _get_xcode_cli_tools_version(self):
        """Get Xcode Command Line Tools version on macOS."""
        try:
            result = subprocess.run(["xcode-select", "--version"], capture_output=True, text=True, timeout=5)
            return result.stdout.strip() if result.returncode == 0 else None
        except Exception as e:
            call_error_api(f"Error getting Xcode CLI Tools version: {str(e)}", "")
            return None

    def _get_powershell_version(self):
        """Get PowerShell version on Windows."""
        try:
            result = subprocess.run(["powershell", "$PSVersionTable.PSVersion"], capture_output=True, text=True, timeout=5)
            return result.stdout.strip() if result.returncode == 0 else None
        except Exception as e:
            call_error_api(f"Error getting PowerShell version: {str(e)}", "")
            return None

    def _check_scoop_installed(self):
        """Check if Scoop is installed on Windows."""
        try:
            return "Installed" if shutil.which("scoop") else None
        except Exception as e:
            call_error_api(f"Error checking Scoop installation: {str(e)}", "")
            return None

    def get_os_info(self):
        """
        The OSEnvironmentDetector returns a dictionary with detailed OS information.
        """
        return self.os_data

    def get_all_info(self):
        """
        A function to return all necessary OS information in one call.
        """
        return self.get_os_info()

    def __str__(self):
        """
        The OSEnvironmentDetector returns a formatted string of the OS information.
        """
        try:
            os_info = self.get_all_info()
            return '\n'.join([f'{key}: {value}' for key, value in os_info.items()])
        except Exception as e:
            call_error_api(f"Error formatting OS info: {str(e)}", "")
            return "Error formatting OS information"

# Example usage:
if __name__ == "__main__":
    try:
        detector = OSEnvironmentDetector()
        print(detector.get_all_info())  # Call to get all info in a dictionary
        print("\nFormatted Output:\n")
        print(detector)  # To print formatted OS info
    except Exception as e:
        call_error_api(f"Error in main execution: {str(e)}", "")
