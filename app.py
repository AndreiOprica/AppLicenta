from flask import Flask, render_template, request, url_for, redirect
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
    n = len(doc_list)
    idf_dict = dict.fromkeys(doc_list[0].keys(), 0)

    for doc in doc_list:
        for word, val in doc.items():
            if val > 0:
                idf_dict[word] += 1

    for word, val in idf_dict.items():
        idf_dict[word] = math.log10(n / float(val))

    return idf_dict


def compute_tfidf(tf_bow, idfs):

    tfidf = {}

    for word, val in tf_bow.items():
        tfidf[word] = val * idfs[word]

    score = 0
    no = 0
    for word, value in tfidf.items():
        score += value
        no += 1

    score = score / no

    return score


@app.route('/', methods=['GET', 'POST'])
def start_page():
    if request.method == 'POST':
        abstract = request.form["abstract"]
        return redirect(url_for('result', abstract=abstract))

    return render_template('index.html')


@app.route("/result", methods=['GET', 'POST'])
def result():
    abstract = request.form.get('abstract')
    option = request.form.getlist('options')

    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()

    if option[0] == 'option1':
        cur.execute('SELECT * FROM ComputerScience')
        print(option[0])
    elif option[0] == 'option2':
        cur.execute('SELECT * FROM MachineLearning')
        print(option[0])

    c0 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []

    for row in cur:
        c1.append(row[0])
        c2.append(row[1])
        c3.append(row[3])
        c4.append(row[5])
        c5.append(row[7])
        c6.append(row[9])
        c7.append(row[11])
        c8.append(row[12])
        c9.append(row[14])

    # calculate score and add it to lists
    bow_abstract = abstract.split(" ")

    for i in range(len(c8)):
        bow_description = c9[i].split(" ")

        word_set = set(bow_abstract).union(set(bow_description))

        word_dict_abstract = dict.fromkeys(word_set, 0)
        word_dict_description = dict.fromkeys(word_set, 0)

        for word in bow_abstract:
            word_dict_abstract[word] += 1

        for word in bow_description:
            word_dict_description[word] += 1

        tf_bow_abstract = compute_tf(word_dict_abstract, bow_abstract)
        tf_bow_description = compute_tf(word_dict_description, bow_description)

        idfs = compute_idf([word_dict_abstract, word_dict_description])

        tfidf_bow_category = compute_tfidf(tf_bow_abstract, idfs)
        tfidf_bow_description = compute_tfidf(tf_bow_description, idfs)

        c0.append((tfidf_bow_category + tfidf_bow_description))

    for i in range(len(c0)):
        max_score = i
        for j in range(i+1, len(c0)):
            if c0[max_score] < c0[j]:
                max_score = j

        c0[i], c0[max_score] = c0[max_score], c0[i]
        c1[i], c1[max_score] = c1[max_score], c1[i]
        c2[i], c2[max_score] = c2[max_score], c2[i]
        c3[i], c3[max_score] = c3[max_score], c3[i]
        c4[i], c4[max_score] = c4[max_score], c4[i]
        c5[i], c5[max_score] = c5[max_score], c5[i]
        c6[i], c6[max_score] = c6[max_score], c6[i]
        c7[i], c7[max_score] = c7[max_score], c7[i]
        c8[i], c8[max_score] = c8[max_score], c8[i]
        c9[i], c9[max_score] = c9[max_score], c9[i]


    # put data in a dictionary and return data to a template
    output = {}
    lenght = 10
    if len(c1) < lenght:
        lenght = len(c1)
    for i in range(lenght):
        lst = [c0[i], c1[i], c8[i], c9[i], c2[i], c3[i], c4[i], c5[i], c6[i], c7[i]]
        output[i] = copy.copy(lst)

    return render_template('result.html', output=output.items())


@app.route('/ComputerScience')
def computer_science():

    # connect to database, extract data and put data in lists
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM ComputerScience')

    c0 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []

    for row in cur:
        c1.append(row[0])
        c2.append(row[1])
        c3.append(row[3])
        c4.append(row[5])
        c5.append(row[7])
        c6.append(row[9])
        c7.append(row[11])
        c8.append(row[12])
        c9.append(row[14])

    # calculate score and add it to lists
    for i in range(len(c8)):
        bow_category = c8[i].split(" ")
        bow_description = c9[i].split(" ")

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

        c0.append((tfidf_bow_category + tfidf_bow_description))

    for i in range(len(c0)):
        max_score = i
        for j in range(i+1, len(c0)):
            if c0[max_score] < c0[j]:
                max_score = j

        c0[i], c0[max_score] = c0[max_score], c0[i]
        c1[i], c1[max_score] = c1[max_score], c1[i]
        c2[i], c2[max_score] = c2[max_score], c2[i]
        c3[i], c3[max_score] = c3[max_score], c3[i]
        c4[i], c4[max_score] = c4[max_score], c4[i]
        c5[i], c5[max_score] = c5[max_score], c5[i]
        c6[i], c6[max_score] = c6[max_score], c6[i]
        c7[i], c7[max_score] = c7[max_score], c7[i]
        c8[i], c8[max_score] = c8[max_score], c8[i]
        c9[i], c9[max_score] = c9[max_score], c9[i]


    # put data in a dictionary and return data to a template
    output = {}

    for i in range(len(c1)):
        lst = [c1[i], c8[i], c9[i], c2[i], c3[i], c4[i], c5[i], c6[i], c7[i]]
        # to print the scores uncomment the next line:
        # lst.append(c0[i])
        output[i] = copy.copy(lst)

    return render_template('computerScience.html', output=output.items())


@app.route('/MachineLearning')
def machine_learning():

    # connect to database, extract data and put data in lists
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM MachineLearning')

    c0 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []

    for row in cur:
        c1.append(row[0])
        c2.append(row[1])
        c3.append(row[3])
        c4.append(row[5])
        c5.append(row[7])
        c6.append(row[9])
        c7.append(row[11])
        c8.append(row[12])
        c9.append(row[14])

    # calculate score and add it to lists
    for i in range(len(c8)):
        bow_category = c8[i].split(" ")
        bow_description = c9[i].split(" ")

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

        c0.append((tfidf_bow_category + tfidf_bow_description))

    for i in range(len(c0)):
        max_score = i
        for j in range(i+1, len(c0)):
            if c0[max_score] < c0[j]:
                max_score = j

        c0[i], c0[max_score] = c0[max_score], c0[i]
        c1[i], c1[max_score] = c1[max_score], c1[i]
        c2[i], c2[max_score] = c2[max_score], c2[i]
        c3[i], c3[max_score] = c3[max_score], c3[i]
        c4[i], c4[max_score] = c4[max_score], c4[i]
        c5[i], c5[max_score] = c5[max_score], c5[i]
        c6[i], c6[max_score] = c6[max_score], c6[i]
        c7[i], c7[max_score] = c7[max_score], c7[i]
        c8[i], c8[max_score] = c8[max_score], c8[i]
        c9[i], c9[max_score] = c9[max_score], c9[i]


    # put data in a dictionary and return data to a template
    output = {}

    for i in range(len(c1)):
        lst = [c1[i], c8[i], c9[i], c2[i], c3[i], c4[i], c5[i], c6[i], c7[i]]
        # to print the scores uncomment the next line:
        # lst.append(c0[i])
        output[i] = copy.copy(lst)

    return render_template('machineLearning.html', output=output.items())


if __name__ == '__main__':
    app.run()
