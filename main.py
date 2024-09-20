def main():
	path_to_file = "books/frankenstein.txt"

	book = open_book(path_to_file)

	print(word_count(book))

def open_book(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def word_count(book_text):
	words = book_text.split()
	return len(words)

main()