from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
                     'SQLAlchemy<=1.3.15',
                     'pg8000>=1.16.6',
                     'beam-nuggets',
                     'workflow'  # Include this line
                    ]

setup(
    name='beamNuggetsDependencies',
    version='0.5',
    description='Dependencies',
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES
)