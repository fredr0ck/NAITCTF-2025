from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

HOSTNAME = str(os.getenv('HOSTNAME', '127.0.0.1'))
PORT = str(os.getenv('PORT', '5003'))

@app.route('/')
def task3():
    return render_template('index.html')

@app.route('/<path:any_path>')
def catch_all(any_path):
    return redirect(url_for('task3'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(PORT))
