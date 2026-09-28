from pathlib import Path
import pandas as pd

CSV_PATH=Path(__file__).parent.parent.parent/"data"/"amazon_books.csv"


def load_books():
 df=pd.read_csv(CSV_PATH)
 return df

   




