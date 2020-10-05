from bs4 import BeautifulSoup
import requests

def searchResults(city, search):
    url = "https://" + city + ".craigslist.org/search/bbb?query="+search
    
    try:
        response = requests.get(url)
        if response.status_code !=200:
            # Couldn't Connect to criagslist.org
            return None
        else:
            soup=BeautifulSoup(response.content,'html.parser')
            search_results = soup.find(id='sortable-results').ul
            result_list=[]
            for res in search_results.children:
                if res.name == 'li':
                    di=dict()
                    di['link']=res.a.get('href')

                    data_ids=res.a.get('data-ids')
                    if data_ids == None:
                        di['image_url'] = "../static/images/Image_Not_Found.jpg"
                    else:
                        data_id=data_ids.split(',')[0][2:]
                        di['image_url']="https://images.craigslist.org/"+data_id+"_300x300.jpg"

                    di['date_time']=res.div.time.get('title')
                    di['title']=res.div.h2.a.string
                    result_list.append(di)
            return result_list
    except Exception:
        return None