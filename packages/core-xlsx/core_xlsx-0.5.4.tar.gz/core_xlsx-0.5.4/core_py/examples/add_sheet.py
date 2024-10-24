from core_xlsx import XLSXSheet


if __name__ == "__main__":
    sheet = XLSXSheet("A", 1)
    print("Sheet", sheet)

    print("Write Cell 100x100")
    sheet.write_cell(100, 100, "Жопа")
    sheet.write_cell_with_formula(99, 99, "Жопа с формулой", "SUM(A1:A100)")

    sheet.write_style_for_cell(100, 100, "StyleID")

    print("Sheet", sheet)

    cell = sheet.find_cell_by_coordinate(99, 99)
    print(
        "Find Cell 99x99 value:",
        cell.value if cell else cell,
        "formula:",
        cell.formula if cell else cell,
    )

    cell = sheet.find_cell_by_coordinate(100, 100)
    print(
        "Find Cell 100x100 value:",
        cell.value if cell else cell,
        "StyleID:",
        cell.style_id if cell else cell,
    )
