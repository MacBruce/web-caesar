from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True




form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>

    <form action="/" method="post">
        <label for="rot">Rotate By:
            <input type="text" name="rot">
        </label>


        <textarea name="text" rows="8" cols="80">{0}</textarea>


        <input type="submit" value="Submit Query">

    </form>
    </body>
</html>

        '''

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rotated_int = int(rot)

    text_str = request.form['text']

    encrypted_str = rotate_string(text_str, rotated_int)

    return form.format(encrypted_str)







app.run()
