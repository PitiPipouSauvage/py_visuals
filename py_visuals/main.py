import os
import sys
import time

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

	sys.stdout.write("Powered by\n")
	sys.stdout.write(logo)
	sys.stdout.flush()
	time.sleep(5)

	screen = sm.Screen(height, width, resolution)

	if animations_folder != None:
		for i in range(len(os.listdir(animations_folder))):
			screen.clear()
			screen.blit()
			sm.move_cursor(0, 0)
			
			sys.stdout.write(f"Loading animations {loading_sequence[i % 4]} \n")
			sys.stdout.flush()
			animation = mapping.Animation(height, width, f"{animations_folder}/{os.listdir(animations_folder)[i]}")
			animation.load_animation()
			animations[os.listdir()[i]] = animation 


	if texture_folder != None:
		for i in range(len(os.listdir(texture_folder))):
			screen.clear()
			screen.blit()
			sm.move_cursor(0, 0)
			sys.stdout.write(f"Loading textures {loading_sequence[i % 4]} \n")
			sys.stdout.flush()

			text_map: mapping.Map = mapping.Map(height, width)
			result = text_map.load(f"{texture_folder}/{os.listdir(texture_folder)[i]}")
			if result == 1:
				sys.exit("1")
			elif result == 2:
				sys.exit("2")
			elif result == 3:
				sys.exit("3")
			textures[os.listdir(texture_folder)[i]] = text_map

	screen.textures = textures
	screen.animations = animations

	return screen
	
