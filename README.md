# Youtube Stream

![image](https://raw.githubusercontent.com/sanjib-sen/youtube-stream/master/screenshots/windows.png)

![MadeBy](https://img.shields.io/badge/Made%20By-Sanjib--Sen-blueviolet?style=for-the-badge) ![GitHub followers](https://img.shields.io/github/followers/sanjib-sen?style=for-the-badge) ![GitHub User's stars](https://img.shields.io/github/stars/sanjib-sen?style=for-the-badge) ![LICENSE](https://img.shields.io/github/license/sanjib-sen/youtube-stream?style=for-the-badge) ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/sanjib-sen/youtube-stream?include_prereleases&style=for-the-badge) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/sanjib-sen/youtube-stream?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/sanjib-sen/youtube-stream?style=for-the-badge) ![PyPI - Status](https://img.shields.io/pypi/status/youtube-stream?style=for-the-badge) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/youtube-stream?style=for-the-badge) ![PyPI](https://img.shields.io/pypi/v/youtube-stream?style=for-the-badge)

---

youtube-stream is a console app for streaming videos quickly from Youtube. Suppose you are working on something and don't have the feeling for opening up youtube, search for the song and play it. It is also a bit more troublesome for playing multiple songs from youtube. That's why I have made a module from where you can listen and watch your favourite songs as quickly as possible. Even there is a voice search option for lazy typists. Using this app, you can stream/play multiple videos/musics at once with a single command. e.g. `stream the reason, aurora runaway` will add Hoobastank's Reason and Aurora's Runaway song in your vlc playlist and play them one after another.

---

## Requirements

-   [VLC](https://www.videolan.org/)

---

## Installation

### Windows

#### Easy Method (App)

1. Download and Install [VLC](https://www.videolan.org/)
2. Download [youtube-stream.exe](https://github.com/sanjib-sen/youtube-stream/releases/download/0.13/youtube-stream.exe)
3. Run **youtube-stream.exe**

#### Recommended Method (Console)

1. Download and Install [VLC](https://www.videolan.org/)
2. Download and Install [Python](https://www.python.org/downloads/release/python-396/). **(Mark Add Python to Path while installation)** and [pip](https://phoenixnap.com/kb/install-pip-windows)
3. Open `Command Prompt` or `Powershell` and Run:

```bash
python -m pip install youtube-stream
```

### Linux

#### Ubuntu, Debian, Linux-Mint, Pop-OS, MX-Linux

> From command line, run:

```bash
sudo apt install vlc python3 python3-pip && pip install -U youtube-stream
```

#### Fedora, OpenSuse, RedHat

> From command line, run:

```bash
sudo dnf install vlc python3 python3-pip && pip install -U youtube-stream
```

#### Arch Linux, Manjaro, EndeavourOS

> From command line, run:

```bash
sudo pacman -Syu vlc python3 python3-pip && pip install -U youtube-stream
```

---

## Usage (From Console)

### Text Search

> Run from command line (Powershell/Bash/CMD/zsh/fish)

```bash
stream <song name>
```

> e.g. To Play Journey's Don't Stop Believing

```bash
stream Journey dont stop believing
```

> For multiple songs use comma `(,)` after each song

```bash
stream <song name>, <song name>, <song name>
```

> e.g. To Play Passenger's Let her go, Hoobastank's The Reason, Majhe Majhe tobo dekha pai by arnob

```txt
stream let her go, the reason hoobastank, majhe majhe tobo arnob
```

### Voice Search (Only English)

> Run from command line (Powershell/Bash/CMD/zsh/fish)

```bash
stream
```

Now speak the song name. e.g. Hello by adele

> For multiple songs, say `then` or `plus` after saying each song name

e.g iridescent linkin park then yellow coldplay

### Enjoy

---

## Upcoming

1. Support for Downloading Videos in High Quality
2. Support for other media players e.g. MPV, KMP etc.

---
