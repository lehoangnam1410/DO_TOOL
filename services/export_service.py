import pandas as pd
from pathlib import Path

from config import OUTPUT_FOLDER, OUTPUT_FILE_NAME, SHEET_RESULTS


def export_result(df: pd.DataFrame, file_name: str = None) -> str:
    """
    Export DataFrame ra file Excel (sheet Results)
    """

    if file_name is None:
        file_name = OUTPUT_FILE_NAME

    output_path = Path(OUTPUT_FOLDER) / file_name

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.to_excel(
            writer,
            sheet_name=SHEET_RESULTS,
            index=False
        )

    return str(output_path)