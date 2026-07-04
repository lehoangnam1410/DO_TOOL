from services.reader import read_workbook, load_data
from services.unit.unit_service import get_valid_items
from services.unit.filter_unit_service import filter_by_unit
from services.layout_service import filter_layout
from services.sort_service import sort_data
from services.selector_service import select_rows
from services.export_service import export_result


def main():

    # 1. read all sheets
    workbook = read_workbook()

    # 2. unit filter
    valid_items = get_valid_items(workbook)

    # 3. load data sheet
    df = load_data(workbook)

    print("[INFO] Raw:", len(df))

    # 4. filter unit
    df = filter_by_unit(df, valid_items)

    print("[INFO] After unit:", len(df))

    # 5. layout filter
    df = filter_layout(df)

    # 6. sort
    df = sort_data(df)

    # 7. select
    df = select_rows(df)

    # 8. export
    path = export_result(df)
    print("DONE:", path)


if __name__ == "__main__":
    main()