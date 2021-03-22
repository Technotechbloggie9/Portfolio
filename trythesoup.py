import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
def main():
    #step 2 import the data from the site
    website = 'https://www.smartsheet.com/factory-manufacturing-automation'
    website_url = requests.get(website).text
    soup = BeautifulSoup(website_url, 'html.parser')
    #step 3
    my_list = soup.find('ul')
    my_list2 = soup.find('ol')
    list_data = []
    list_data2 = []
    for listitem in my_list.findAll('li'):
        list_data.append(listitem.text)
    for listitem in my_list2.findAll('li'):
        list_data2.append(listitem.text)
    print(list_data)
    print(list_data2)
    '''
    assessment: list items captured,
    but the usability is probably poor
    may want to find a website with actual tables
    to scrape
    '''
if __name__=="__main__":
    main()
    
