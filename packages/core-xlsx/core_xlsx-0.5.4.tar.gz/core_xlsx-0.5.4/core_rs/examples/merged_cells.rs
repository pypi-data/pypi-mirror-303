use core_rs::types::XLSXSheet;

fn main() {
    let mut sheet = XLSXSheet::new("A".to_string(), 1, 5, 5);

    println!("Добавление значения в ячейку 20:20");
    let _ = sheet.write_cell(20, 20, "Жопа".to_string());
    let _ = sheet.set_merged_cells(1, 3, 1, 3);

    for cell in sheet.cells.iter() {
        // println!("{} -> {}:{}", cell.cell, cell.row, cell.column);

        if cell.is_merge {
            println!(
                "{} -> {}:{} __ is_merge: {:?} [{:?}, {:?}, {:?}, {:?}]",
                cell.cell,
                cell.row,
                cell.column,
                cell.is_merge,
                cell.start_row,
                cell.end_row,
                cell.start_column,
                cell.end_column
            );
        }
    }

    println!("max row: {}, max col: {}", sheet.max_row, sheet.max_column);
    println!("cnt {}", sheet.cells.len());
}
