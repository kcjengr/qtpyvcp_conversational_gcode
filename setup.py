from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("entry_points.ini", "r") as fh:
    entry_points = fh.read()

setup(
    name="qtpyvcp.conversational_gcode",
    version="0.0.1",
    author="Aaron Dargel",
    author_email="",
    description="QtPyVCP Conversation G-code generator widgets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kcjengr/qtpyvcp.conversational-gcode",
    download_url="https://github.com/kcjengr/qtpyvcp.conversational-gcode/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points
)
