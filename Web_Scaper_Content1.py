import requests
import bs4

def webscraper_website_content():
    #get the website content
    result = requests.get("https://www.philgeps.gov.ph/Indexes/getFormerOpportunities")
    type(result)
    result.text

    #save into a the soup variable and via lxml decode the website

    soup = bs4.BeautifulSoup(result.text, "lxml")
    #calling soup to print if we actually getting the data
    soup

    #via the soup.select[0] we organize the output and make it more easier to read
    selected_soup = soup.select('td')[0]

    #this for loop print all the "td" class name inside the harvested code.
    for item in soup.select('td'):
        print (item.text)


webscraper_website_content()
        
    
#selected_soup
