import subprocess
import sys

class PackageManager:
    """
    This class is designed to manage Python packages.
    It can check if a package is installed and install a package if needed.
    """
    def __init__(self):
        """
        Initializes the PackageManager object.
        The executable attribute is set to the current Python executable.
        """
        self.executable = sys.executable

    def is_package_installed(self, package_name):
        """
        Checks if a specific package is installed in the current Python environment.

        Parameters:
        package_name (str): The name of the package to check.

        Returns:
        bool: True if the package is installed, False otherwise.
        """
        try:
            __import__(package_name)
            return True
        except ImportError:
            return False

    def install_package(self, package_name):
        """
        Installs a specific package in the current Python environment.

        Parameters:
        package_name (str): The name of the package to install.

        Returns:
        None: This function does not return a value but it installs the package.
        """
        subprocess.check_call([self.executable, "-m", "pip", "install", package_name])
