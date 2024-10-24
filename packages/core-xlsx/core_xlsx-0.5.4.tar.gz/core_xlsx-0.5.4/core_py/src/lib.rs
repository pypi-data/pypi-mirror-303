pub(crate) mod helper;
pub(crate) mod services;
pub(crate) mod types;

use helper::{WrapperHelperSheet, WrapperHelperSheetCell};
use pyo3::{
    prelude::*,
    types::{PyDict, PyList},
};
use services::Service;
use types::{WrapperXLSXSheet, WrapperXLSXSheetCell};

/// Преобразование номера колонки в букву.
#[pyfunction]
fn column_number_to_letter(col: u32) -> PyResult<String> {
    Python::with_gil(|_py| {
        let letter = core_rs::utils::column_number_to_letter(col);

        Ok(letter)
    })
}

/// Преобразование данных в json.
#[pyfunction]
fn xlsxheets_to_json(sheets: Vec<WrapperXLSXSheet>) -> PyResult<String> {
    Python::with_gil(|_py| {
        let xlsx_sheets: Vec<core_rs::types::XLSXSheet> = sheets.into_iter().map(|s| s.0).collect();

        let json = core_rs::utils::xlsxheets_to_json(xlsx_sheets);

        Ok(json)
    })
}

/// Преобразование данных в json.
#[pyfunction]
fn xlsxheets_to_dict(py: Python<'_>, sheets: Vec<WrapperXLSXSheet>) -> PyResult<Bound<'_, PyList>> {
    let xlsx_sheets: Vec<core_rs::types::XLSXSheet> = sheets.into_iter().map(|s| s.0).collect();

    let py_vec = PyList::empty_bound(py);
    for sheet in xlsx_sheets.iter() {
        let sheet_dict = PyDict::new_bound(py);

        sheet_dict.set_item("name", &sheet.name)?;
        sheet_dict.set_item("max_row", sheet.max_row)?;
        sheet_dict.set_item("max_column", sheet.max_column)?;
        sheet_dict.set_item("index", sheet.index)?;
        sheet_dict.set_item("main", sheet.main)?;

        let cells_list = PyList::empty_bound(py);
        for cell in &sheet.cells {
            // New
            let cell_dict = PyDict::new_bound(py);

            // Set
            cell_dict.set_item("row", cell.row)?;
            cell_dict.set_item("column", cell.column)?;
            cell_dict.set_item("cell", &cell.cell)?;
            cell_dict.set_item("value", cell.value.get_value_str())?;
            cell_dict.set_item("formula", &cell.formula)?;
            cell_dict.set_item("data_type", &cell.data_type)?;
            cell_dict.set_item("number_format", &cell.number_format)?;
            cell_dict.set_item("cell_type", &cell.cell_type)?;
            cell_dict.set_item("el_type", &cell.el_type)?;
            cell_dict.set_item("is_merge", cell.is_merge)?;
            cell_dict.set_item("start_row", cell.start_row)?;
            cell_dict.set_item("end_row", cell.end_row)?;
            cell_dict.set_item("start_column", cell.start_column)?;
            cell_dict.set_item("end_column", cell.end_column)?;
            cell_dict.set_item("style_id", &cell.style_id)?;
            cell_dict.set_item("hidden_value", &cell.hidden_value)?;
            cell_dict.set_item("comment", &cell.comment)?;
            // append
            cells_list.append(cell_dict)?;
        }
        sheet_dict.set_item("cells", cells_list)?;

        py_vec.append(sheet_dict)?;
    }

    Ok(py_vec)
}

/// Returns the version of the underlying queue_rs library.
///
/// Returns
/// -------
/// version : str
///   The version of the underlying queue_rs library.
///
#[pyfunction]
fn version() -> String {
    core_rs::version().to_string()
}

#[pymodule]
#[pyo3(name = "_core_xlsx")]
fn boriy_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Service>()?;
    m.add_class::<WrapperXLSXSheet>()?;
    m.add_class::<WrapperXLSXSheetCell>()?;
    m.add_class::<WrapperHelperSheet>()?;
    m.add_class::<WrapperHelperSheetCell>()?;

    m.add_function(wrap_pyfunction!(version, m)?)?;
    m.add_function(wrap_pyfunction!(column_number_to_letter, m)?)?;
    m.add_function(wrap_pyfunction!(xlsxheets_to_json, m)?)?;
    m.add_function(wrap_pyfunction!(xlsxheets_to_dict, m)?)?;

    Ok(())
}
