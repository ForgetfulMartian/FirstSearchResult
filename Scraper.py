import Return_First
import requests
from bs4 import BeautifulSoup

url = Return_First.well()


def scrape_website(url):
    # Send a GET request to the website URL and retrieve the HTML content
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the text from the relevant HTML elements
    text = ""
    for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        text += element.get_text(strip=True) + " "

    return text.strip()


# Example usage

scraped_text = scrape_website(url)
if scraped_text:
    print("Scraped text:\n", scraped_text)
else:
    print("No text found.")
