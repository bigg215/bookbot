def main():
	path_to_file = "books/frankenstein.txt"

	with open(path_to_file) as f:
		file_contents = f.read()

	words = file_contents.split()

	print(len(words))

main()