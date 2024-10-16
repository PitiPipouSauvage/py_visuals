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
		self.screen_matrix: np.array = np.array([[' '] * (self.width * resolution) for _ in range(self.height * resolution)])
		self.textures = {}
		self.animations = {}

	def clear(self) -> None:
		self.screen_matrix: np.array = np.array([[' '] * self.width for _ in range(self.height)])

	@staticmethod
	def superimpose(base: np.array, overlay: mapping.Map, x_coord=0, y_coord=0) -> None:
		for i in range(overlay.map.shape[0]):
			for j in range(overlay.map.shape[1]):
				base[j + x_coord, i + y_coord] = overlay.map[i, j]		

	def generate_screen(self, nb_layers: int, layers: list[tuple[tuple]]) -> np.array:
		self.clear()
		for layer in layers:
			self.superimpose(self.screen_matrix, layer[0], layer[1][0], layer[1][1])
		return self.screen_matrix

	def blit(self):
		map: mapping.MapFromArray = mapping.MapFromArray(self.screen_matrix)
		move_cursor(0, 0)
		map.display()
