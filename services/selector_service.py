import pandas as pd

from config import COL_ITEM_CD, COL_PLAN_ERP_QTY, ERP_PERCENT


def select_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Logic chọn dòng theo từng Item Cd:
    - Tính tổng ERP theo Item Cd
    - target = total * ERP_PERCENT
    - sort sẵn rồi => lấy từ trên xuống
    - cộng dồn đến khi >= target thì dừng
    """

    df = df.copy()

    # ===== chuẩn hoá dữ liệu ERP =====
    plan_erp = (
        df.iloc[:, COL_PLAN_ERP_QTY]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    item_cd = df.iloc[:, COL_ITEM_CD]

    df["_item_cd"] = item_cd
    df["_erp"] = plan_erp

    result_parts = []

    # ===== xử lý từng Item Cd =====
    for item, group in df.groupby("_item_cd", sort=False):

        total = group["_erp"].sum()
        target = total * ERP_PERCENT

        running = 0.0

        selected_index = []

        # group đã sort sẵn từ trước => đi từ trên xuống
        for idx, row in group.iterrows():
            running += row["_erp"]
            selected_index.append(idx)

            if running >= target:
                break

        result_parts.append(df.loc[selected_index])

    result_df = pd.concat(result_parts, ignore_index=True)

    # bỏ cột phụ
    result_df = result_df.drop(columns=["_item_cd", "_erp"])

    return result_df