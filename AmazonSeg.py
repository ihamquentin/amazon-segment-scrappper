#THIS CODE WAS WRITTING TO PRACTICE SEGMENT SCRAPING OF AMAZON
#CODE IS STILL UNCOMPLETED SINCE IT DOESN'T STORE TO A DATABASE
#DATE = 17TH OCTOBER 2021

from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


url = 'https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_unv_e_1_172665_4'
mainlist = []
big_data = []

def extractor(url):
    
    header = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find('span', {'class':'zg_selected'}).parent
    #births = results.find_next('ul').find_all('li')
    
    for li in results.find_next('ul').find_all('li'):
        new_name = li.get_text()
        for a in li.find_all('a', href=True):
            new_link = a['href']
        
            lister = {
                'product_name' : new_name,
                'product_link': new_link,
            }
            mainlist.append(lister)
    return mainlist


#catName, level1, level2, level3, level4 = ([] for i in range(5))
#counter = 0
catName = extractor(url)


for items in catName:
    #this collects category name and link for level 1
    category_name = [category_name['product_name'] for category_name in catName
                    if 'product_name' in category_name]
    level_link = [level_link['product_link'] for level_link in catName
                if 'product_link' in level_link]
    for levels in level_link:
        #this collects category name and link for level 2
        a_level2 = extractor(levels)
        category_name_new = [category_name_new['product_name'] for category_name_new in a_level2
                             if 'product_name' in category_name_new]
        level_link_new = [level_link_new['product_link'] for level_link_new in a_level2
                          if 'product_link' in level_link_new]
        #print(category_name_new)
        for level3_a in level_link_new:
            #this collects category name and link for level 3
            a_level3 = extractor(level3_a)
            category_name_new3 = [category_name_new3['product_name'] for category_name_new3 in a_level3
                                 if 'product_name' in category_name_new3]
            level_link_new3 = [level_link_new3['product_link'] for level_link_new3 in a_level3
                              if 'product_link' in level_link_new3]
            for level4_a in level_link_new3:
                #this collects category name and link for level 4
                a_level4 = extractor(level4_a)
                category_name_new4 = [category_name_new4['product_name'] for category_name_new4 in a_level4
                                     if 'product_name' in category_name_new4]
                level_link_new4 = [level_link_new4['product_link'] for level_link_new4 in a_level4
                                  if 'product_link' in level_link_new4]
                level4_id = ([int(s) for s in level_link_new4.split("/") if s.isdigit()][0])
                level4_number = ([s for s in level_link_new4.split("_")][-2])

    #this sorts the levels into a db container         
    collator = {
        'CatID': level4_Id,
        'CatLevel1': category_name,
        'CatLevel2': category_name_new,
        'CatLevel3': category_name_new3,
        'CatLevel4': category_name_new4,
        'Level': level_number,
        'CatUrl': level4_link,
    }
    print(collator)
    big_data.append(collator)
