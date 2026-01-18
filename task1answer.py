import os
import requests
from bs4 import BeautifulSoup

# Define the URL globally so it can be used inside functions
url = "https://web.archive.org/web/20191126074327/https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7"
    
def get_page():
    response = requests.get(url)
    response.raise_for_status() # Check for errors
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
def collect_text(soup):
    
    text = f'url: {url}\n\n'
    para_text = soup.find_all('p')
    print(f"paragraphs text = \n {para_text}")
    
    for para in para_text:
        text += f"{para.text}\n\n"
    return text

def save_file(text):
   
    # Create directory if it doesn't exist
    if not os.path.exists('./scraped_articles'):
        os.mkdir('./scraped_articles')
    
    # Create filename based on the URL
    name = url.split("/")[-1]
    print(name)
    fname = f'scraped_articles/{name}.txt'
    
    with open(fname, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f'File saved in directory {fname}')

if __name__ == '__main__':
    text = collect_text(get_page())
    save_file(text)