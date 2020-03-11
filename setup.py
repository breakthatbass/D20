from setuptools import setup

setup(
    name='dice',
    packages=['modules'],
    entry_points={
        'console_scripts' : [
            'roll = modules.dice:main',
        ]
    },
    install_requires=[
        'termcolor',
        'random2',
    ]
)