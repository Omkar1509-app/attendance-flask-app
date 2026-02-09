from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    names = []
    selected_date = None
    shift = None

    if request.method == "POST":
        file = request.files.get("file")
        shift = request.form.get("shift")
        date_str = request.form.get("date")

        if file and shift and date_str:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            df = pd.read_excel(file_path)
            df["Date"] = pd.to_datetime(df["Date"]).dt.date

            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            present_employees = df[
                (df["Date"] == selected_date)
                & (df["Shift"] == shift)
                & (df["Status"] == "Present")
            ]

            names = present_employees["Name"].tolist()

    return render_template(
        "index.html",
        names=names,
        shift=shift,
        selected_date=selected_date
    )

if __name__ == "__main__":
    app.run()