from setuptools import setup, find_packages

setup(
    name='flightmatrixbridge',
    version='1.3.1',
    license="MIT License with attribution requirement",
    author="Ranit Bhowmick",
    author_email='bhowmickranitking@duck.com',
    description='''FlightMatrixBridge is a Python library that facilitates seamless inter-process communication between the Flight Matrix software using shared memory. It handles frames, timestamps, and movement commands for efficient data sharing in robotics applications.''',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Kawai-Senpai/Py-FlightMatrix-Bridge',
    download_url='https://github.com/Kawai-Senpai/Py-FlightMatrix-Bridge',
    keywords=["Robotics", "Inter-process communication", "Shared memory", "Data management"],
    install_requires=[
        'numpy',  # Include numpy as a dependency since it's used in the code
        'ultraprint',  # Include ultraprint as a dependency since it's used in the code
        'opencv-python',  # Include opencv-python as a dependency since it's used in the code
    ],
)
