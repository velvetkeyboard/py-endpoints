from setuptools import setup, find_packages
from endpoints import (
        __version__,
        __author__,
        __author_email__,
        __license__,
        __app_name__,
        __description__,
        __long_description__,
    )


setup(
    name=__app_name__,
    version=__version__,
    url='https://gitlab.com/velvetkeyboad/py-endpoints',
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    description=__description__,
    long_description=__long_description__,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.0.0',
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: GTK',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
