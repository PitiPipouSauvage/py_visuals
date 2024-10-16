import os
import sys

from py_visuals import mapping
from py_visuals import screen_manager as sm


def init(texture_folder: str, animations_folder: str, height: int, width: int, resolution=1) -> sm.Screen:
	animations: dict = {}
	textures: dict = {}
	loading_sequence = ["-", "\\", "|", "/"]
	logo = """
.----..-.  .-..-. .-..-. .----..-. .-.  .--.  .-.    .----.
| {}  }\\ \\/ / | | | || |{ {__  | { } | / {} \\ | |   { {__  
| .--'  }  {  \\ \\_/ /| |.-._} }| {_} |/  /\\  \\| `--..-._} }
`-'     `--'   `---' `-'`----' `-----'`-'  `-'`----'`----' 

	"""

	loading_phase: int = 0
	sys.stdout.write("Powered by\n")
	sys.stdout.write(logo)
	sys.stdout.flush()

	screen = sm.Screen(height, width, resolution)

	if animations_folder != None:
		for i in range(len(os.listdir(animations_folder))):
			screen.clear()
			screen.blit()
			sm.move_cursor(loading_phase, 0)
			
			sys.stdout.write(f"Loading animations {loading_sequence[i % 4]} \n")
			sys.stdout.flush()
			animation = mapping.Animation(height, width, f"{animations_folder}/{os.listdir(animations_folder)[i]}")
			animation.load_animation()
			animations[os.listdir()[i]] = animation 

		loading_phase += 1

	if texture_folder != None:
		for i in range(len(os.listdir(texture_folder))):
			screen.clear()
			screen.blit()
			sm.move_cursor(loading_phase, 0)
			sys.stdout.write(f"Loading textures {loading_sequence[i % 4]} \n")
			sys.stdout.flush()

			map = mapping.Map()
			map.load(os.listdir(texture_folder)[i])
			textures[os.listdir(texture_folder)[i]] = map


	return screen
	
