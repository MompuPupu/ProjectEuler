# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
# from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However,
# Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)

with open('Problem 18 Input.txt', 'r') as file:
	data = file.readlines()
	data[len(data) - 1] += '\n'

pyramid = []


def numerise_string():
	""" Runs through a string, and loads each number into a variable in an array. each line is a new row of the array
			WORKS
	:return: array of ints
	"""
	global data
	global pyramid
	new_num_str = ''

	for row in range(0, len(data)):
		new_row = []
		for c in data[row]:
			if c.isdigit():
				new_num_str += c
			elif c == ' ':
				new_row.append(int(new_num_str))
				new_num_str = ''
			elif c == '\n':
				new_row.append(int(new_num_str))
				new_num_str = ''
				pyramid.append(new_row)


def sum_pyramid():
	""" Sum the pyramid. Start at the bottom. Replace the penultimate row with the max sum of each value.

	Need to start on second-to-bottom row and compare the sum of each number with the pair of numbers it can go to.
	Replace each number on second-to-bottom row with the max sum.
	Delete bottom row.

	Run loop from bottom to top

	:return:
	"""
	global pyramid

	for row in range((len(pyramid) - 2), -1, -1):
		for num in range(len(pyramid[row])):
			pyramid[row][num] = max((pyramid[row][num] + pyramid[row + 1][num]),
									(pyramid[row][num] + pyramid[row + 1][num + 1]))

	return pyramid[0]


if __name__ == '__main__':
	numerise_string()
	print(sum_pyramid())
