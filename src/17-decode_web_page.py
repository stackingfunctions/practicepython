import urllib.request
from bs4 import BeautifulSoup


def parsePage(URL):
    return BeautifulSoup(urllib.request.urlopen(URL))

def getHeaders(bsObj):
    headerContainers = bsObj.findAll("h2", {"class": "story-heading"})
    headers = []
    for header in headerContainers:
        str = None
        try:
            headers.append(header.a.getText().strip())
        except AttributeError:
            headers.append(header.getText().strip())

    return headers



if __name__ == "__main__":
    counter = 0
    for header in getHeaders(parsePage("http://www.nytimes.com")):
        print(header)
        counter += 1
    print("\nThere are ", counter, " article titles on NYTimes front page.")