# Go to a weather website
# Get the current temperature and waether for your local city
#  Print the current temp and weather

# Hit the websites using requests module
# Parse the html

import requests
import bs4

def send_request(website_url: str) -> str:
    return requests.get(website_url).text


def parse_html_string(html_str: str) -> bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(html_str, 'html.parser')
    return soup

def fetch_current_date(parsed_html: bs4.BeautifulSoup) -> str:
    top_element = parsed_html.find(id="top")
    date_element = top_element.find('div', class_="date")
    current_date = date_element.span.string.removeprefix('\n')
    return current_date
def main():
    website ="https://www.hamropatro.com/"
    html_str = send_request(website)
    parsed_html = parse_html_string(html_str)
    current_date = fetch_current_date(parsed_html)

    print(f"The current temperature is {current_date} for today.")



if __name__ == '__main__':
    main()