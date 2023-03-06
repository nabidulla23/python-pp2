with open("Words.txt", "w") as output_file:
    with open("original_words.txt", "r") as input_file:
        for line in input_file:
            words = line.strip().split()
            updated_words = [word for word in words if word.isalpha() and len(word) >= 3]
            output_file.write(" ".join(updated_words) + "\n")