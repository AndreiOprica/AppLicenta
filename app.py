from flask import Flask, render_template
import sqlite3
import sys

app = Flask(__name__)


def computeTF(wordDict, bow):

    tfDict = {}
    bowCount = len(bow)

    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)

    return tfDict


def computeIDF(docList):

    import math
    idfDict = {}
    N = len(docList)
    idfDict = dict.fromkeys(docList[0].keys(), 0)

    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))

    return idfDict


def computeTFIDF(tfBow, idfs):

    tfidf = {}

    for word, val in tfBow.items():
        tfidf = val * idfs[word]

    return tfidf


@app.route('/')
def hello_world():

    # connect to database, extract data and put data in lists
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM datas')

    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []
    c10 = []
    c11 = []
    c12 = []
    c13 = []
    c14 = []
    c15 = []
    c16 = []
    c17 = []
    c18 = []
    c19 = []
    c20 = []

    for row in cur:
        if (row[1][0] == 'L' and row[1][1] == 'i' and row[1][2] == 'n' and row[1][3] == 'k' and row[1][4] == ':' and row[1] != 'Link: http://www.cceai.org/' and row[1] != 'Link: https://coinsconf.com/' and row[1] != 'Link: https://www.mlforhc.org/' and row[9] != 'Call For Papers'):
            c1.append(row[0])
            c2.append(row[1])
            c3.append(row[2])
            c4.append(row[3])
            c5.append(row[4])
            c6.append(row[5])
            c7.append(row[6])
            c8.append(row[7])
            c9.append(row[8])
            c10.append(row[9])
            c11.append(row[10])
            c12.append(row[11])
            c13.append(row[12])
            c14.append(row[13])
            c15.append(row[14])
            c16.append(row[15])
            c17.append(row[16])
            c18.append(row[17])
            c19.append(row[18])

    # calculate score and add it to lists
    for i in range(len(c13)):
        bowCategory = c13[i].split(" ")
        bowDescription = c15[i].split(" ")

        wordSet = set(bowCategory).union(set(bowDescription))

        wordDictCategory = dict.fromkeys(wordSet, 0)
        wordDictDescription = dict.fromkeys(wordSet, 0)

        for word in bowCategory:
            wordDictCategory[word] += 1

        for word in bowDescription:
            wordDictDescription[word] += 1

        tfBowCategory = computeTF(wordDictCategory, bowCategory)
        tfBowDescription = computeTF(wordDictDescription, bowDescription)

        idfs = computeIDF([wordDictCategory, wordDictDescription])

        tfidfBowCategory = computeTFIDF(tfBowCategory, idfs)
        tfidfBowDescription = computeTFIDF(tfBowDescription, idfs)

        c20.append((tfidfBowCategory + tfidfBowDescription))

    for i in range(len(c20)):
        max_score = i
        for j in range(i+1, len(c20)):
            if c20[max_score] < c20[j]:
                max_score = j

        c20[i], c20[max_score] = c20[max_score], c20[i]
        c1[i], c1[max_score] = c1[max_score], c1[i]
        c2[i], c2[max_score] = c2[max_score], c2[i]
        c3[i], c3[max_score] = c3[max_score], c3[i]
        c4[i], c4[max_score] = c4[max_score], c4[i]
        c5[i], c5[max_score] = c5[max_score], c5[i]
        c6[i], c6[max_score] = c6[max_score], c6[i]
        c7[i], c7[max_score] = c7[max_score], c7[i]
        c8[i], c8[max_score] = c8[max_score], c8[i]
        c9[i], c9[max_score] = c9[max_score], c9[i]
        c10[i], c10[max_score] = c10[max_score], c10[i]
        c11[i], c11[max_score] = c11[max_score], c11[i]
        c12[i], c12[max_score] = c12[max_score], c12[i]
        c13[i], c13[max_score] = c13[max_score], c13[i]
        c14[i], c14[max_score] = c14[max_score], c14[i]
        c15[i], c15[max_score] = c15[max_score], c15[i]
        c16[i], c16[max_score] = c16[max_score], c16[i]
        c17[i], c17[max_score] = c17[max_score], c17[i]
        c18[i], c18[max_score] = c18[max_score], c18[i]
        c19[i], c19[max_score] = c19[max_score], c19[i]

    # put data in a dictionary and return data to a template
    output = {
        '1': c1,
        '2': c2,
        '3': c3,
        '4': c4,
        '5': c5,
        '6': c6,
        '7': c7,
        '8': c8,
        '9': c9,
        '10': c10,
        '11': c11,
        '12': c12,
        '13': c13,
        '14': c14,
        '15': c15,
        '16': c16,
        '17': c17,
        #'18': c18,
        #'19': c19,
        #'20': c20
    }

    return render_template('index.html', output=output.items())


if __name__ == '__main__':
    app.run()
