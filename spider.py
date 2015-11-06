#coding: utf-8

import requests
from bs4 import BeautifulSoup
import os

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

    def writeFile(self,pageIndex,allList):
        fileName = str(pageIndex) + ".html"
        f = open(fileName, "w+")
        f.write(allList.encode('utf-8'))

    def letsGo(self):
        
        allList = self.getContents(1)
        self.writeFile(allList)

spider = Spider()
spider.letsGo()

      

            




