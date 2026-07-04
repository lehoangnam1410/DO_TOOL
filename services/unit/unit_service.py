import pandas as pd
from config import SHEET_DATA


def get_valid_items(workbook: dict[str, pd.DataFrame]) -> set:
    """
    Lấy danh sách Item Cd hợp lệ từ sheet Unit
    """

    if "Unit" not in workbook:
        raise ValueError("Không tìm thấy sheet Unit")

    unit_df = workbook["Unit"].copy()

    item_set = set(unit_df.iloc[:, 0].astype(str).str.strip())

    return item_set