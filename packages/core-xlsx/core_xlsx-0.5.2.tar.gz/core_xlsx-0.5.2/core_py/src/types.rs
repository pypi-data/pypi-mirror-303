use chrono::NaiveDateTime;
use core_rs::{
    datatype::CellRawValue,
    types::{XLSXSheet, XLSXSheetCell},
};
use pyo3::{
    exceptions::PyRuntimeError,
    prelude::*,
    types::{PyDict, PyList},
};
use serde::{Deserialize, Serialize};

/// Данный макрос написан для преобразрвания Python объета в структуру Rust
// TODO
macro_rules! extract_sheet {
    ($obj:expr, $($attr:ident),+) => {
        {
            let o = if $obj.is_instance_of::<PyDict>() {
                XLSXSheet {
                    $($attr: $obj.get_item(stringify!($attr))?.extract()?,)+
                    ..Default::default()
                }
            } else {
                XLSXSheet {
                    $($attr: $obj.getattr(stringify!($attr))?.extract()?,)+
                    ..Default::default()
                }
            };

            WrapperXLSXSheet(o)
        }
    };
}

/// Данный макрос написан для преобразрвания Python объета в структуру Rust
// TODO
macro_rules! extract_sheetcell {
    ($obj:expr, $($attr:ident),+) => {
        {
            let o = if $obj.is_instance_of::<PyDict>() {
                XLSXSheetCell {
                    $($attr: $obj.get_item(stringify!($attr))?.extract()?),+,
                    ..Default::default()
                }
            } else {
                XLSXSheetCell {
                    $($attr: $obj.getattr(stringify!($attr))?.extract()?),+,
                    ..Default::default()
                }
            };

            WrapperXLSXSheetCell(o)
        }
    };
}

#[pyclass]
#[pyo3(module = "core_xlsx", name = "XLSXSheet", subclass)]
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WrapperXLSXSheet(pub(crate) XLSXSheet);

impl WrapperXLSXSheet {
    pub(crate) fn from_py(obj: &Bound<'_, PyAny>) -> PyResult<WrapperXLSXSheet> {
        Python::with_gil(|_py| {
            let mut s = extract_sheet!(obj, name, max_row, max_column, index, main);

            let cells_iter = if obj.is_instance_of::<PyDict>() {
                obj.get_item("cells")?
            } else {
                obj.getattr("cells")?
            }
            .downcast::<PyList>()?
            .iter();

            s.0.cells = cells_iter
                .filter_map(|c| WrapperXLSXSheetCell::from_py(&c).ok())
                .map(|w| w.0)
                .collect();

            Ok(s)
        })
    }
}

#[pymethods]
impl WrapperXLSXSheet {
    #[new]
    #[pyo3(signature=(name, index, rows=5, cols=5))]
    pub fn new(name: String, index: i32, rows: u32, cols: u32) -> PyResult<Self> {
        Python::with_gil(|_py| Ok(Self(XLSXSheet::new(name, index, cols, rows))))
    }

    #[getter]
    pub fn name(&self) -> PyResult<String> {
        Python::with_gil(|_py| Ok(self.0.name.clone()))
    }

    #[getter]
    pub fn max_row(&self) -> PyResult<u32> {
        Python::with_gil(|_py| Ok(self.0.max_row))
    }

    #[getter]
    pub fn max_column(&self) -> PyResult<u32> {
        Python::with_gil(|_py| Ok(self.0.max_column))
    }

    #[getter]
    pub fn index(&self) -> PyResult<i32> {
        Python::with_gil(|_py| Ok(self.0.index))
    }

    #[getter]
    pub fn main(&self) -> PyResult<bool> {
        Python::with_gil(|_py| Ok(self.0.main))
    }

    #[getter]
    pub fn cells(&self) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let cells = self
                .0
                .cells
                .iter()
                .map(|c| WrapperXLSXSheetCell(c.clone()))
                .collect::<Vec<WrapperXLSXSheetCell>>();

