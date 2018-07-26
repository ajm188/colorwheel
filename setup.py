from setuptools import find_packages
from setuptools import setup


setup(
    name='colorwheel',
    version='0.0.1',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
    ],
    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={
        'console_scripts': [
            'colorwheel = colorwheel.main:main',
        ],
    },
)
