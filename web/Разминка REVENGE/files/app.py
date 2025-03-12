from flask import Flask, render_template, redirect, url_for, request, jsonify
import os

app = Flask(__name__)

sizes = []

HOSTNAME = str(os.getenv('HOSTNAME', '127.0.0.1'))
PORT = str(os.getenv('PORT', '5005'))

@app.route('/', methods=["GET", "POST"])
def task5():
    if request.method == 'GET':
        return render_template('test.html')
    elif request.method == 'POST':
            window_size = request.json
            if 'width' in window_size and 'height' in window_size:
                size = f'{window_size["width"]}x{window_size["height"]}'
                for log in sizes:
                    if log['ip'] == request.remote_addr:
                        if size == log['size']:
                            return 'ok'
                        else:
                            return jsonify({'error': "Don't cheat"}), 400
                log = {'ip': f'{request.remote_addr}', 'size': f'{size}'}
                sizes.append(log)
                return 'ok'
            else:
                return jsonify({'error': "Don't cheat"}), 400


if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(PORT))
