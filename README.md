# virtual-school-bell
a basic Python script to play a sound at a designated time.

## getting started
### Windows
1. install Python 3.7+ (to check which version you have, run `python --version`)
2. install `ffmpeg` (use [this tutorial](https://www.wikihow.com/Install-FFmpeg-on-Windows) to install it)
3. (optional, only if you want to manually invoke the bell) install `keyboard` with `pip` (`python -m pip install keyboard`)

### Linux
1. install Python 3.7+ (to check which version you have, run `python3 --version`)
2. install `ffmpeg` (`sudo apt-get install ffmpeg` or `pacman -S ffmpeg`, depends on your package manager)
3. (optional, only if you want to manually invoke the bell) install `keyboard` with `pip` (`python3 -m pip install keyboard`)

## configuration
put in sections into `hours.ini` in the following format:
```ini
[hour]
SoundPath=<PATH_TO_SOUND_FILE>
```
where:
- `[hour]` is the time in a 24-hour format (e.g. `[13:15]`)
- `SoundPath` is the path to the sound file to play (e.g. `SoundPath=sounds/default.wav`)

## running
to run it, just do it regularily, with `python main.py` (or `python3 main.py`)

if you want to run it in the background, you can use `nohup python3 main.py` (linux only)