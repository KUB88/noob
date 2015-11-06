#coding: utf-8

import requests
from bs4 import BeautifulSoup

#https://share.dmhy.org/topics/list/page/1
class Spider:
    def __init__(self):
        self.startURL = 'https://share.dmhy.org'
        

    def getPage(self,pageIndex):
        response = requests.get(self.startURL+'/topics/list/page/'+str(pageIndex))
        soup = BeautifulSoup(response.text)
        return soup
    
    def getContents(self,pageIndex):
        content = self.getPage(pageIndex)
        enteryList = []
        allList = []
        #if content.span['class'] == 'tag':
        # for child in content.span['class'] == 'tag':
        for groupSpan in content.select('.tag'):
            enteryList.append(groupSpan.a)
            enteryList.append(groupSpan.find_next_sibling('a'))
            enteryList.append(groupSpan.find_next(class_ = "download-arrow arrow-magnet"))
            allList.append(enteryList)
        return allList
            


spider = Spider()
spider.getContents(1)

