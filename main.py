from flask import Flask
from flask import url_for
app = Flask(__name__)



@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                            <title>Привет, Марс</title>
                        </head>
                        <body>
                            <h1>Жди нас, Марс</h1>
                            <br>
                            <img src="{url_for('static', filename='img/scale_1200.png')}" 
                                alt="вот она какая красная планета">
                            <br>
                            вот она какая красная планета
                        </body>
                    </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')