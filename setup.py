from setuptools import setup

setup(
    name='dice',
    packages=['module'],
    entry_points={
        'console_scripts' : [
            'roll = modules.dice:main',
        ]
    },
    install_requires=[
        'termcolor',
        'sys',
        'random2',
    ]
)