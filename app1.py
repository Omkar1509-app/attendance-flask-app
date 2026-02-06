from flask import Flask, jsonify, request
import pandas as pd
from datetime import date

app = Flask(__name__)

# Load Excel once
data = pd.read_excel("Final Master file_200126.xlsx")
data['Date'] = pd.to_datetime(data['Date']).dt.date

@app.route("/attendance", methods=["GET"])
def get_attendance():
    shift = request.args.get("shift")

    if not shift:
       return jsonify({"error": "Shift is required (A/B/C/D)"}), 400

    shift = shift.upper()
    today = date.today()

    present_employees = data[
        (data['Date'] == today) &
        (data['Shift'] == shift) &
        (data['Status'] == 'Present')
    ]

    names = present_employees['Name'].tolist()

    return jsonify({
        "date": str(today),
        "shift": shift,
        "count": len(names),
        "employees": names
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
