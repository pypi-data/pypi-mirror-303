from setuptools import setup, find_packages


VERSION = '0.0.148'
DESCRIPTION = 'Youtube Autónomo Multimedia Module is here.'
LONG_DESCRIPTION = 'These are all the multimedia utils we need in the Youtube Autónomo project to work in a better way. This module includes audio, image and video generation and editing utilities.'

setup(
        name = "yta-multimedia", 
        version = VERSION,
        author = "Daniel Alcalá",
        author_email = "<danielalcalavalera@gmail.com>",
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        packages = find_packages(),
        install_requires = [
            # Audio module
            'pyttsx3',
            'gtts',
            'pydub',
            'pedalboard',
            'spleeter'
            # Image module
            # Video module
        ],
        
        keywords = [
            'youtube autonomo multimedia utils module'
        ],
        classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)