            Ok(cells)
        })
    }

    pub fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        Python::with_gil(|_py| {
            Ok(format!(
                "XLSXSheet ({}): cells: {}",
                slf.borrow().0.name,
                slf.borrow().0.cells.len()
            ))
        })
    }

    /// Запись ячейки.
    pub fn write_cell(&mut self, row: u32, col: u32, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .write_cell(row, col, value)
                .map_err(|e| PyRuntimeError::new_err(format!("Failed to write cell: {}", e)))
        })
    }

    /// Добавление значения в ячейку по координате с форумлой.
    /// Дополнительно создаются несуществующие ячейки.
    pub fn write_cell_with_formula(
        &mut self,
        row: u32,
        col: u32,
        value: String,
        formula: String,
    ) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .write_cell_with_formula(row, col, value, formula)
                .map_err(|e| {
                    PyRuntimeError::new_err(format!("Failed to write cell with formula: {}", e))
                })
        })
    }

    /// Добавление стиля в существующую ячейку по координате.
    pub fn write_style_for_cell(&mut self, row: u32, col: u32, style_id: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .write_style_for_cell(row, col, style_id)
                .map_err(|e| {
                    PyRuntimeError::new_err(format!("Failed to write style for cell: {}", e))
                })
        })
    }

    /// Добавление стиля в существующую ячейку по координате.
    pub fn write_formula_for_cell(&mut self, row: u32, col: u32, formula: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .write_formula_for_cell(row, col, formula)
                .map_err(|e| {
                    PyRuntimeError::new_err(format!("Failed to write formula for cell: {}", e))
                })
        })
    }

    /// Метод для удаления колонок
    pub fn delete_cols(&mut self, idx: u32, cols: u32) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .delete_cols(idx, cols)
                .map_err(|e| PyRuntimeError::new_err(format!("Failed to delete cols: {}", e)))
        })
    }

    /// Метод для удаления строк
    pub fn delete_rows(&mut self, idx: u32, rows: u32) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .delete_rows(idx, rows)
                .map_err(|e| PyRuntimeError::new_err(format!("Failed to delete rows: {}", e)))
        })
    }

    /// Метод для добавления данных по объединению ячеек.
    pub fn set_merged_cells(
        &mut self,
        start_row: u32,
        end_row: u32,
        start_column: u32,
        end_column: u32,
    ) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_merged_cells(start_row, end_row, start_column, end_column)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Получить список всех ячеек в заданном диапазоне.
    #[pyo3(signature=(min_row=None, max_row=None, min_col=None, max_col=None))]
    pub fn iter_cells(
        &self,
        min_row: Option<u32>,
        max_row: Option<u32>,
        min_col: Option<u32>,
        max_col: Option<u32>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .iter_cells(min_row, max_row, min_col, max_col)
                    .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Поиск ячейки по шаблону
    pub fn find_cell_pattern_regex(&self, pattern: &str) -> PyResult<Option<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cell_pattern_regex(pattern)
                    .map(|cell| cell.map(WrapperXLSXSheetCell))
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Поиск ячеек по шаблону
    pub fn find_cells_pattern_regex(&self, pattern: &str) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cells_pattern_regex(pattern)
                    .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Поиск ячеек колонок для строк которые соответствуют патерну
    #[pyo3(signature=(pattern, col_stop=None))]
    pub fn find_cells_for_rows_pattern_regex(
        &self,
        pattern: &str,
        col_stop: Option<u32>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cells_for_rows_pattern_regex(pattern, col_stop)
                    .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Поиск ячеек строк для колонок которые соответствуют патерну
    #[pyo3(signature=(pattern, row_stop=None))]
    pub fn find_cells_for_cols_pattern_regex(
        &self,
        pattern: &str,
        row_stop: Option<u32>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cells_for_cols_pattern_regex(pattern, row_stop)
                    .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Поиск ячеек с помощью ИЛИ ячейки по патернам
    pub fn find_cells_multi_pattern_regex(
        &self,
        pattern_1: &str,
        pattern_2: &str,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cells_multi_pattern_regex(pattern_1, pattern_2)
                    .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Поиск ячейки по буквенной координате A1 (cell)
    pub fn find_cell_by_cell(&self, cell: &str) -> PyResult<Option<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cell_by_cell(cell)
                    .map(|cell| cell.map(WrapperXLSXSheetCell))
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Поиск ячейки по координате
    pub fn find_cell_by_coordinate(
        &self,
        row: u32,
        col: u32,
    ) -> PyResult<Option<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cell_by_coordinate(row, col)
                    .map(|cell| cell.map(WrapperXLSXSheetCell))
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Поиск ячеек между шаьлонами
    pub fn find_cells_between_patterns(
        &self,
        pattern_after: &str,
        pattern_before: &str,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cells_between_patterns(pattern_after, pattern_before)
                    .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Возвращаем все ячейки, которые находятся в диапазоне строк
    pub fn find_cells_by_range_rows(
        &self,
        start_row: u32,
        end_row: u32,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cells_by_range_rows(start_row, end_row)
                    .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }

    /// Возвращаем все ячейки, которые находятся в диапазоне колонок
    pub fn find_cells_by_range_cols(
        &self,
        start_col: u32,
        end_col: u32,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|py| {
            py.allow_threads(|| {
                self.0
                    .find_cells_by_range_cols(start_col, end_col)
                    .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                    .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
            })
        })
    }
}

#[pyclass]
#[pyo3(module = "core_xlsx", name = "XLSXSheetCell", subclass)]
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WrapperXLSXSheetCell(pub(crate) XLSXSheetCell);

impl WrapperXLSXSheetCell {
    pub(crate) fn from_py(obj: &Bound<'_, PyAny>) -> PyResult<WrapperXLSXSheetCell> {
        // TODO
        Python::with_gil(|_py| {
            let mut s = extract_sheetcell!(
                obj,
                row,
                column,
                cell,
                // value,
                formula,
                data_type,
                number_format,
                cell_type,
                el_type,
                is_merge,
                start_row,
                end_row,
                start_column,
                end_column,
                style_id
            );

            // Временное решение.
            let value = if obj.is_instance_of::<PyDict>() {
                obj.get_item("value")?
                    .extract::<String>()
                    .unwrap_or("".to_string())
            } else {
                obj.getattr("value")?
                    .extract::<String>()
                    .unwrap_or("".to_string())
            };

            s.set_value(value)?;

            Ok(s)
        })
    }
}

#[pymethods]
impl WrapperXLSXSheetCell {
    #[new]
    #[pyo3(signature=(row, col, value=None))]
    pub fn new(row: u32, col: u32, value: Option<String>) -> PyResult<Self> {
        Python::with_gil(|_py| Ok(Self(XLSXSheetCell::new(row, col, value))))
    }

    #[getter]
    pub fn row(&self) -> PyResult<u32> {
        Python::with_gil(|_py| Ok(self.0.row))
    }

    #[getter]
    pub fn column(&self) -> PyResult<u32> {
        Python::with_gil(|_py| Ok(self.0.column))
    }

    #[getter]
    pub fn cell(&self) -> PyResult<String> {
        Python::with_gil(|_py| Ok(self.0.cell.clone()))
    }

    /// Getter для получения значения из ячейки
    #[getter]
    pub fn value(&self) -> PyResult<PyObject> {
        Python::with_gil(|py| {
            Ok(match &self.0.value.raw_value {
                CellRawValue::Empty => py.None(),
                CellRawValue::String(s) => s.into_py(py),
                CellRawValue::Numeric(n) => n.into_py(py),
                CellRawValue::Bool(b) => b.into_py(py),
                CellRawValue::Datetime(d) => d.into_py(py),
            })
        })
    }

    #[getter]
    pub fn formula(&self) -> PyResult<Option<String>> {
        Python::with_gil(|_py| Ok(self.0.formula.clone()))
    }

    #[getter]
    pub fn data_type(&self) -> PyResult<String> {
        Python::with_gil(|_py| Ok(self.0.data_type.clone()))
    }

    #[getter]
    pub fn number_format(&self) -> PyResult<String> {
        Python::with_gil(|_py| Ok(self.0.number_format.clone()))
    }

    #[getter]
    pub fn cell_type(&self) -> PyResult<Option<String>> {
        Python::with_gil(|_py| Ok(self.0.cell_type.clone()))
    }

    #[getter]
    pub fn el_type(&self) -> PyResult<Option<String>> {
        Python::with_gil(|_py| Ok(self.0.el_type.clone()))
    }

    #[getter]
    pub fn is_merge(&self) -> PyResult<bool> {
        Python::with_gil(|_py| Ok(self.0.is_merge))
    }

    #[getter]
    pub fn start_row(&self) -> PyResult<Option<u32>> {
        Python::with_gil(|_py| Ok(self.0.start_row))
    }

    #[getter]
    pub fn end_row(&self) -> PyResult<Option<u32>> {
        Python::with_gil(|_py| Ok(self.0.end_row))
    }

    #[getter]
    pub fn start_column(&self) -> PyResult<Option<u32>> {
        Python::with_gil(|_py| Ok(self.0.start_column))
    }

    #[getter]
    pub fn end_column(&self) -> PyResult<Option<u32>> {
        Python::with_gil(|_py| Ok(self.0.end_column))
    }

    #[getter]
    pub fn style_id(&self) -> PyResult<Option<String>> {
        Python::with_gil(|_py| Ok(self.0.style_id.clone()))
    }

    #[getter]
    pub fn hidden_value(&self) -> PyResult<Option<String>> {
        Python::with_gil(|_py| Ok(self.0.hidden_value.clone()))
    }

    #[getter]
    pub fn comment(&self) -> PyResult<Option<String>> {
        Python::with_gil(|_py| Ok(self.0.comment.clone()))
    }

    pub fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        Python::with_gil(|_py| {
            Ok(format!(
                "XLSXSheetCell [{}]: (row: {} col: {})",
                slf.borrow().0.cell,
                slf.borrow().0.row,
                slf.borrow().0.column,
            ))
        })
    }

    /// Метод для получения значения ячейки.
    pub fn set_value(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_value(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для добавления технического (скрытого) значения
    pub fn set_hidden_value(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0.hidden_value = Some(value);

            Ok(())
        })
    }

    /// Метод для добавления комментария
    pub fn set_comment(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0.comment = Some(value);

            Ok(())
        })
    }

    /// Метод для получения значения ячейки Numbers.
    pub fn set_value_number(&mut self, value: f64) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_value_number(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для получения значения ячейки Bool.
    pub fn set_value_bool(&mut self, value: bool) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_value_bool(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для получения значения ячейки String.
    pub fn set_value_str(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_value_str(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для получения значения ячейки Datetime.
    pub fn set_value_datetime(&mut self, value: NaiveDateTime) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_value_datetime(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для получения значения ячейки String.
    pub fn set_formula(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_formula(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для получения значения ячейки data_type.
    pub fn set_data_type(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_data_type(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для получения значения ячейки number_format.
    pub fn set_number_format(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_number_format(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для получения значения ячейки cell_type.
    pub fn set_cell_type(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_cell_type(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для получения значения ячейки el_type.
    pub fn set_el_type(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_el_type(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для получения флага, ячейка с формулой или нет.
    pub fn is_formula(&self) -> PyResult<bool> {
        Python::with_gil(|_py| {
            self.0
                .is_formula()
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Проверить, является ли значение ячейки boolean
    pub fn is_value_bool(&self) -> PyResult<bool> {
        Python::with_gil(|_py| {
            self.0
                .is_value_bool()
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Проверить, является ли значение ячейки numeric
    pub fn is_value_numeric(&self) -> PyResult<bool> {
        Python::with_gil(|_py| {
            self.0
                .is_value_numeric()
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Проверить, является ли значение ячейки datetime
    pub fn is_value_datetime(&self) -> PyResult<bool> {
        Python::with_gil(|_py| {
            self.0
                .is_value_datetime()
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Проверить, является ли значение ячейки empty
    pub fn is_value_empty(&self) -> PyResult<bool> {
        Python::with_gil(|_py| {
            self.0
                .is_value_empty()
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Метод для добавления стиля к ячейки
    pub fn set_style_id(&mut self, value: String) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .set_style_id(value)
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }
}
