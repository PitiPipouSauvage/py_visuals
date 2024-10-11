import os
import sys

from py_visuals import mapping
from py_visuals import screen_manager as sm


def init(animations_folder: str, height: int, width: int, resolution=1) -> sm.Screen:
	animations: dict = {}
	loading_sequence = ["-", "\\", "|", "/"]
	logo = """
.----..-.  .-..-. .-..-. .----..-. .-.  .--.  .-.    .----.
| {}  }\\ \\/ / | | | || |{ {__  | { } | / {} \\ | |   { {__  
| .--'  }  {  \\ \\_/ /| |.-._} }| {_} |/  /\\  \\| `--..-._} }
`-'     `--'   `---' `-'`----' `-----'`-'  `-'`----'`----' 

	"""


	for i in range(len(os.listdir(animations_folder))):
		screen = sm.Screen(height, width, resolution)
		screen.clear()
		screen.blit()
		sm.move_cursor(0, 0)
		
		sys.stdout.write(f"Loading animations {loading_sequence[i % 4]} \n")
		sys.stdout.flush()
		animation = mapping.Animation(height, width, f"{animations_folder}/{os.listdir(animations_folder)[i]}")
		animation.load_animation()
		animations[os.listdir()[i]] = animation 

	sys.stdout.write("Powered by\n")
	sys.stdout.write(logo)
	sys.stdout.flush()
	return screen
