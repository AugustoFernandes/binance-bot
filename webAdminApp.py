# Запуск python3 webAdminApp.py
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import json

app = Flask(__name__)

# Путь к главной странице
@app.route('/')
def webAdmin():
    return render_template('webAdmin.html')

# Передаем  настройки из веб-админки в index.py
@app.route('/', methods=['POST'])
def setSettings():
    if request.method == 'POST':
        apiKey = request.form['apiKey']
        apiSecret = request.form['apiSecret']
        symbol = request.form['symbol']
        settings = "API_KEY = \"%s\"\nAPI_SECRET = \"%s\"\nsmbl = \"%s\"\n"%(apiKey, apiSecret, symbol)
        with open("index.py","r+") as f:
           lines=f.readlines()
           lines[11] = settings
           f.seek(0)
           f.writelines(lines)
           f.close()
        return redirect(url_for('webAdmin'))


# Передаем ордер сетку в start_net.py
@app.route('/ordersNet', methods=['GET',    'POST', 'DELETE'])
def setOrderNet():
    if request.method == 'POST':
        data = request.form.to_dict()
        readyData = []
        def split(data):
            def fetch(data,prefix): return {k: v for k, v in data.items() if k.startswith(prefix)}
            for i in range(21):
                data1 = str(fetch(data, "[%s]"%i))
                data1 = data1.replace('[%s]'%i, '')
                print(data1)
                readyData.append(data1)
                with open("start_net.py","r+") as f:
                    lines=f.readlines()
                    lines[2] = json.dumps(readyData)
                    f.seek(0)
                    f.writelines(lines)
                    f.close()
        split(data)
        with open("start_net.py", "r+") as f:
            line = f.readlines()
            while '"' in line[2]:
                line[2] = line[2].replace('"', ' ')
            for i in range(len(line)):
                while '\n' in line[i]:
                    line[i] = line[i].replace('\n', ' ')
            f.seek(0)
            f.writelines(line)
            f.close()
        return redirect(url_for('setOrderNet'))
    return render_template('ordersNet.html')


# Инициализируем app, app.debug=True позволяет динамически отслеживать изминения в коде
if __name__=='__main__':
    app.debug = True
    app.run()


