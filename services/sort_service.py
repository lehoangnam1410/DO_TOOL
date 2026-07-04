import pandas as pd

from config import (
    COL_DAS_CELL_NO,
    COL_ITEM_CD,
    COL_PLAN_ERP_QTY,
)


def sort_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sắp xếp dữ liệu:
    1. Ưu tiên DAS Cell No. bắt đầu bằng 'B'
    2. Item Cd tăng dần
    3. Plan ERP Qty giảm dần
    """

    df = df.copy()

    das_cell = (
        df.iloc[:, COL_DAS_CELL_NO]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    item_cd = df.iloc[:, COL_ITEM_CD]

    plan_erp = (
        df.iloc[:, COL_PLAN_ERP_QTY]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # Bắt đầu bằng B -> 0, còn lại -> 1
    priority = (~das_cell.str.startswith("B")).astype(int)

    df["_priority"] = priority
    df["_item_cd"] = item_cd
    df["_plan_erp"] = plan_erp

    df_sorted = df.sort_values(
        by=["_priority", "_item_cd", "_plan_erp"],
        ascending=[True, True, False]
    )

    df_sorted = df_sorted.drop(
        columns=["_priority", "_item_cd", "_plan_erp"]
    )

    df_sorted.reset_index(drop=True, inplace=True)

    return df_sorted