#credit for definition data pulled from the Internet goes to wordnetweb.princeton.edu
import getopt, sys


import requests
from lxml import html


def scrapeSynsets(s):
    masterList = []
    address = str(
        'http://wordnetweb.princeton.edu/perl/webwn?s=' + s + '&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=0')
    r = requests.get(address)
    tree = html.fromstring(r.content)

    # we start a loop to navigate'/html/body/div[2]/ul/ {loop variable}'
    # the reason this number is 8 is because there are a constant 8 parts of speech, and
    # hence there will be a max of 8 categories containing scrape-able content within this section of the x-path
    for loo in range(8):


        foo = 1
        defResult = ['a']
        exSentence = ['a']

        while (defResult != [] or exSentence != []):
            strList = []
            defResult = tree.xpath('/html/body/div[2]/ul[' + str(loo) + ']/li['+ str(foo) + ']/text()') #definition
            exSentence = tree.xpath('/html/body/div[2]/ul[' + str(loo) + ']/li[' + str(foo) + ']/i/text()')  #used in a sentence
            partOfSpeech = tree.xpath('/html/body/div[2]/ul[' + str(loo) + ']/li[' + str(foo)+ '] / a[2]/text()') #part of speech

            synList = []
            synonyms= "initiate"
            goo=3
            while synonyms:
                synonyms = tree.xpath(
                '/html/body/div[2]/ul[' + str(loo) + ']/li[' + str(foo) + ']/a[' + str(goo) + ']/text()')
                if synonyms:
                    synList.append(list(synonyms).pop())
                goo+=1

            foo += 1

            if synList:
                strList.append(list(synList))

            if strList:
                print(strList)
                print('\n')
                masterList.append(strList.pop())  # appends the database row to our masterList 'table'

    if masterList:
        file_to_write = open(str(s)+'_SYNSETS.txt', 'w')
        for item in masterList:
          file_to_write.write("%s\n" % item)
        return masterList
    else:
        print('The word you were looking for could not be found.')
######################################################################################################################



######################################################################################################################
#  Code below comes from: http://stackabuse.com/command-line-arguments-in-python/
# count the arguments
arguments = len(sys.argv) - 1
print("the script is called with %i arguments" % arguments)
# output argument-wise
position = 1
while (arguments >= position):
    scrapeSynsets(sys.argv[position])
    position = position + 1

