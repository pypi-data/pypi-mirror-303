use anyhow::Result;
use core_rs::{helper::HelperSheet, types::XLSXSheet};

fn main() -> Result<()> {
    let helper = HelperSheet::new(Vec::from([XLSXSheet::new("ЦП".to_string(), 1, 100, 100)]));

    if let Some(mut sheet) = helper.find_sheet_by_index(1)? {
        for r in 1..=15 {
            for c in 1..=15 {
                sheet.write_cell(r, c, format!("Значение {}", r + c))?;
            }
        }

        let cell = sheet.find_cell_by_cell("A1")?;
        println!("Find Cell [A1]: {:?}\n", cell);

        let cell = sheet.find_cell_by_coordinate(1, 2)?;
        println!("Find Coordinate [1, 2]: {:?}\n", cell);

        let cell = sheet.find_cell_pattern_regex("Значение 10$")?;
        println!("Find Cell Pattern [Значение 10$]: {:?}\n", cell);

        let cells = sheet.find_cells_pattern_regex("Значение 15$")?;
        println!("Find Cells Pattern [Значение 15$]: {:?}\n", cells);

        let cells = sheet.find_cells_between_patterns("2$", "3$")?;
        println!("Find Cells Between Pattern [2$, 5$]: {:?}\n", cells);

        let cells = sheet.find_cells_multi_pattern_regex("^Значение 1$", "^Значение 2$")?;
        println!(
            "Find Cells Multi Pattern [^Значение 1$, ^Значение 2$]: {:?}\n",
            cells
        );

        let cells = sheet.find_cells_for_rows_pattern_regex("10$", Some(1))?;
        println!("Find Cells For Rows [10$, 1]: {:?}\n", cells);

        let cells = sheet.find_cells_for_cols_pattern_regex("10$", Some(1))?;
        println!("Find Cells For Cols [10$, 1]: {:?}\n", cells);

        let cells = sheet.find_cells_by_range_rows(2, 3)?;
        for c in cells {
            println!("Cell{:?}, row: {:?}, col: {:?}", c.cell, c.row, c.column);
        }

        let cells = sheet.find_cells_by_range_cols(2, 3)?;
        for c in cells {
            println!("Cell{:?}, row: {:?}, col: {:?}", c.cell, c.row, c.column);
        }
    }

    Ok(())
}
