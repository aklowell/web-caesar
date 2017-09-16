from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <!--create form here-->
        
        <form method = "post">
            <label for = "places">Rotate by:</label>
            <input id = "places" type = "text" name = "rot" value = "0" /><br>
            
            <input type = "textarea" name = "text" /><br>
            
            <input type = "submit" value = "Submit query"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    message = rotate_string(text,rot)
    return '<h1>' + message + '</h1>'


app.run()