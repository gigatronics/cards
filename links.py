import requests
from bs4 import BeautifulSoup 
import re  # Importing the missing 're' module

class DisclaimerExtractor:
    def __init__(self, urls: list) -> None:
        self.urls = urls  # Correctly assigning the list of URLs

    def make_soup(self, url) -> BeautifulSoup:   # Adding 'url' as a parameter
        return BeautifulSoup(requests.get(url).content, 'html.parser')

    def extract_disclaimers(self, soup) -> list:
        txt = soup.find_all(id=re.compile("disclaimer-token"))
        clean_txt = []

        for t in txt:
            clean_txt.append(t.get_text(" ", strip=True))

        return clean_txt

    def save_html(self, url, path) -> bool:  
        soup = self.make_soup(url)  # Define soup by calling make_soup
        filename = self.get_title(soup).replace(" ", "_").lower()
        with open(path + filename + '.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True
    
    def get_title(self, soup) -> str:
        return soup.title.string if soup.title else "untitled"


# Example usage
base = 'https://www.td.com/ca/en/personal-banking/products/credit-cards/'
urls = [
    'https://www.td.com/ca/en/personal-banking/products/credit-cards/aeroplan/aeroplan-visa-infinite-privilege-card',
    'https://www.td.com/ca/en/personal-banking/products/credit-cards/aeroplan/aeroplan-visa-platinum-card',
    'https://www.td.com/ca/en/personal-banking/products/credit-cards/aeroplan/aeroplan-visa-infinite-card',

    'https://www.td.com/ca/en/personal-banking/products/credit-cards/travel-rewards/first-class-travel-visa-infinite-card',
    'https://www.td.com/ca/en/personal-banking/products/credit-cards/travel-rewards/platinum-travel-visa-card',
    'https://www.td.com/ca/en/personal-banking/products/credit-cards/travel-rewards/rewards-visa-card',

    'https://www.td.com/ca/en/personal-banking/products/credit-cards/cash-back/cash-back-visa-infinite-card',
    'https://www.td.com/ca/en/personal-banking/products/credit-cards/cash-back/cash-back-visa-card',
    
    'https://www.td.com/ca/en/business-banking/small-business/credit-cards/aeroplan-visa-business-card',
    'https://www.td.com/ca/en/business-banking/small-business/credit-cards/business-travel-visa-card',
    'https://www.td.com/ca/en/business-banking/small-business/credit-cards/business-cash-back-visa-card',
    'https://www.td.com/ca/en/business-banking/small-business/credit-cards/business-select-rate-visa-card',
    
    'https://www.td.com/ca/en/personal-banking/products/credit-cards/low-rate/low-rate-visa-card',
    'https://www.td.com/ca/en/personal-banking/products/credit-cards/us-dollar/us-dollar-visa-card'
]

# us-dollar-visa-card#cmp-modal~OLNQEN15~udvcB

extractor = DisclaimerExtractor(urls)
full_txt = []  # Change to a list to use append
output_path = 'cards/copy_review/disclosure.txt'

for url in urls:
    soup = extractor.make_soup(url)
    disclaimers = extractor.extract_disclaimers(soup)
    print(extractor.save_html(url, output_path)) # Save the HTML content
    full_txt.append(f'######## {extractor.get_title(soup)} ########')
    full_txt.append('\n'+url)
    full_txt.append('\n'.join(disclaimers))  # Join disclaimers with newlines
    full_txt.append('\n\n')

# Ensure the directory exists or use an absolute path
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(''.join(full_txt))  # Join the list into a single string