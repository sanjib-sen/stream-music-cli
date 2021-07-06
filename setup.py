import pathlib
from setuptools import find_packages, setup
from _version import __version__

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="youtube_stream",
    version=__version__,
    description="Stream Youtube Music Videos in Local Media Player (Currently VLC) using Command Line!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sanjib-sen/youtube_stream",
    author="Sanjib Kumar Sen",
    author_email="sksenonline@gmail.com",
    license="MIT",
    keywords = ['youtube', 'streaming', 'vlc', 'video', 'audio', 'automation'],
    download_url = 'https://github.com/sanjib-sen/youtube-stream/archive/v_0.0.4.tar.gz',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Home Automation",
        "Topic :: Multimedia :: Video :: Display",

    ],
    packages=find_packages(exclude=("tests",)),
    package_dir={'youtube_stream': 'youtube_stream'},
    package_data={'youtube_stream': ['*.txt']},
    include_package_data=True,
    install_requires=["SpeechRecognition"],
    entry_points={
        "console_scripts": [
            "stream=youtube_stream.__main__:main",
        ]
    },
)