from core_xlsx import XLSXSheet


if __name__ == "__main__":
    sheet = XLSXSheet("A", 1, 100, 100)
    print("Sheet", sheet)

    print("--> min_row=20, max_row=25, min_col=10, max_col=11")
    for c in sheet.iter_cells(min_row=20, max_row=25, min_col=10, max_col=11):
        print("Cell:", c.cell, "row:", c.row, "col:", c.column)

    print("--> min_row=20, max_row=21")
    for c in sheet.iter_cells(min_row=20, max_row=21):
        print("Cell:", c.cell, "row:", c.row, "col:", c.column)

    print("--> min_col=1, max_col=2")
    for c in sheet.iter_cells(min_col=1, max_col=2):
        print("Cell:", c.cell, "row:", c.row, "col:", c.column)
