from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)

user = False
dataa = '0'


# MySQL database configuration
config = {
    'user': 'root',
    'password': 'mudassir',
    'host': 'localhost',
    'database': 'mysql',
    'raise_on_warnings': True
}

# Connect to the MySQL database
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# first login and after login successfully redirect to homepage(index.html)

@app.route('/')
def login():
    print(user, dataa)
    if dataa:
        return render_template('./login.html', data=dataa)

    return render_template('./login.html', data=dataa)


# after login if user is found then go to home page 
# else use the sql payloads to break through
@app.route('/home')
def home():
    if user:
        return render_template('./index.html')
    else:
        return render_template('./login.html')


# this page is for stored xss
# there is also a reset button to reset all data from data base

@app.route('/stored')
def stored():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    sql = "select text from sxss"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    # Close the database connection
    cursor.close()
    conn.close()

    return render_template('./product_stored_xss.html', results=results)


# submit the comment is databace (stored xss)
@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    comment = request.form['comment_p']

    # Insert the form data into the database (I assume you have a valid database connection and cursor)
    insert_query = "INSERT INTO sxss (text) VALUES (%s);"
    cursor.execute(insert_query, (comment,))
    conn.commit()

    # After processing the form data, redirect to the 'stored' route using the 'redirect' function
    return redirect(url_for('stored'))


# remove all coments from database (stored xss)
@app.route('/reset_comments', methods=['POST'])
def reset_comments():

    # Insert data into 'users' table
    insert_query = "DELETE FROM sxss;"
    cursor.execute(insert_query)
    conn.commit()

    sql_query = "select text from sxss"
    cursor.execute(sql_query)
    results = cursor.fetchall()

    return render_template('./product_stored_xss.html', results=results)


# search anything in database example: cycle
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')

    # Fetch data from the database
    sql = "select item from items where item ='"+query+"';"
    cursor.execute(sql)
    results = cursor.fetchall()

    return render_template('search.html', results=results)

# after login if user is found then go to home page 
# else use the sql payloads to break through
@app.route('/userlogin', methods=['POST'])
def userlogin():
    user_input = request.form['user_input']

    # Execute the SQL query to check if the user exists in the database
    # create a 'users1234' table with column 'name' and add the users inside that column
    sql = "SELECT 1 FROM users1234 WHERE name = '"+user_input+"' LIMIT 1;"
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        user = True
        return render_template('./index.html')
    else:
        dataaa = 'No user'
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)


# cursor.close()
# conn.close()



# these are the sql queries that needs to be run in the sql database


# 1. create a 'users1234' table with column 'name' and add the users inside that column

# 2. this is for the search bar
# create table items(item varchar(50) not null);
# insert into items(item) value('c3');



# 3. this is for the stored xss
# create table sxss(text varchar(50) not null);
# insert into sxss(text) value('it is a amazing cycle');
# insert into sxss(text) value('cycle is good');
# select exists(select text from sxss where text ='c1');
























