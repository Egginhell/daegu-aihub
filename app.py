from flask import Flask
import sqlite3
app = Flask(__name__)
@app.route('/')
def home():
    cnt = sqlite3.connect('topics.db')
    result = cnt.execute('SELECT * FROM topic')
    



    return "Hello Flask"
app.run(debug=True)