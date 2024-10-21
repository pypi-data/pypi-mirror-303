from setuptools import setup, find_packages

setup(
    name="wavefront_package",
    version="1.0.0",
    packages = find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'opencv-python',
    ],
    entry_points = {
        'console_scripts': [
            'wavefront_5 = wavefront_package.wavefront_5_pac:main',
            
        ],
    },
)