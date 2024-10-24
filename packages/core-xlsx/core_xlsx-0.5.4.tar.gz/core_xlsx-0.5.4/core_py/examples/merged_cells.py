from core_xlsx import XLSXSheet


if __name__ == "__main__":
    sheet = XLSXSheet("A", 1)

    print("Sheet", sheet)

    sheet.write_cell(20, 20, "Жопа")
    sheet.set_merged_cells(1, 3, 1, 3)

    for cell in sheet.cells:
        if cell.is_merge:
            print(
                "Cell",
                cell.cell,
                "row:",
                cell.row,
                "col:",
                cell.column,
                "merged:",
                cell.start_row,
                cell.end_row,
                cell.start_column,
                cell.end_column,
            )
