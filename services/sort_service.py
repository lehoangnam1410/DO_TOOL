import pandas as pd

from config import COL_ITEM_CD, COL_PLAN_ERP_QTY


def sort_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sắp xếp:
    - Item Cd tăng dần
    - Plan ERP Qty giảm dần
    """

    df = df.copy()

    item_cd = df.iloc[:, COL_ITEM_CD]
    plan_erp = df.iloc[:, COL_PLAN_ERP_QTY]

    # Ép kiểu số cho ERP (tránh trường hợp đang là text "6,000")
    plan_erp = (
        plan_erp.astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    df["_item_cd"] = item_cd
    df["_plan_erp"] = plan_erp

    df_sorted = df.sort_values(
        by=["_item_cd", "_plan_erp"],
        ascending=[True, False]
    )

    df_sorted = df_sorted.drop(columns=["_item_cd", "_plan_erp"])

    return df_sorted