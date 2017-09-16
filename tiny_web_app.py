from flask import Flask, make_response, Response, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    response = '''<?xml version="1.0" encoding="UTF-8"?>
                    <Response>
                        <Say>Hello there Jacob. It's your good buddy Mike. Happy Friday. Also, you have just been rick rolled.</Say>
                        <Play>https://afternoon-gorge-22076.herokuapp.com/rick_roll.mp3</Play>
                    </Response>'''
    return Response(response, mimetype='text/xml')

@app.route('/rick_roll.mp3')
def song():

    return app.send_static_file('rick_roll.mp3')


if __name__ == '__main__':
    app.run(debug=True)