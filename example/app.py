from flask import Flask, render_template, request, send_from_directory
import subprocess
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


CSV_FILES = {
    "courses": "courses.csv",
    "rooms": "rooms.csv",
    "time_slots": "time_slots.csv"
}

@app.route("/", methods=["GET", "POST"])
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
            ["python", "example.py"],
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

