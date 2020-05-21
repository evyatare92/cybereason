from flask import Flask, render_template
import json

app = Flask(__name__)
file_path = "/mongo/db_export/users.json"

@app.route('/', methods=['GET'])
def show_data():
    with open(file_path, "r") as infile:
        users = json.load(infile)
    return render_template("data.html", users= users)

app.run(host="0.0.0.0", port=80, debug=False)