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
        groupList = []
        #if content.span['class'] == 'tag':
        # for child in content.span['class'] == 'tag':
        for group in content.select('.tag'):
            groupList.append(group.a.string)

        print(groupList)
            


spider = Spider()
spider.getContents(1)

