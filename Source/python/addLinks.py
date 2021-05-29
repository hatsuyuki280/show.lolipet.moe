# -*- coding:utf-8 -*-

import os
import sys
import random
import json
import requests
import socket

Workspace = os.path.join(sys.argv[1], 'Source')
picPath = os.path.join(sys.argv[1], 'img')


def main():
    readJsonToDict()
    listVisible()
    randomVisibleLinks()
    count = 0
    pos = 0
    for item in visibleList:
        if checkUrl(linksDict[item]['url']):
            imgPath=getScreenShout(linksDict[item]['url'])
            addLink(item,imgPath,pos)
        count += 1
        pos = count % 3


def readJsonToDict():
    with open(os.path.join(Workspace, 'Links.json')) as sourceFile:
        sourceJson = sourceFile.read()
        global linksDict
        linksDict = json.loads(sourceJson)


def listVisible():
    global visibleList
    visibleList = []
    for name in linksDict.keys():
        if linksDict[name]['visible'] == True:
            visibleList.append(name)


def randomVisibleLinks():
    global visibleList
    random.shuffle(visibleList)


def checkUrl(url):  ## 这个地方准备拿来随便访问下主页，强制https，不超时的情况下返回 true
    pass


def getScreenShout(url):    ## 这个地方将会对 url 进行抓图，存入 ../img 文件夹后返回路径
    baseURL = "https://s0.wordpress.com/mshots/v1/https://"


    return imgPath

def addLink(name,path,pos):     ## 这个地方将会拿来添加链接，传入的三个参数分别是友链的 Key 截图位置 和 友链坐标。
    pass


if __name__ == '__main__':
    main()
