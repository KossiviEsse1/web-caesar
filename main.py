from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
      <form method="POST">
        <label for="rot">Rotate By:</label>
            <input type="text" name="rot" value="0"/>
        </label>
            <br><br>
            <textarea name="textarea">
            {0}
            </textarea>
            <br><br>
            <input type="submit" value= "Submit Query">
      </form>
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['textarea']
    code = ""
    for i in range(len(text)):
        code += rotate_string(text[i], rot)
    return form.format(code)

@app.route("/")
def index():
    return form.format("")

app.run()