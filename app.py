import re

from flask import Flask, render_template
import sqlite3
app = Flask(__name__)





@app.route('/')
def hello_world():
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
        if (row[1][0] == 'L' and row[1][1] == 'i' and row[1][2] == 'n' and row[1][3] == 'k' and row[1][4] == ':'):
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
            c20.append(row[19])
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
        '18': c18,
        '19': c19,
        '20': c20
    }
    return render_template('index.html', output=output.items())
    #return 'Hello World!'


if __name__ == '__main__':
    app.run()
