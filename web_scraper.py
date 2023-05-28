import requests
from bs4 import BeautifulSoup


"""
    Retrieves the number of citations needed from a Wikipedia page.

    Args:
        URL (str)

    Returns:
        The count of citations needed on the given Wikipedia page.
    """


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
def get_citations_needed_count(URL):
    # sending a request from this claint to the server to get the page content and store it inside the variable
    page = requests.get(URL) 

    # convert the data inside the request module response obj to HTML
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # will return a list of BeautifulSoup objects that match the spicefy element in other word to return all sup that have this class name
    all_citations = soup.find_all('sup', class_= 'noprint Inline-Template Template-Fact') # **kwargs to specify a key
    count = 0
    for citation in all_citations:
        if citation:
            count += 1
    return count
print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))


def get_citations_needed_report(URL):
    """
 this function to get the paragraph contan the citation
    """
def  get_citations_needed_report(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_tags = soup.find_all('sup', class_='noprint')
    citations = [response.find_previous('p').text.strip() for response in citation_tags]
    result = '\n'.join(citations)
    return print(result)
get_citations_needed_count(URL)
get_citations_needed_report(URL)