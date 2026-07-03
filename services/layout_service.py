import pandas as pd

from config import COL_LAYOUT_CODE, LAYOUT_LIMIT


def filter_layout(df: pd.DataFrame) -> pd.DataFrame:
    """
    Loại bỏ các dòng có Layout Code >= LAYOUT_LIMIT
    """

    df = df.copy()
    # Lấy cột Layout Code theo index (an toàn với Excel)
    layout_series = df.iloc[:, COL_LAYOUT_CODE]

    # Ép về string để xử lý an toàn (tránh lỗi mixed type)
    layout_series = layout_series.astype(str)

    # Lấy 2 ký tự đầu (ví dụ: "32-0001" -> "32")
    layout_prefix = layout_series.str[:2]

    # Ép sang số để so sánh
    layout_number = pd.to_numeric(layout_prefix, errors="coerce")

    # Filter điều kiện < 32
    df_filtered = df[layout_number < LAYOUT_LIMIT].copy()

    return df_filtered