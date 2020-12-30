from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt
import re
def get_url(base_url: str, job: str,jt :str ):
    """a function to built the url of the page to be scaped.

    Args:
        base_url (str): url of the index page
        job (str): job 
        jt (str): job type. Supported jib types are:
            - "internship", 'contract', "permanent", "parttime", "apprenticeship", "custom_1", "subcontract" 

    Raises:
        NotImplementedError: Only indeed urls are supported 

    Returns:
        str: url of the page to be scaped
    """    
    if re.search('indeed', base_url):
        return  base_url + "/emplois?q={}&jt={}".format(job, jt)
    else :#TODO
        raise NotImplementedError

def get_text(url, section , classe):
    """A function to parse the description of an offer from it's url

    Args:
        url (str): a complete url 
        section (str): the section containing the description
        classe (str): the section classe

    Returns:
        str: Description text 
    """
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser') 
    tags = soup.find(section, {"class": classe})
    return tags.text


def get_offers(base_url, url ):
    """A function to scrape job offers from a base url.

    Args:
        base_url (str): url of the index page
        job ([type]): job your are looking for 
        jt ([type]): job type

    Returns:
        DataFrame: Job offers dataframe with the following columns : 'title', 'date', 'lien', 'description'
    """    

    section = 'div'
    classe = "jobsearch-jobDescriptionText"
    
    response = requests.get(url)
    page= response.text
    soup = BeautifulSoup(page, 'html.parser')

    titles, links, dates,  description = [], [], [], []
    offres = soup.find_all("div", {"class": "jobsearch-SerpJobCard unifiedRow row result"})
    for offre in offres:
        title_link = offre.find_all("a", {"class": "jobtitle turnstileLink " })
        link = base_url+title_link[0].get('href')
        title = title_link[0].get('title')
        date = offre.find_all("div", {"class": "result-link-bar" })[0].text.split('Sau')[0]
        descrip = get_text(link, section, classe)
        
        titles.append(title)
        links.append(link)
        dates.append(date)
        description.append(descrip)

    datazip =list(zip(titles, dates, links, description))
    df = pd.DataFrame(datazip, columns =['title', 'date', 'lien', 'description'])# date = date de publication

    suivant = soup.find_all("a", {"aria-label": "Suivant"})
    if len(suivant)>0:
      url = base_url+suivant[-1].get('href')
      df = df.append(get_offers(base_url, url))
    return df