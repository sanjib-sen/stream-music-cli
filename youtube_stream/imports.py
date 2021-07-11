# import pathlib
from importlib import resources

# HERE = pathlib.Path(__file__).parent
# ascii_art = open(HERE / "ascii_art.txt", encoding="utf8")
# config_file = (HERE / "config.txt").read_text()

ascii_art = resources.read_text("youtube_stream", "ascii_art.txt")
config_file = resources.read_text("youtube_stream", "config.txt")

