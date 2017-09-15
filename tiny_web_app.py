from flask import Flask, Response, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    response = '''<?xml version="1.0" encoding="UTF-8"?>
                    <Response>
                        <Say>Hello, Mike! You have been rick rolled.</Say>
                        <Play>https://api.twilio.com/cowbell.mp3</Play>
                        <Play>https://afternoon-gorge-22076.herokuapp.com/rick_roll.mp3</Play>
                    </Response>'''
    return Response(response, mimetype='text/xml')

@app.route('/rick_roll.mp3', methods=['GET', 'POST'])
def song():
    response = flask.make_response(render_template('audio.html'))

    response.headers['Content-Type'] = 'audio/mp3'
    return response


if __name__ == '__main__':
    app.run(debug=True)