from flask import Flask, request, render_template, url_for, redirect
import bot
import uuid
import os

app = Flask(__name__, subdomain_matching=True)

HOSTNAME = str(os.getenv('HOSTNAME', '127.0.0.1'))
PORT = str(os.getenv('PORT', '5001'))

pages = {}

@app.route('/', methods=['GET', 'POST'])
def task1():
    if request.method == 'POST':
        page = request.form.get('query')
        new_id = str(uuid.uuid4())
        pages[new_id] = {'content': page} 

        return redirect(url_for('new_page', page_id=new_id))

    return render_template('index.html') 

@app.route('/pages/<page_id>', methods=['GET', 'POST'])
def new_page(page_id):
    if request.method == 'POST':
        id = request.form.get('id')
        if id and 'http://' not in id:
            bot.check_url((HOSTNAME + ':' + PORT), id)
            return render_template('success.html')
        else:
            return '<h2>Ты должен отправить страничку из нашего сайта!</h2><br><a href='/'>На главную</a>', 400 

    page = pages.get(page_id)
    if page:
        return render_template('new_page.html', content=page['content'], page_id=page_id) 
    else:
        return '<h2>Такой странички нет!</h2><br><a href='/'>На главную</a>', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(PORT))
