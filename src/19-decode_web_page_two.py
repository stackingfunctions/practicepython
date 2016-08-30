from bs4 import BeautifulSoup
import urllib.request


class LewinskyArticle():
    def __init__(self):
        self.rootURL = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

        # It is easiest to get the page URLs by noticing the pattern in the URL
        #   http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture#1 - page1
        #   http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture#2 - page2
        self.pageURLs = {1: self.rootURL, 2: self.rootURL + "#2", 3: self.rootURL + "#3", 4: self.rootURL + "#4", 5: self.rootURL + "#5"}
        self.pageContents = {1: None, 2: None, 3: None, 4: None, 5: None}

    def getTitle(self, bsObj):
        return bsObj.find("p", class_="nav-title").getText()

    def prettyfy(self):
        res = ""

        for i in range(1, len(self.pageContents)):
            res += "\n(Page %d)\n\n" % i
            for page in self.pageContents.get(i):
                res += "".join(page) + "\n\n"

        return res

    def parsePages(self):

        for i in range(1,5):
            bsObj = BeautifulSoup(urllib.request.urlopen(self.pageURLs[i]))

            paragraphs = []
            for paragraph in bsObj.findAll("p", class_=None):
                paragraphs.append(paragraph.getText())

            self.pageContents[i] = paragraphs

def saveFile(str, filename):
    file = open(filename, "w")
    file.write(str)
    file.close()


if __name__ == "__main__":

    article = LewinskyArticle()
    article.parsePages()
    saveFile(article.prettyfy(), "../tmp/Lewinsky.txt")
