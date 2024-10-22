#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = (
    [
        "auro_utils==0.0.7",
        "evdev",
    ],
)


test_requirements = [
    "pytest>=3",
]

setup(
    author="Herman Ye",
    author_email="hermanye233@icloud.com",
    license="Apache License 2.0",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description="Auro Joystick is a Python library designed for interfacing with joystick devices in robotics applications, offering robust support for ROS to facilitate easy integration.",
    install_requires=requirements,
    include_package_data=True,
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="auro_joystick",
    name="auro_joystick",
    packages=find_packages(include=["auro_joystick", "auro_joystick.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Auromix/auro_joystick",
    version="1.0.2",
    zip_safe=False,
)
