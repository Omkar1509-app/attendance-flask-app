import pandas as pd
from datetime import date
FILE_PATH = ""
def load_data():
    return pd.read_excel(FILE_PATH)
def show_today_attendance():
    df = load_data()
        today =
        date.today().strftime("")
    