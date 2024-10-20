from setuptools import setup, find_packages

setup(
    name="TurboTalk",
    version="0.1.3",  # Increment the version number
    packages=find_packages(),
    install_requires=[
        "g4f",
        "colorama",
    ],
)
