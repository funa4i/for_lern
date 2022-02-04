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


@app.route("/promotion_image")
def protmotion_image():
    return f'''<!doctype html>
                <html lang="ru">
                    <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс</title>
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous"
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    </head>
                    <body>  
                        <h1>Жди на Марс!</h1>' 
                        <img src="{url_for('static', filename='img/scale_1200.png')}" 
                                alt="вот она какая красная планета"> 
                        <p>Человечество вырастает из детства.</p>
                        <div class="alert alert-success" role="alert"> Человечеству мала одна планета! </div>
                        <p2>Мы сделаем обитаемыми безжизненые пока планеты!</p2>
                        <div class="alert alert-warning" role="alert"> И начнем с марса! </div>
                        <div class="alert alert-danger" role="alert"> Присоеденяйся! </div>
                    </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')