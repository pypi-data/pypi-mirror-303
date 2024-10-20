# setup.py
from setuptools import setup, find_packages

setup(
    name='rocket_ss',  # Replace with your package name
    version='0.1.0',  # Replace with your package version
    author='Said Senhadji',  # Replace with your name
    author_email='ms.senhadji@esi-sba.com',  # Replace with your email
    description='A package for simulating rockets and shuttles',
    packages=find_packages(),  # Automatically find packages in the directory
    license='MIT',  # License type
    url='https://github.com/SenhadjiMSaid',  # Replace with your repo URL if applicable
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
