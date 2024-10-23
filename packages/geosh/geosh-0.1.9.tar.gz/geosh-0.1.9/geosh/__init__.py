import sys
import os

# Determine the Python version
python_version = sys.version_info

# Set the path to the .pyd files
project_path = os.path.dirname(os.path.abspath(__file__))

# Initialize the module variable
cy_theoretical_dc = None

# Check for the appropriate .pyd file based on Python version
if python_version.major == 3 and python_version.minor == 11:
    pyd_file = 'cy_theoretical_dc.cp311-win_amd64.pyd'
elif python_version.major == 3 and python_version.minor == 12:
    pyd_file = 'cy_theoretical_dc.cp312-win_amd64.pyd'
else:
    raise ImportError("This package only supports Python 3.11 and 3.12.")

# Import the .pyd file dynamically
try:
    cy_theoretical_dc = __import__(f"geosh.{pyd_file[:-4]}", fromlist=['*'])  # Remove the .pyd extension
except ImportError as e:
    raise ImportError(f"Failed to import {pyd_file}: {e}")

# You can expose the imported module for easier access
# This will allow you to do `from geosh import cy_theoretical_dc` in your scripts
# Note: This assumes your pyd file exports the functions and classes you want to use