from flask import Flask, render_template

app = Flask(__name__, 
            template_folder ="siteciencia/templates",)

@app.route("/")
def index():
    # return "<h1>bom dia, professor.</h1>"
    return render_template("index.html")
