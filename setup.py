#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

test_requirements = requirements

setup(
    author="Patrick Roy Christie",
    author_email='patrick.christie.dev@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Core runner for Spotify Playlist Additions. Where all the magic happens",
    entry_points={
        'console_scripts': [
            'spotify_playlist_additions_core=spotify_playlist_additions_core.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='spotify_playlist_additions_core',
    name='spotify_playlist_additions_core',
    packages=find_packages(include=['spotify_playlist_additions_core', 'spotify_playlist_additions_core.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/prchristie/spotify-playlist-additions-core',
    version='0.1.8',
    zip_safe=False,
)
