def main():
	path_to_file = "books/frankenstein.txt"

	book = open_book(path_to_file)

	print(char_count(book))

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


main()