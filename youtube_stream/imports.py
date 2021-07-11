import pathlib
HERE = pathlib.Path(__file__).parent
ascii_art = open(HERE / "ascii_art.txt", encoding="utf8")
config_file = (HERE / "config.txt").read_text()