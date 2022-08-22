def web_scrap_image():
    result_image = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
    soup_image = bs4.BeautifulSoup(result_image.text, "lxml")
    
    #.thumbimage is the class name we define [0] represent the first result we tested
    #you may also remove the [0] to view all the content associated with the said class
    selected_soup_image = soup_image.select(".thumbimage")[0]
    
    #save it to selected_soup_image1 with the content of 'src' you can return the 1 variable to see the content
    selected_soup_image1 = selected_soup_image['src']
    
    #use this to request the binary file of the image
    #you can also do loop to download every image here, just for poc we use one link
    image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
    
    #this will download the image you want, wb on the end of code means write binary, which enables python to download the image.
    f = open('selected_soup_image.jpg', 'wb')
    f.write(image_link.content)
    
    f.close()
    #upon running the image must be saved on your local
    
    #to return the binary file incase you need to see
    #return image_link.content

#disable the comment if you wanna download the images associated.
#web_scrap_image()
