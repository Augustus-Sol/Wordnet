#credit for definition data pulled from the Internet goes to wordnetweb.princeton.edu

import requests
from lxml import html


def findDef(s):
    masterList = []
    address = str(
        'http://wordnetweb.princeton.edu/perl/webwn?s=' + s + '&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=0')
    r = requests.get(address)
    tree = html.fromstring(r.content)

    for loo in range(3):


        foo = 1
        defResult = ['a']
        exSentence = ['a']

        while (defResult != [] or exSentence != []):
            strList = []
            defResult = tree.xpath('/html/body/div[2]/ul[' + str(loo) + ']/li['+ str(foo) + ']/text()') #definition
            exSentence = tree.xpath('/html/body/div[2]/ul[' + str(loo) + ']/li[' + str(foo) + ']/i/text()')  #used in a sentence
            partOfSpeech = tree.xpath('/html/body/div[2]/ul[' + str(loo) + ']/li[' + str(foo)+ '] / a[2]/text()') #part of speech

            #print each one individually above for testing purposes

            foo += 1
            toPrintDef = list(defResult)
            toPrintSentence = list(exSentence)
            toPrintPOS = list(partOfSpeech)

            if toPrintPOS:
                strList.append(toPrintPOS.pop())
            if toPrintDef:
                strList.append(toPrintDef.pop())
            if toPrintSentence:
                strList.append(toPrintSentence.pop())
            if strList:
                print(strList)
                print('\n')
                masterList.append(strList)

    if masterList:
        return masterList
    else:
        print('The word you were looking for could not be found.')


print(findDef('plunder'))
