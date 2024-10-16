import numpy as np
import sys

from py_visuals import mapping


def move_cursor(row, column):
	sys.stdout.write(f"\033[{row};{column}H")
	sys.stdout.flush()


class Screen:
	def __init__(self, height: int, width: int, resolution=1):
		self.height = height
		self.width = width
		self.resolution = resolution
		self.screen_matrix: np.array = np.array([[' '] * self.width * resolution] * self.height * resolution)
		self.textures = {}
		self.animations = {}

	def clear(self) -> None:
		self.screen_matrix: np.array = np.array([[' '] * self.width] * self.height)

	@staticmethod
	def superimpose(self, base: np.array, overlay: np.array, x_coord=0, y_coord=0) -> None:
		for i in range(overlay.shape[1]):
			for j in range(overlay.shape[0]):
				base[j + x_coord, i + y_coord] = overlay[j, i]		

	def generate_screen(self, nb_layers: int, layers: list[tuple[tuple]]) -> np.array:
		self.clear()
		for layer in layers:
			self.superimpose(self.screen_matrix, layer[0], layer[1][0], layer[1][1])
		return self.screen_matrix

	def blit(self):
		map: mapping.MapFromArray = mapping.MapFromArray(self.screen_matrix)
		move_cursor(0, 0)
		map.display()
