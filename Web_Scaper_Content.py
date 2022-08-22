import requests
import bs4
              
#this loop will check everything on the website pages for the particular thing your wishing.

#starting with a empty dictionary which later will append with content
two_star_titles = []
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
        
for i in range(1,51):
    scrape_url = base_url.format(i)
    
    #usual requests.get method for calling the url
    res = requests.get(scrape_url)
    
    #usual calling soup library
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    #storing on books variable the soup.select .product_pod class content. This may vary depends on what class you calls.
    
    books = soup.select(".product_pod")
    #        
    for ii in books:
        if len(ii.select('.star-rating.Two')) != 0:
            
        #using the book_title as a variable holder for the content of select('a')[1]. a is the value we need to extract the title. 
        #it goes <a href something here. which why I input a. [1] is the index of the below value. When we run the result without
        #the [1] it gives us two value. Above is the image and below is the actual text. We rid the image value and just
        #scrape the title which is why it is on [1] the['title'] is the dictionary call with the specific word with Title
            book_title = ii.select('a')[1]['title']
            
            #appending the gathered content on the two_star_titles dictionary we just declared on the above.
            two_star_titles.append(book_title)
            
two_star_titles
        
