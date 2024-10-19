from setuptools import setup, find_packages

setup(
    name="qdev",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    description="An AI powered cli to make setting up a development environment fast and efficient.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my-cli-tool",  # Your project URL
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "q=qdev.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
