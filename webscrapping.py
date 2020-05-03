from bs4 import BeautifulSoup as soup  # HTML data structure
#from urllib.request import urlopen as uReq  # Web client
import requests
# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2"
#https://www.amazon.in/s?k=laptop&page=2&qid=1588345599&ref=sr_pg_2
#https://www.amazon.in/s?k=laptop&page=3&qid=1588346939&ref=sr_pg_3

# opens the connection and downloads html page from url
#uClient = uReq(page_url)
page = requests.get(page_url)


# parses html into a soup data structure to traverse html
# as if it were a json data type.
#page_soup = soup(uClient.read(), "html.parser")
#uClient.close()
page_soup = soup(page.content, 'html.parser')

out_filename = "product_description.csv"
headers = "Description \n"

# opens file, and writes headers
f = open(out_filename, "w",encoding="utf-8")
f.write(headers)


result = page_soup.find_all('span', class_="a-size-medium a-color-base a-text-normal")
descriptions = [desc.text for desc in result]
#page.close()

def iterate_on_pages(description) -> any:
    base_url = "https://www.amazon.in/s?k=laptop&page={}&qid=1588345599&ref=sr_pg_{}"
    for page in range(2, 21):
        #base_url1 = base_url.format(page,page)
        #print("base_url1 :",base_url1)
        #uClient = uReq(base_url1)
        page = requests.get(base_url.format(page,page))
        #page_soup = soup(uClient.read(), "html.parser")
        page_soup = soup(page.content, 'html.parser')
        #uClient.close()
        result = page_soup.find_all('span', class_="a-size-medium a-color-base a-text-normal")
        description.extend( [desc.text for desc in result])
        #page.close()
    #print(description)
    page.close() 
    return description 

final_description_list =iterate_on_pages(descriptions)
for i in range (0, len(final_description_list)) :
     #print(final_description_list[i])
     f.write(final_description_list[i] +"\n")

page.close()


f.close() 


#print(discriptions)

#f.close()  # Close the file

