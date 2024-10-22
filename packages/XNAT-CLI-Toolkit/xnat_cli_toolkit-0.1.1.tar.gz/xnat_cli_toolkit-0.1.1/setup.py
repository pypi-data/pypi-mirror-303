import sys
import os.path
from setuptools import setup, find_packages

PKG_NAME = 'XNAT_CLI_Toolkit'

# Extract version number from module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), PKG_NAME))
sys.path.pop(0)

setup(
    name=PKG_NAME,
    author='Rahul Rajput',
    author_email='rahul.rajput@proxmed.com.au',
    version='0.1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['xnat-share = XNAT_CLI_Toolkit:share_subjects',
                            'xnat-upload = XNAT_CLI_Toolkit:upload_and_archive',
                            'xnat-list = XNAT_CLI_Toolkit:list_projects',
                            'xnat-toolkit = XNAT_CLI_Toolkit:list_commands',
                            'xnat-prearchive = XNAT_CLI_Toolkit:upload_to_prearchive',
                            'xnat-archive = XNAT_CLI_Toolkit:archive_to_xnat',
                            'xnat-updatedemographics = XNAT_CLI_Toolkit:update_demographics',
                            'xnat-authenticate = XNAT_CLI_Toolkit:store'
                            ],
        },
    url='',
    license='The MIT License (MIT)',
    description=(
        'A collection of scripts for sharing/uploading and listing '
        'data from XNAT repositories.'),
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    install_requires=['xnat>=0.6',
                      'progressbar2>=3.16.0',
                      'future>=0.16'],
    python_requires='>=3.4',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps."])