from pathlib import Path
import pandas as pd


def write_excel(df: pd.DataFrame, file_name: str):
    file_path = Path("output") / file_name

    df.to_excel(
        file_path,
        index=False
    )