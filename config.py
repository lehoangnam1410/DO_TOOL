# =========================
# FILE CONFIG CHUNG
# =========================

# Folder
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"
LOG_FOLDER = "logs"

# File mặc định
INPUT_FILE_NAME = "Data.xlsx"
OUTPUT_FILE_NAME = "Result.xlsx"

# Sheet names
SHEET_DATA = "Data"
SHEET_RESULTS = "Results"

# =========================
# BUSINESS RULES
# =========================

# Layout rule
LAYOUT_LIMIT = 32  # bỏ Layout >= 32

# ERP rule
ERP_PERCENT = 0.1  # lấy 10%

# Max rows per Item Cd (nếu có rule giới hạn sau này)
MAX_ROWS_PER_ITEM = 15

# =========================
# COLUMN INDEX (theo Excel A=0)
# =========================

COL_SUPPLIER_ID = 0
COL_SUPPLIER_NAME = 1

COL_ITEM_CD = 2
COL_ITEM_NAME = 3

COL_LAYOUT_CODE = 4

COL_SHIPTO_ID = 5
COL_SHIPTO_NAME = 6

COL_PLAN_ERP_QTY = 7
COL_ACTUAL_ERP_QTY = 8

COL_INPUT_QTY = 9

COL_ACTUAL_WEIGHT_QTY = 10

COL_PICK_TYPE = 11