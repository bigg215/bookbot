def main():
	path_to_file = "books/frankenstein.txt"

	generate_reports(path_to_file)

def open_book(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def word_count(book_text):
	words = book_text.split()
	return len(words)

def char_count(book_text):
	counts = {}
	lowered_case = book_text.lower()
	
	for c in lowered_case:
		if c not in counts:
			counts[c] = 1
		else:
			counts[c] += 1
	
	return counts

def generate_reports(path_to_file):
	book = open_book(path_to_file)
	words = word_count(book)
	characters = char_count(book)
	char_list = []

	for c, num in characters.items():
		holder = {}
		if c.isalpha():
			holder['name'] = c
			holder['num'] = num
			char_list.append(holder)

	char_list.sort(reverse=True, key=sort_on)

	print(f"--- Begin report of {path_to_file} ---")
	print(f"{words} words found in the document")
	print("")

	for entry in char_list:
		print(f"The '{entry['name']}' character was found '{entry['num']}' times")

	print("--- End report ---")

def sort_on(dict):
	return dict["num"]




main()