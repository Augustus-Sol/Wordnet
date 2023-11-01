from appIdeas.WordNet.synonymList import findSynList

#basic v1
def thesaurize (file):
    non_blank_count = 0
    word_count = 0
    newTXT = ''

    with open(file) as infp:
        for line in infp:
            if line.strip():
                non_blank_count += 1

    fh = open(file)
    for line in fh:
        for word in line.split():
            synonyms = findSynList(word)
            if synonyms == 'This word has no synonyms.':
                newTXT += ' ' + str(word)
            else:
                newTXT += ' ' + str(synonyms[0])

    print(newTXT)

thesaurize('greekparagraph.txt')
