from setuptools import setup, find_packages
import os

# Get the project path (where setup.py is located)
project_path = os.path.dirname(os.path.abspath(__file__))

# Define the paths for the .pyd files for Python 3.11 and 3.12
pyd_files = []
if os.path.exists(os.path.join(project_path, 'geosh', 'cy_theoretical_dc.cp311-win_amd64.pyd')):
    pyd_files.append('geosh/cy_theoretical_dc.cp311-win_amd64.pyd')
if os.path.exists(os.path.join(project_path, 'geosh', 'cy_theoretical_dc.cp312-win_amd64.pyd')):
    pyd_files.append('geosh/cy_theoretical_dc.cp312-win_amd64.pyd')

# Read the long description from README.md
with open(os.path.join(project_path, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setup the package
setup(
    name="geosh",  # The name of the package
    version="0.1.9",  # Version number; update as needed
    author="Umberto Grechi",
    author_email="umberto.grechi@sofhare.com",
    description="Library and dependency for Geo Utilities Plugin",  # Short description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Adre17/geosh",  # URL to your repository
    packages=find_packages(),  # Automatically find and include sub-packages
    classifiers=[  # Classifiers for PyPI
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11, <3.13",  # Specify supported Python versions
    install_requires=[  # Dependencies to be installed
        'xlrd',
        'pyproj',
        'numpy',
        'shapely',
        'matplotlib',
        'Pillow',
        'psycopg2',
        'reportlab',
        'segyio',
        'opencv-python',
        'openpyxl',
        'opencv-contrib-python'
    ],
    # Include the compiled .pyd files
    data_files=pyd_files,
)



