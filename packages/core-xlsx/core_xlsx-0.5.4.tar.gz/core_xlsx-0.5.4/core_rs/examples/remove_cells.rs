use anyhow::Result;
use core_rs::{helper::HelperSheet, types::XLSXSheet};

fn main() -> Result<()> {
    let helper = HelperSheet::new(Vec::from([XLSXSheet::new("ЦП".to_string(), 1, 10, 10)]));

    if let Some(mut sheet) = helper.find_sheet_by_index(1)? {
        for r in 1..=10 {
            for c in 1..=10 {
                sheet.write_cell(r, c, format!("Значение {}: {}", r, c))?;
            }
        }

        let _ = sheet.delete_cols(4, 4);
        let _ = sheet.delete_rows(4, 4);

        for c in sheet.cells {
            println!(
                "Cell {:?} [row: {}, col: {}]: value: {:?}",
                c.cell, c.row, c.column, c.value
            );
        }

        println!("{:?}: {:?}", sheet.max_row, sheet.max_column);
    }

    Ok(())
}
