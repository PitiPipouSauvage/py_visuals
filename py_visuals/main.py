import mapping
import os
import screen_manager as sm
import sys


def init(animations_folder: str, height: int, width: int, resolution=1) -> sm.Screen:
	animations: dict = {}
	loading_sequence = ["-", "\\", "|", "/"]


	for i in range(len(os.listdir(animations_folder))):
		sm.move_cursor(0, 0)
		sys.stdout.write(f"Loading animations {loading_sequence[i % 4]} \n")
		sys.stdout.flush()
		animation = mapping.Animation(height, width, f"{animations_folder}{os.listdir(animations_folder)[i]}")
		animation.load_animation()
		animations[os.listdir()[i]] = animation 

	screen = sm.Screen(height, width, resolution)
	return screen
