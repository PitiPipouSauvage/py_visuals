import mapping
import os
import screen_manager as sm
import sys


loading_sequence = ["-", "\\", "|", "/"]


def init(animations_folder: str) -> int:
	animations: dict = {}

	try:
		width = int(sys.argv[1])
		height = int(sys.argv[2])

	except IndexError:
		width = 500
		height = 400

	for i in range(len(os.listdir(animations_folder))):
		sm.move_cursor(0, 0)
		sys.stdout.write(f"Loading animations {loading_sequence[i % 4]} \n")
		sys.stdout.flush()
		animation = mapping.Animation(height, width, f"{animations_folder}{os.listdir(animations_folder)[i]}")
		animation.load_animation()
		animations[os.listdir()[i]] = animation 
	
	return 0
