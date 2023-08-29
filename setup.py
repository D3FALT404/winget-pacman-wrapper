from setuptools import setup

setup(
    name='pacman',
    version='0.1.0',
    py_modules=['pacman'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'pacman = pacman:cli',
        ],
    },
)