from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads'
app.secret_key = 'your_secret_key'

# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        file = request.files.get("file")
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for("success", name=name, age=age))
    return render_template("index.html")


@app.route("/success")
def success():
    name = request.args.get("name")
    age = request.args.get("age")
    return f"<h1>Submission Successful!</h1><p>Name: {name}</p><p>Age: {age}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
