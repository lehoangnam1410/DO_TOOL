import pandas as pd
from config import COL_ITEM_CD


def filter_by_unit(df: pd.DataFrame, valid_items: set) -> pd.DataFrame:
    """
    Chỉ giữ lại Item Cd nằm trong sheet Unit
    """

    df = df.copy()

    item_cd = df.iloc[:, COL_ITEM_CD].astype(str).str.strip()

    return df[item_cd.isin(valid_items)]