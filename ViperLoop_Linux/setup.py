from setuptools import setup

setup(
    name='viperloop',
    version='1.0.0',
    packages=['viperloop'],
    entry_points={
        'console_scripts': [
            'viperloop = viperloop.network_dns:main'
        ]
    },
    install_requires=[
        'colorama',
        'psutil',
        'netifaces'
    ]
)
