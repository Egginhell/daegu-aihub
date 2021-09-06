
import sqlite3


cnt = sqlite3.connect('topics.db')
result = cnt.execute('SELECT * FROM topic')
rows = result.fetchall()
print('rows', rows)


# @app.route('/')
# def home():
#     cnt = sqlite3.connect('topics.db')
#     result = cnt.execute('SELECT * FROM topic')
#     topics = result.fetchall()
#     print('topics', topics)
#     contents = '<h1><a href="/">Web</a></h1>'
#     contents += '<ol>'3
#     for id, title,body in topics: 
#         contents += '<li><a href="/read/'+str(id)+'">'+title+'</a></li>'
#     contents += '</ol>'
#     contents +='<h2>Welcome</h2>Hello, WEB'
#     return contents+'<p><a href="/create">create</a></p>'

# app.run()
