import numpy as np 
import os
import sys
import time


class Map:
	def __init__(self, x_size: int, y_size: int):
		self.map: np.array = np.array([['0'] * x_size for _ in range(y_size)])

	def load(self, object_file: str) -> int:
		with open(object_file, 'r') as obj:
			lines: list = [line.strip() for line in obj.readlines()]

			if len(lines) > self.map.shape[0]:
				return 1

			for line_index in range(1, len(lines)):
				if len(lines[line_index]) != len(lines[line_index - 1]):

					if len(lines[line_index]) > len(lines[line_index - 1]):
						lines[line_index] += ' ' * (len(lines[line_index]) - len(lines[line_index - 1]))
					else:
						lines[line_index] += ' ' * (len(lines[line_index - 1]) - len(lines[line_index]))
			for line in lines:
				print(line)

			if len(lines[line_index]) > self.map.shape[1]:
				return 3

			for i in range(len(lines)):
				new_line: list = list(lines[i])
				lines[i] = new_line

			self.map = np.array(lines)
			return 0

	def display(self) -> int:
		for i in range(self.map.shape[1]):
			for j in range(self.map.shape[0]):
				sys.stdout.write(self.map[j, i])
			sys.stdout.flush('\n')
		sys.stdout.flush()


class MapFromArray(Map):
	def __init__(self, map: np.array):
		self.map: np.array = map


class Animation:
	def __init__(self, height: int, width: int, folder: str):
		self.height: int = height
		self.width: int = width
		self.frames: list = []
		self.folder = folder

	def load_animation(self) -> None:
		dir_content: list = os.listdir(self.folder)
		dir_content = [f"{self.folder}/{i}" for i in dir_content]
		self.frames = [Map(self.width, self.height) for i in range(len(dir_content))]
		for i in range(len(self.frames)):
			success: int = self.frames[i].load(dir_content[i])
			if success == 1:
				sys.exit("Invalid size")


def extract(map: Map, first_corner: tuple, second_corner: tuple) -> np.array:
	new_map: np.array = np.array([['0'] * (second_corner[0] - first_corner[0])] * (second_corner[1] - first_corner[1]))
	for i in range(first_corner[0], second_corner[0] + 1):
		for j in range(first_corner[1], second_corner[1] + 1):
			new_map[i - first_corner[0], j - first_corner[1]] = map.map[i, j]

	return new_map


def intersect(entity1: Map, entity2: Map, coord_e1: tuple[int], coord_e2: tuple[int]) -> bool:
	return coord_e1[0] <= (coord_e2[0] + entity2.map.shape[0]) and (coord_e1[0] + entity1.map.shape[0]) >= coord_e2[0] and \
		coord_e1[1] <= (coord_e2[1] + entity2.map.shape[1]) and (coord_e1[1] + entity1.map.shape[1]) >= coord_e2[1]


def collision(entity1: Map, entity2: Map, coord_e1: tuple[int], coord_e2: tuple[int], empty_charac=' ') -> bool:
	if not(intersect(entity1, entity2, coord_e1, coord_e2)):
		return False

	pixels_entity_1: list[MapFromArray] = []
	pixels_entity_2: list[MapFromArray] = []

	for entity, pixel_list, coord in [entity1, entity2], [pixels_entity_1, pixels_entity_2], [coord_e1, coord_e2]:
		for i in range(entity.map.shape[0]):
			for j in range(entity.map.shape[1]):
				if entity.map[i, j] == empty_charac:
					continue
				else:
					pixel_list.append((i + coord[0], j + coord[1]))

	for pixel1 in pixels_entity_1:
		for pixel2 in pixels_entity_2:
			if pixel1 == pixel2:
				return True

	return False















