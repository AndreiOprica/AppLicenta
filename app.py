from flask import Flask, render_template
import sqlite3
import copy

app = Flask(__name__)


def compute_tf(word_dict, bow):

    tf_dict = {}
    bow_count = len(bow)

    for word, count in word_dict.items():
        tf_dict[word] = count/float(bow_count)

    return tf_dict


def compute_idf(doc_list):

    import math
    idf_dict = {}
    N = len(doc_list)
    idf_dict = dict.fromkeys(doc_list[0].keys(), 0)

    for doc in doc_list:
        for word, val in doc.items():
            if val > 0:
                idf_dict[word] += 1

    for word, val in idf_dict.items():
        idf_dict[word] = math.log10(N / float(val))

    return idf_dict


def compute_tfidf(tf_bow, idfs):

    tfidf = {}

    for word, val in tf_bow.items():
        tfidf = val * idfs[word]

    return tfidf


@app.route('/')
def start_page():
    return render_template('index.html')


@app.route('/ComputerScience')
def computer_science():

    # connect to database, extract data and put data in lists
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM ComputerScience')

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
    c20 = []

    for row in cur:
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

    # calculate score and add it to lists
    for i in range(len(c13)):
        bow_category = c13[i].split(" ")
        bow_description = c15[i].split(" ")

        word_set = set(bow_category).union(set(bow_description))

        word_dict_category = dict.fromkeys(word_set, 0)
        word_dict_description = dict.fromkeys(word_set, 0)

        for word in bow_category:
            word_dict_category[word] += 1

        for word in bow_description:
            word_dict_description[word] += 1

        tf_bow_category = compute_tf(word_dict_category, bow_category)
        tf_bow_description = compute_tf(word_dict_description, bow_description)

        idfs = compute_idf([word_dict_category, word_dict_description])

        tfidf_bow_category = compute_tfidf(tf_bow_category, idfs)
        tfidf_bow_description = compute_tfidf(tf_bow_description, idfs)

        c20.append((tfidf_bow_category + tfidf_bow_description))

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

    for i in range(len(c20)):
        if c15[i] == '':
            del c1[i]
            del c2[i]
            del c3[i]
            del c4[i]
            del c5[i]
            del c6[i]
            del c7[i]
            del c8[i]
            del c9[i]
            del c10[i]
            del c11[i]
            del c12[i]
            del c13[i]
            del c14[i]
            del c15[i]

    # put data in a dictionary and return data to a template

    output = {}

    for i in range(len(c1)):
        lst = [c1[i], c2[i], c3[i], c4[i], c5[i], c6[i], c7[i], c8[i], c9[i], c10[i], c11[i], c12[i], c13[i], c15[i], c20[i]]
        output[i] = copy.copy(lst)

    return render_template('computerScience.html', output=output.items())


@app.route('/MachineLearning')
def machine_learning():

    # connect to database, extract data and put data in lists
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM MachineLearning')

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
    c20 = []

    for row in cur:
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

    # calculate score and add it to lists
    for i in range(len(c13)):
        bow_category = c13[i].split(" ")
        bow_description = c15[i].split(" ")

        word_set = set(bow_category).union(set(bow_description))

        word_dict_category = dict.fromkeys(word_set, 0)
        word_dict_description = dict.fromkeys(word_set, 0)

        for word in bow_category:
            word_dict_category[word] += 1

        for word in bow_description:
            word_dict_description[word] += 1

        tf_bow_category = compute_tf(word_dict_category, bow_category)
        tf_bow_description = compute_tf(word_dict_description, bow_description)

        idfs = compute_idf([word_dict_category, word_dict_description])

        tfidf_bow_category = compute_tfidf(tf_bow_category, idfs)
        tfidf_bow_description = compute_tfidf(tf_bow_description, idfs)

        c20.append((tfidf_bow_category + tfidf_bow_description))

    for i in range(len(c20)):
        max_score = i
        for j in range(i + 1, len(c20)):
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

    for i in range(len(c20)):
        if c15[i] == '':
            del c1[i]
            del c2[i]
            del c3[i]
            del c4[i]
            del c5[i]
            del c6[i]
            del c7[i]
            del c8[i]
            del c9[i]
            del c10[i]
            del c11[i]
            del c12[i]
            del c13[i]
            del c14[i]
            del c15[i]

    # put data in a dictionary and return data to a template

    output = {}

    for i in range(len(c1)):
        lst = [c1[i], c2[i], c3[i], c4[i], c5[i], c6[i], c7[i], c8[i], c9[i], c10[i], c11[i], c12[i], c13[i], c15[i], c20[i]]
        output[i] = copy.copy(lst)

    return render_template('machineLearning.html', output=output.items())


if __name__ == '__main__':
    app.run()
