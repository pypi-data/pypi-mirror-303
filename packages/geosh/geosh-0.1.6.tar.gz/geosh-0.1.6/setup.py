from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy as np
import os

# Get the project path (where setup.py is located)
project_path = os.path.dirname(os.path.abspath(__file__))

# Define an extension that includes your Cython file
extensions = [
    Extension(
        "geosh.cy_theoretical_dc",  # Update to match the package name
        [os.path.join(project_path, "geosh", "cy_theoretical_dc.pyx")],  # Cython source file path
        include_dirs=[np.get_include()],  # Include NumPy headers
    )
]

# Read the long description from README.md
with open(os.path.join(project_path, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setup the package
setup(
    name="geosh",  # The name of the package
    version="0.1.6",  # Version number; update as needed
    author="Umberto Grechi",
    author_email="umberto.grechi@sofhare.com",
    description="Library and dependency for Geo Utilities Plugin",  # Short description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Adre17/geosh",  # URL to your repository
    packages=find_packages(),  # Automatically find and include sub-packages
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),  # Include Cython extensions
    classifiers=[  # Classifiers for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6, <3.13",  # Specify supported Python versions
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
)


