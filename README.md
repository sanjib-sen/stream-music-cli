# Youtube Stream

## Requirements

- [VLC](https://www.videolan.org/)

## Installation and Usage

### Windows

#### Easy Method (App)

1. Download and Install [VLC](https://www.videolan.org/)
2. Download [youtube-stream.exe](https://github.com/sanjib-sen/youtube-stream/releases/download/0.08/winows.exe)
3. Run **youtube-stream.exe**

#### Recommended Method (Console)

1. Download and Install [VLC](https://www.videolan.org/)
2. Download and Install [Python](https://www.python.org/downloads/release/python-396/). **(Mark Add Python to Path while installation)**
3. Open `Command Prompt` or  `Powershell` and Run:

  ```bash
  python -m pip install youtube-stream
  ```

### Linux

#### Ubuntu, Debian, Linux-Mint, Pop-OS, MX-Linux

> From command line, run:

```bash
sudo apt install vlc python3 python3-pip && sudo pip install -U youtube-stream
```

#### Fedora, OpenSuse, RedHat

> From command line, run:

```bash
sudo dnf install vlc python3 python3-pip && sudo pip install -U youtube-stream
```

#### Arch Linux

> From command line, run:

```bash
sudo pacman -Syu vlc python3 python3-pip && sudo pip install -U youtube-stream
```

## Usage (From Console)

### Text Search

  > Run from command line (Powershell/Bash/CMD/zsh/fish)

  ```bash
  stream <song name>
  ```

  > e.g. To Play Journey's Don't Stop Believing
  
  ``` bash
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
