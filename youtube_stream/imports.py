import pathlib
HERE = pathlib.Path(__file__).parent.parent
ascii_art = (HERE / "ascii_art.txt").read_text()
config_file = (HERE / "config.txt").read_text()