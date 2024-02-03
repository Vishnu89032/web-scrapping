web scrapping:-

This python script is a simple web scrapping, using libraries like Beautiful soup and requests.

(beautiful soup - to parse HTML content
requests - to make http requests)

the purpose of the program is to retrieve the titles of latest articles from python.org website

**importing libraries:**

import requests
from bs4 import BeautifulSoup

**get_latest_python_article Function:**

def get_latest_python_article():
    url = "https://www.python.org"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        latest_article = []

        for article in soup.select(".event-widget li"):
            title = article.a.text.strip()
            latest_article.append(title)

        return latest_article
    else:
        print(f"Failed to retrieve information. Status code: {response.status.code}")
        return []

description:

"get" request to the Python.org website and checks if the response status code is 200
If the response is successful, it uses BeautifulSoup to parse the HTML content.
It selects all list items (li) within elements with the class "event-widget" and extracts the text content of the anchor (a) inside each list item.
The article titles are appended to the latest_article list, which is then returned.
If the request fails, it prints an error message and returns an empty list.

**__main__ Block:**

if __name__ == "__main__":
    python_article = get_latest_python_article()

    if python_article:
        print("New News in the python.org section")
        for index, article in enumerate(python_article, 1):
            print(f"{index}. {article}")
    else:
        print("No article found")

description:

This block is executed when the script is run as the main program.
It calls the get_latest_python_article function to retrieve the latest Python articles.
If articles are found, it prints a header and enumerates through the list of articles, displaying them with their index.
If no articles are found, it prints a message indicating that no articles were found.

Summary:
Its a basic web scraper that fetches and displays the titles of the latest articles from the Python.org website

word frequency:-

It defines a function "word_frequency_from_file" that takes a file path as an argument and returns a dictionary representing the frequency of each word in the file. 
        
**Function definition**

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

description:

To open and read the file specified by file_path using the with statement, which ensures that the file is properly closed after reading.
split()- The text content of the file is then split into a list of words 
A dictionary named - frequency is initialized to store word frequencies.
Each word is processed by removing common punctuation and converting it to lowercase.
The script then updates the word frequency in the dictionary.
Finally, the function returns the word frequency dictionary.

**Application of the Function**

file_path = "/Users/admin/Desktop/Data Science & AI/Python/Assn 2/assn2_text_file.txt"   
result = word_frequency_from_file(file_path)

if result:
    print("Word Frequency:")
    print(result)
else:
    print("Failed to read the file.")

description:

The file_path variable is set to the path of a specific text file.
The word_frequency_from_file function is called with this file path, and the result is stored in the result variable.
If the function is successful "result is not None", it prints the word frequency dictionary.
If there is an error reading the file, it prints an error message.

Summary:
It reads a text file, tokenizes the words, and counts the frequency of each word, ignoring common punctuation. 
The final word frequency dictionary is then printed if the file is successfully processed.
        
