from os import write
import sqlite3
import json

db = 'db.sqlite'

try :
    conn = sqlite3.connect(db)
    cur = conn.cursor()
except :
    print(db,'named database not found...')
    print('The Program terminated, Please Check the databse file')
    quit()

(totalPerson,) = cur.execute('SELECT COUNT(*) FROM Person').fetchone()


def createUnique(columnName,cur):
    query = 'SELECT DISTINCT ' + columnName + ' FROM Person'  
    cur.execute(query)
    row = cur.fetchall()
    uniqueVals = []
    for (item,) in row :
        uniqueVals.append(item)
    print('We have',len(uniqueVals),'different',columnName) 
    print('These ' + columnName + ' were used while collecting data.',uniqueVals,'\n')
    
    return uniqueVals

def countRelatoin(rel1,col1,cur,rel2=None,col2=None):
    relationDict = dict()
    sortedRelationDict = dict()
    if col2 != None :
        query = 'SELECT COUNT(*) FROM Person WHERE ('+ col1 + '=? AND ' + col2 + '=?)'
        for item1 in rel1:
            for item2 in rel2:
                key = str(item1) + '_' + str(item2)
                cur.execute(query,(item1,item2))
                (count,) = cur.fetchone()
                relationDict[key] = count
                
    else:
        query = 'SELECT COUNT(*) FROM Person WHERE ('+ col1 + '=?)'
        for item in rel1:
            key = str(item)
            cur.execute(query,(item,))
            (count,) = cur.fetchone()
            relationDict[key] = count

    for item in sorted(relationDict.keys()):
        sortedRelationDict[item] = relationDict[item]
    

    if col2 != None :
        print(col2,'distribution by',col1,sortedRelationDict,'\n')
        title = str(col2) + ' distribution by ' + str(col1)
    else:
        print(col1,'distribution by',sortedRelationDict,'\n')
        title = str(col1) + ' distribution'
    
    updateSortedRelationDict = {'title':title}
    updateSortedRelationDict.update(sortedRelationDict)
    return updateSortedRelationDict

def averageRelation(rel1,col1,cur,rel2=None,col2=None):
    relationDict = dict()
    sortedRelationDict = dict()
    if col2 != None:
        query = 'SELECT AVG(earnings) FROM Person WHERE ('+ col1 + '=? AND ' + col2 + '=?)'
        for item1 in rel1:
            for item2 in rel2:
                key = str(item1) + '_' + str(item2)
                cur.execute(query,(item1,item2))
                (avg,) = cur.fetchone()
                avg = float("{:.2f}".format(avg))
                relationDict[key] = avg

    else:
        query = 'SELECT AVG(earnings) FROM Person WHERE (' + col1 + '=?)'
        for item1 in rel1 :
            key = str(item1)
            cur.execute(query,(item1,))
            (avg,) = cur.fetchone()
            avg = float("{:.2f}".format(avg))
            relationDict[key] = avg

    for item in sorted(relationDict.keys()):
        sortedRelationDict[item] = relationDict[item]
    
    if col2 != None :
        print('Avarage Income Per Hour according to',col1,'and',col2,sortedRelationDict,'\n')
        title = 'Avarage Income Per Hour according to ' + str(col1) + ' and ' + str(col2)
    else:
        print('Avarage Income Per Hour according to',col1,sortedRelationDict,'\n')
        title = 'Avarage Income Per Hour according to ' + str(col1)
    
    updateSortedRelationDict = {'title':title}
    updateSortedRelationDict.update(sortedRelationDict)
    return updateSortedRelationDict


print('\n***RESULT BELOW***\n')
print('Total Number of people used for analysis: ',totalPerson , '\n')
years = createUnique('year',cur)
degrees = createUnique('degree',cur)
genders = createUnique('gender',cur)
ages = createUnique('age',cur)

yearsCount = countRelatoin(years,'year',cur)
yearsDegree = countRelatoin(years,'year',cur,degrees,'degree')
yearsGender = countRelatoin(years,'year',cur,genders,'gender')

degreesGender= countRelatoin(degrees,'degree',cur,genders,'gender')
#yearsAge = countRelatoin(years,ages,'year','age',cur)

avgYears = averageRelation(years,'year',cur)
avgGender = averageRelation(genders,'gender',cur)
avgDegree = averageRelation(degrees,'degree',cur)

avgYearsGender = averageRelation(years,'year',cur,genders,'gender')
avgYearsDegree = averageRelation(years,'year',cur,degrees,'degree')

data = [yearsCount,yearsDegree,yearsGender,degreesGender,avgYears,avgGender,avgDegree,avgYearsGender,avgYearsDegree]

def writeToJsonFile(List,fileName):
    with open(fileName,'w+') as f:
        f.write(json.dumps(List,indent=4))
    print('Created',fileName,'for data visualization')

writeToJsonFile(data,'data.json')



