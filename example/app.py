from flask import Flask, render_template, request, send_from_directory, session, redirect, url_for
import subprocess
import os
from functools import wraps
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASIC_AUTH_PASSWORD = os.environ.get("BASIC_AUTH_PASSWORD")


CSV_FILES = {
    "courses": "courses.csv",
    "rooms": "rooms.csv",
    "time_slots": "time_slots.csv"
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'password' not in session or session['password'] != BASIC_AUTH_PASSWORD:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == BASIC_AUTH_PASSWORD:
            session['password'] = password
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
    return render_template("login.html")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    result_ready = False

    if request.method == "POST":
        # Save uploaded CSVs (if provided)
        for key, filename in CSV_FILES.items():
            file = request.files.get(key)
            if file and file.filename:
                file.save(os.path.join(BASE_DIR, filename))

        # Run the existing script
        subprocess.run(
            ["python3", "example.py"],
            cwd=BASE_DIR,
            check=True
        )

        result_ready = True

    return render_template("index.html", result_ready=result_ready)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(BASE_DIR, filename, as_attachment=True)

@app.route("/image/<filename>")
def image_file(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=True)

