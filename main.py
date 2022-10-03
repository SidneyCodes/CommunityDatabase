from flask import Flask, render_template, request

app = Flask('app')

# Accessing SQLite database
import openpyxl
import sqlite3
import os
from typeO import typeO
from typeN import typeN
from lgbt import lgbt
from pregnancy import pregnancy

#checks whether the db file exists & returns True or False
f = os.path.isfile('commres.db')

# if f returns False(i.e. DB file doesnt exist) then functions are
# called to retrieve excel sheets and copy them to SQLite database

if f == False:
    print('Copying Excel data to SQLite database')

    lgbt('LGBTQ2S+')
    pregnancy('Pregnancy')

    osheets = ['Addictions','AIDS Hepatitis C','Bereavement', \
               'Anger Management','Black Lives','Brain InjuryTumour',\
               'Clothing Donations', 'Community Programs', 'Disability',\
               'Education','Emergency Services','Employment Services',\
               'Family Services','Financial','Government',\
               'Healthcare','Housing','Legal Assistance',\
               'Newcomers','Older Adults','Transportation' \
              ]
    [typeO(osheet) for osheet in osheets]

    nsheets = ['Francophones','Food Banks','Abuse','Homelessness','Indigenous People',\
               'Mental Health','Youth' \
              ]
    [typeN(nsheet) for nsheet in nsheets]

    print('Data processing complete')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/abuse', methods=["GET", "POST"])
def abuse():
    category = ''
    #search = ''

    #Connecting to sqlite database
    con = sqlite3.connect("commres.db")

    con.row_factory = sqlite3.Row

    # Creating a cursor object using the cursor() method
    cur = con.cursor()

    data = cur.execute('SELECT * FROM abuse')

    cols = data.description
    #for col in cols:
    # print(col[0])
    print()

    rows = cur.fetchall()
    con.close()

    #if requesting method is post, which is the method
    #specified in each form
    #we get the input data from these HTML forms
    if request.method == "POST":
        category = request.form["category"]
        print(category)

        #search = request.form.get("search")
        #print(search)

        #Connecting to sqlite database
        con = sqlite3.connect("commres.db")

        con.row_factory = sqlite3.Row

        # Creating a cursor object using the cursor() method
        cur = con.cursor()

        #If the user selects the category 'all' in the webpage, the first statement will be executed
        if category == 'all':
            data = cur.execute(f'SELECT * FROM abuse')
        else:
            data = cur.execute(f'SELECT * FROM abuse \
                          WHERE category LIKE "%{category}%";')

        cols = data.description
        rows = cur.fetchall()
        con.close()

    return render_template("abuse.html", rows=rows, cols=cols)


@app.route('/addictions', methods=["GET", "POST"])
def addictions():
    category = ''
    #search = ''

    #Connecting to sqlite database
    con = sqlite3.connect("commres.db")

    con.row_factory = sqlite3.Row

    # Creating a cursor object using the cursor() method
    cur = con.cursor()

    data = cur.execute('SELECT * FROM addictions')

    cols = data.description
    #for col in cols:
    # print(col[0])
    print()

    rows = cur.fetchall()
    con.close()

    #if requesting method is post, which is the method
    #specified in each form
    #we get the input data from these HTML forms
    if request.method == "POST":
        category = request.form["category"]
        print(category)

        #search = request.form.get("search")
        #print(search)

        #Connecting to sqlite database
        con = sqlite3.connect("commres.db")

        con.row_factory = sqlite3.Row

        # Creating a cursor object using the cursor() method
        cur = con.cursor()

        #If the user selects the category 'all' in the webpage, the first statement will be executed
        if category == 'all':
            data = cur.execute(f'SELECT * FROM addictions')
        else:
            data = cur.execute(f'SELECT * FROM addictions \
                          WHERE category LIKE "%{category}%";')

        cols = data.description
        rows = cur.fetchall()
        con.close()

    return render_template("addictions.html", rows=rows, cols=cols)

