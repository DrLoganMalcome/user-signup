from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form="""<!DOCTYPE html><html>
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
      
      <form name="form" method="post">
        Rotate by: <input text="rotate" name="rotate" ></input>
        <textarea name ="textarea1">{0}</textarea>
        <input type="submit"></input>
      </form>


    </body>
</html>"""


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('welcome.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()