from flask import Flask, render_template
 

app = Flask(__name__)


@app.route('/')
def main():
    with open('file.txt', 'r', encoding='utf-8') as file:
        resultData = list()
        for line in file.readlines():
            resultData.append(tuple(line.split('\n')[0].split(';')))

    return render_template('base.html', data=resultData)
    # "<h1>Hello, world!</h1><br><a href='/index'>перейти на 2-ю страницу</a"


@app.route('/about')
def about():
    return render_template('about.html')    


if __name__ == '__main__':
    app.run()