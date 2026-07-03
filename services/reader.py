from pathlib import Path
import pandas as pd

from config import INPUT_FOLDER, INPUT_FILE_NAME, SHEET_DATA


def read_workbook(file_name: str = None) -> dict[str, pd.DataFrame]:
    """
    Đọc toàn bộ Excel workbook (multi-sheet)
    """

    if file_name is None:
        file_name = INPUT_FILE_NAME

    file_path = Path(INPUT_FOLDER) / file_name

    return pd.read_excel(
        file_path,
        sheet_name=None,
        engine="openpyxl"
    )


def load_data(workbook: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Lấy sheet Data từ workbook
    """

    if SHEET_DATA not in workbook:
        raise ValueError(f"Không tìm thấy sheet: {SHEET_DATA}")

    df = workbook[SHEET_DATA].copy()

    # clean nhẹ
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()

    return df