# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first
# names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?


name_file_name = "E:\Coding\Python\Project Euler\Problems 21 - 30\p022_names.txt"
letters = ['']


def read_names(file_name):
	"""
	Reads all the names from the file and loads them into the global names variable with no punctuation
	:param file_name: Name file location
	:return:
	"""
	with open(file_name, 'r') as f:
		names_raw = f.read()
	names_raw = names_raw.split(',')
	names_stripped = []

	for name in names_raw:
		names_stripped.append(name.strip('\"'))
	print(names_stripped)
	return names_stripped


def sort_names(input_names):
	return sorted(input_names)


def assign_letters_to_scores():
	global letters
	letters_raw = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	letters = list(letters_raw)


def score_name(name, position):
	global letters
	letters_score = 0
	for c in name:
		for i in range(len(letters)):
			if c == letters[i]:
				letters_score += i

	return letters_score * position


if __name__ == '__main__':
	formatted_names = read_names(name_file_name)
	sorted_names = sort_names(formatted_names)
	assign_letters_to_scores()
	total_score = 0

	for i in range(len(sorted_names)):
		total_score += score_name(sorted_names[i], i + 1)
	print(total_score)
