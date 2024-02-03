def word_frequency_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        words = text.split()
        frequency = {}
        for word in words:
            word = word.strip('.,?!()[]{}":;').lower()

            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

        return frequency

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = "/Users/admin/Desktop/Data Science & AI/Python/Assn 2/assn2_text_file.txt"   
result = word_frequency_from_file(file_path)

if result:
    print("Word Frequency:")
    print(result)
else:
    print("Failed to read the file.")
