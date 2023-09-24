import requests
from bs4 import BeautifulSoup
import json

def get_text_from_all_entry_content(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <div class="entry-content"> elements
            entry_content_divs = soup.find_all('div', class_='entry-content')

            # Extract the text content of the single <p> tag inside each <div class="entry-content"> element
            text_content_list = []

            for entry_content_div in entry_content_divs:
                paragraph = entry_content_div.find('p')
                if paragraph:
                    text_content = paragraph.get_text()
                    text_content_list.append(text_content)

            return text_content_list
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

sentences = []

# Specify the URL of the web page you want to visit
url_to_visit = 'https://roar.media/sinhala/'

# Get the text content inside the <p> tag within all <div class="entry-content"> elements
text_in_all_entry_content = get_text_from_all_entry_content(url_to_visit)

# Print or process the extracted text content
if text_in_all_entry_content:
    for text_content in text_in_all_entry_content:
        # print(text_content)
        sentences.append(text_content)
else:
    print("No content extracted or an error occurred.")

# print(sentences)

output_file = "roar_media_documents.json"

# Write the result to the JSON file
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(sentences, json_file, ensure_ascii=False, indent=4)
