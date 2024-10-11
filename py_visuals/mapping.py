import numpy as np 
import os
import sys
import time


def extract(map: Map, first_corner: tuple, second_corner: tuple) -> np.array:
	new_map: np.array = np.array([['0'] * (second_corner[0] - first_corner[0])] * (second_corner[1] - first_corner[1]))
	for i in range(first_corner[0], second_corner[0]):
		for j in range(first_corner[1], second_corner[1]):
			new_map[i - first_corner[0], j - first_corner[1]] = map.map[i, j]

	return new_map


class Map:
	def __init__(self, x_size: int, y_size: int):
		x_array: list = ['0'] * x_size
		y_array: list = [x_array] * y_size

		self.map: np.array = np.array(y_array)

	def load(self, object_file: str) -> int:
		with open(object_file, 'r') as obj:
			lines: list = obj.readlines()

			if len(lines) > self.map.shape[1]:
				return 1

			for line_index in range(1, len(lines)):
				if len(lines[line_index]) != len(lines[line_index - 1]):
					return 1

				if len(lines[line_index]) > self.map.shape[0]:
					return 1

			for i in range(len(lines)):
				new_line: list = [j for j in lines[i]]
				lines[i] = new_line

			self.map = np.array(lines)
			return 0

	def display(self) -> int:
		for i in range(self.map.shape[0]):
			for j in range(self.map.shape[1]):
				sys.stdout.write(self.map[i, j])
			sys.stdout.flush()


class MapFromArray(Map):
	def __init__(self, map: np.array):
		self.map: np.array = map


class Animation:
	def __init__(self, height: int, width: int, folder: str):
		self.height: int = height
		self.width: int = width
		self.folder: str = folder.split("/")[1]
		self.frames: list = []

	def load_animation(self) -> None:
		dir_content: list = os.listdir(self.folder)
		dir_content = [f"{self.folder}/{i}" for i in dir_content]
		self.frames = [Map(self.width, self.height) for i in range(len(dir_content))]
		for i in range(len(self.frames)):
			success: int = self.frames[i].load(dir_content[i])
			if success == 1:
				sys.exit("Invalid size")
