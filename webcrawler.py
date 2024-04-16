#Gabriela Fuller
#“I have not given or received any unauthorized assistance on this assignment.”

import requests
from bs4 import BeautifulSoup
import re
import heapq
from collections import Counter

def get_words_from_url(url):
    """
    Extracts words from a given URL.

    Args:
      url: The URL of the webpage to extract words from.

    Returns:
      A list of words found on the webpage.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Remove script tags and style tags
    for script in soup(["script", "style"]):
        script.extract()

    # Get text from the webpage
    text = soup.get_text(separator=" ")

    # Remove non-alphanumeric characters and convert to lowercase
    words = re.findall(r"\w+", text.lower())

    return words

def count_word_frequency(words):
    """
    Counts the frequency of each word in a list of words.

    Args:
      words: A list of words.

    Returns:
      A dictionary where the keys are the words and the values are their frequencies.
    """
    word_counts = Counter(words)

    return word_counts

def get_most_common_words(word_counts, num_words):
    """
    Gets the most common words from a dictionary of word counts.

    Args:
      word_counts: A dictionary where the keys are the words and the values are their frequencies.
      num_words: The number of most common words to return.

    Returns:
      A list of the most common words.
    """
    return heapq.nlargest(num_words, word_counts, key=word_counts.get)

def main():
    """
    Crawls a website and finds the 25 most common words.

    Args:
      None

    Returns:
      None
    """
    # Set the starting URL and the maximum number of links to visit
    start_url = "http://cdm.depaul.edu"
    max_links = 10000

    # Visited URLs to avoid revisiting
    visited_urls = set()

    # Keep track of word counts
    word_counts = Counter()

    # Crawl the website
    queue = [start_url]
    while queue and len(visited_urls) < max_links:
        url = queue.pop(0)
        if url not in visited_urls:
            visited_urls.add(url)

            # Extract words from the webpage
            words = get_words_from_url(url)

            # Update word counts
            word_counts.update(words)

            # Find links to other pages on the website
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            for link in soup.find_all('a', href=True):
                next_url = link['href']
                if next_url.startswith('http') and next_url not in visited_urls:
                    queue.append(next_url)

    # Get the most common words
    most_common_words = get_most_common_words(word_counts, 25)

    # Print the results
    print("The 25 most common words on the CDM website:")
    for word in most_common_words:
        print(word)

if __name__ == "__main__":
    main()