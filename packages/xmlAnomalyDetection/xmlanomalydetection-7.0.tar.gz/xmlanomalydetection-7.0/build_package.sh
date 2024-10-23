#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Clean previous builds
echo "Cleaning up old builds..."
rm -rf build/ dist/ xmlAnomalyDetection.egg-info/

# Build the package
echo "Building the package..."
python3 setup.py sdist bdist_wheel

# Check if twine is installed
if ! command -v twine &> /dev/null
then
    echo "twine could not be found, installing..."
    pip install twine
fi

# Push to PyPI
echo "Uploading the package to PyPI..."
twine upload dist/*

# Done
echo "Package uploaded successfully!"

