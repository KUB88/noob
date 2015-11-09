# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import re

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
        dic = {}
        for groupSpan in content.select('.tag'):
            pattern = re.compile('href="(magnet.*?)"',re.S)            
            items = re.findall(pattern,str(groupSpan.find_next(class_ = "download-arrow arrow-magnet")))
            dic['group'] = groupSpan.a.string.strip()
            dic['title'] = groupSpan.find_next_sibling('a').string.strip()
            dic['download'] = items
            items = []
            allList.append(dic)
        print(allList)
        return allList

    # def writeFile(self,pageIndex,allList):
    #     nextLine = '\t'
    #     fileName = "D:/" + str(pageIndex) + ".txt"
    #     f = open(fileName, "wb+")
    #     for entery in  allList:
    #         for items in entery:
    #             f.write(items.encode('utf-8'))
    #         f.write(nextLine.encode('utf-8'))
    #     f.close()   


    def letsGo(self):        
        allList = self.getContents(1)
        #self.writeFile(1, allList)

spider = Spider()
spider.letsGo()

      

            




