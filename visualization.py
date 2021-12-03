import json
from os import error, name, read
import matplotlib.pyplot as plt

titles = []
def readFromJsonFile(fileName):
    with open(fileName,'r+') as f:
        data = json.load(f)
        return data


def getTitles(lst,index=None):
    global titles
    i = 0
    if index == None: index = 1 
    for i in range(len(lst)):
        titles.append(lst[i]['title'])

    return titles


lst = readFromJsonFile('data.json')
getTitles(lst)

def showGraph(allLst,nameLst,slct):
    names = []
    values = []
    title = nameLst[slct-1]
    for i in range(len(allLst)):
        if allLst[i]['title'] != title : continue
        for key in allLst[i].keys() :
            if key == 'title' : continue
            names.append(key)
            values.append(allLst[i][key])

        plt.bar(names, values)
        plt.title(title)
        plt.xticks(rotation=10)
        plt.show()
        print('Created report of',title,'...')
        return 1

for i in range(len(titles)):
    print(i+1,')',titles[i])
    
while True :
    print('\nfor opening another report please closed currently report')
    val = input('Please Select Report...(for exit : -1)  :')
    if val == '-1': break
    try:
        val = int(val)
        showGraph(lst,titles,val)
    except:
        print('Something went wrong, Please try again (for exit : -1)  ')
        continue