@app.route('/aids_hep_c', methods=["GET", "POST"])
def aids_hep_c():
    category = ''
    #search = ''

    #Connecting to sqlite database
    con = sqlite3.connect("commres.db")

    con.row_factory = sqlite3.Row

    # Creating a cursor object using the cursor() method
    cur = con.cursor()

    data = cur.execute('SELECT * FROM aids_hepatitis_c')

    cols = data.description
    #for col in cols:
    # print(col[0])
    print()

    rows = cur.fetchall()
    con.close()

    #if requesting method is post, which is the method
    #specified in each form
    #we get the input data from these HTML forms
    if request.method == "POST":
        category = request.form["category"]
        print(category)

        #search = request.form.get("search")
        #print(search)

        #Connecting to sqlite database
        con = sqlite3.connect("commres.db")

        con.row_factory = sqlite3.Row

        # Creating a cursor object using the cursor() method
        cur = con.cursor()

        #If the user selects the category 'all' in the webpage, the first statement will be executed
        if category == 'all':
            data = cur.execute(f'SELECT * FROM aids_hepatitis_c')
        else:
            data = cur.execute(f'SELECT * FROM aids_hepatitis_c \
                          WHERE category LIKE "%{category}%";')

        cols = data.description
        rows = cur.fetchall()
        con.close()

    return render_template("aids_hep_c.html", rows=rows, cols=cols)

@app.route('/bereavement', methods=["GET", "POST"])
def bereavement():
    category = ''
    #search = ''

    #Connecting to sqlite database
    con = sqlite3.connect("commres.db")

    con.row_factory = sqlite3.Row

    # Creating a cursor object using the cursor() method
    cur = con.cursor()

    data = cur.execute('SELECT * FROM bereavement')

    cols = data.description
    #for col in cols:
    # print(col[0])
    print()

    rows = cur.fetchall()
    con.close()

    #if requesting method is post, which is the method
    #specified in each form
    #we get the input data from these HTML forms
    if request.method == "POST":
        category = request.form["category"]
        print(category)

        #search = request.form.get("search")
        #print(search)

        #Connecting to sqlite database
        con = sqlite3.connect("commres.db")

        con.row_factory = sqlite3.Row

        # Creating a cursor object using the cursor() method
        cur = con.cursor()

        #If the user selects the category 'all' in the webpage, the first statement will be executed
        if category == 'all':
            data = cur.execute(f'SELECT * FROM bereavement')
        else:
            data = cur.execute(f'SELECT * FROM bereavement \
                          WHERE category LIKE "%{category}%";')

        cols = data.description
        rows = cur.fetchall()
        con.close()

    return render_template("bereavement.html", rows=rows, cols=cols)

@app.route('/community_programs', methods=["GET", "POST"])
def community_programs():
    category = ''
    #search = ''

    #Connecting to sqlite database
    con = sqlite3.connect("commres.db")

    con.row_factory = sqlite3.Row

    # Creating a cursor object using the cursor() method
    cur = con.cursor()

    data = cur.execute('SELECT * FROM community_programs')

    cols = data.description
    #for col in cols:
    # print(col[0])
    print()

    rows = cur.fetchall()
    con.close()

    #if requesting method is post, which is the method
    #specified in each form
    #we get the input data from these HTML forms
    if request.method == "POST":
        category = request.form["category"]
        print(category)

        #search = request.form.get("search")
        #print(search)

        #Connecting to sqlite database
        con = sqlite3.connect("commres.db")

        con.row_factory = sqlite3.Row

        # Creating a cursor object using the cursor() method
        cur = con.cursor()

        #If the user selects the category 'all' in the webpage, the first statement will be executed
        if category == 'all':
            data = cur.execute(f'SELECT * FROM community_programs')
        else:
            data = cur.execute(f'SELECT * FROM community_programs \
                          WHERE category LIKE "%{category}%";')

        cols = data.description
        rows = cur.fetchall()
        con.close()

    return render_template("community_programs.html", rows=rows, cols=cols)


app.run(host='0.0.0.0', port=5000)
