use anyhow::Result;
use core_rs::{helper::HelperSheet, types::XLSXSheet};

fn main() -> Result<()> {
    let mut sheets = Vec::with_capacity(5);
    for i in 1..=5 {
        let sheet_name = format!("Лист {}", i);
        sheets.push(XLSXSheet::new(sheet_name, i, 1, 1));
    }

    let helper = HelperSheet::new(sheets);

    let s = helper.find_sheet_by_name("Лист 1")?;
    println!("Find Name: {:?}", s);

    let s = helper.find_sheet_by_index(1)?;
    println!("Find Index: {:?}", s);

    let s = helper.find_sheet_by_pattern("3$")?;
    println!("Find Pattern: {:?}", s);

    let s = helper.get_sheets_with_names(Vec::from(["Лист 1".to_string(), "Лист 2".to_string()]));
    println!("Find With names: {:?}", s);

    let s =
        helper.get_sheets_without_names(Vec::from(["Лист 1".to_string(), "Лист 2".to_string()]));
    println!("Find Without Names: {:?}", s);

    Ok(())
}
