import requests
import bs4
from urllib.parse import urljoin


def webscraper_website_content():
    # get the website content
    result = requests.get("https://www.scrapethissite.com/pages/")
    type(result)
    result.text

    # save into a the soup variable and via lxml decode the website

    soup = bs4.BeautifulSoup(result.text, "lxml")
    # calling soup to print if we actually getting the data
    soup

    # via the soup.select[0] we organize the output and make it more easier to read
    selected_soup = soup.select('div.page')

    # this for loop print all the "td" class name inside the harvested code.
    for div in selected_soup:
        title = div.select_one('h3.page-title').text.strip()
        information = div.select_one('p.lead.session-desc').text.strip()
        link = div.select_one('a')['href'].strip() if div.select_one('a') else "N/A"

        # using the full_link function to join the two links.
        full_link = urljoin("https://www.scrapethissite.com/pages/", link)

        print(f"Title: {title}\nInformation: {information}\nLink: {full_link}\n\n")


webscraper_website_content()

