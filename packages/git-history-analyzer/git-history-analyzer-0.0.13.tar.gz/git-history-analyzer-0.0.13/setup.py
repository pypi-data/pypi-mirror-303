import os
import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

# Get version from environment variable or fallback to a default value
version = os.getenv("PACKAGE_VERSION", "0.0.7")  # Default to '0.0.7' if not provided

setuptools.setup(
    name="git-history-analyzer",
    version=version,  # Use the dynamic version from the environment variable
    author="Jorge Cardona",
    description="Generate Reports from Your Repository's Git History",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jorgecardona/git-history-analyzer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
