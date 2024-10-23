use std::collections::HashSet;

use anyhow::{bail, Result};
use chrono::NaiveDateTime;
use serde::{Deserialize, Serialize};

use crate::{
    datatype::{CellRawValue, CellValue},
    helper::HelperSheetCell,
    utils::{column_number_to_letter, get_number_format_by_datatype},
};

// Список типов
const DATA_TYPES: [&str; 4] = ["s", "n", "d", "b"];
#[derive(Clone, Debug, Serialize, Deserialize, Default)]
pub struct XLSXSheet {
    pub name: String,
    pub max_row: u32,
    pub max_column: u32,
    pub index: i32,
    pub main: bool,
    pub cells: Vec<XLSXSheetCell>,
    pub _indexes: HashSet<(u32, u32)>,
}

impl XLSXSheet {
    pub fn new(name: String, index: i32, cols: u32, rows: u32) -> Self {
        let mut cells = Vec::with_capacity((rows * cols) as usize);
        let mut indexes = HashSet::new();
        for r in 1..=rows {
            for c in 1..=cols {
                let cell = XLSXSheetCell::new(r, c, None);
                cells.push(cell);

                // Insert Indexes
                indexes.insert((r, c));
            }
        }

        Self {
            name,
            index,
            cells,
            max_row: rows,
            max_column: cols,
            _indexes: indexes,
            ..Default::default()
        }
    }

    /// Добавление значения в ячейку по координате.
    /// Дополнительно создаются несуществующие ячейки.
    pub fn write_cell(&mut self, row: u32, col: u32, value: String) -> Result<()> {
        if self._indexes.contains(&(row, col)) {
            // Ячейка существует, редактируем ее
            let cell_index = self
                .cells
                .iter()
                .position(|c| c.row == row && c.column == col)
                .unwrap();

            // Редактирование
            self.cells[cell_index].set_value(value)?;
        } else {
            // Ячейка не существует, добавляем новую
            let new_cell = XLSXSheetCell::new(row, col, Some(value));
            self.cells.push(new_cell);
            self._indexes.insert((row, col));

            let mr = row as i32 - self.max_row as i32;
            let mc = col as i32 - self.max_column as i32;

            if mr > 1 || mc > 1 {
                // Генерация несуществующих ячеек.
                let mut new_cells = Vec::with_capacity((row * col) as usize);
                for r in (self.max_row + 1)..row {
                    for c in (self.max_column + 1)..col {
                        new_cells.push(XLSXSheetCell::new(r, c, None));
                        self._indexes.insert((r, c));
                    }
                }
                self.cells.extend(new_cells);

                // Сортируем, чтобы все было упорядочено.
                self.cells
                    .sort_by(|a, b| a.row.cmp(&b.row).then_with(|| a.column.cmp(&b.column)));
            }

            // Обновим максимальные значения
            self.max_row = self.max_row.max(row);
            self.max_column = self.max_column.max(col);
        }
        Ok(())
    }

    /// Добавление значения в ячейку по координате с форумлой.
    /// Дополнительно создаются несуществующие ячейки.
    pub fn write_cell_with_formula(
        &mut self,
        row: u32,
        col: u32,
        value: String,
        formula: String,
    ) -> Result<()> {
        if self._indexes.contains(&(row, col)) {
            // Ячейка существует, редактируем ее
            let cell_index = self
                .cells
                .iter()
                .position(|c| c.row == row && c.column == col)
                .unwrap();

            // Редактирование
            let cell = &mut self.cells[cell_index];
            cell.set_value(value)?;
            cell.set_formula(formula)?;
        } else {
            // Ячейка не существует, добавляем новую
            let mut new_cell = XLSXSheetCell::new(row, col, Some(value));
            new_cell.set_formula(formula)?;

            self.cells.push(new_cell);
            self._indexes.insert((row, col));

            let mr = row as i32 - self.max_row as i32;
            let mc = col as i32 - self.max_column as i32;

            if mr > 1 || mc > 1 {
                // Генерация несуществующих ячеек.
                let mut new_cells = Vec::with_capacity((row * col) as usize);
                for r in (self.max_row + 1)..row {
                    for c in (self.max_column + 1)..col {
                        new_cells.push(XLSXSheetCell::new(r, c, None));
                        self._indexes.insert((r, c));
                    }
                }
                self.cells.extend(new_cells);

                // Сортируем, чтобы все было упорядочено.
                self.cells
                    .sort_by(|a, b| a.row.cmp(&b.row).then_with(|| a.column.cmp(&b.column)));
            }

            // Обновим максимальные значения
            self.max_row = self.max_row.max(row);
            self.max_column = self.max_column.max(col);
        }
        Ok(())
    }

    /// Добавление стиля в существующую ячейку по координате.
    pub fn write_style_for_cell(&mut self, row: u32, col: u32, style_id: String) -> Result<()> {
        let index = self
            .cells
            .binary_search_by_key(&(row, col), |c| (c.row, c.column));

        if let Ok(index) = index {
            self.cells[index].set_style_id(style_id)?;
        }
        Ok(())
    }

    /// Добавление стиля в существующую ячейку по координате.
    pub fn write_formula_for_cell(&mut self, row: u32, col: u32, formula: String) -> Result<()> {
        let index = self
            .cells
            .binary_search_by_key(&(row, col), |c| (c.row, c.column));

        if let Ok(index) = index {
            self.cells[index].set_formula(formula)?;
        }
        Ok(())
    }

    /// Метод для удаления колонок
    pub fn delete_cols(&mut self, idx: u32, amount: u32) -> Result<()> {
        // Remove cells in the specified columns
        self.cells
            .retain(|cell| cell.column < idx || cell.column >= idx + amount);

        // Update column numbers for remaining cells
        for cell in &mut self.cells {
            if cell.column > idx {
                cell.column -= amount;
                // Update the cell's letter coordinate
                let new_letter = column_number_to_letter(cell.column);
                cell.cell = format!("{}{}", new_letter, cell.row);
            }
        }

        // Update max_column if necessary
        self.max_column = self.max_column.saturating_sub(amount);

        // Sort cells to maintain order
        self.cells
            .sort_by(|a, b| a.row.cmp(&b.row).then_with(|| a.column.cmp(&b.column)));

        Ok(())
    }

    /// Метод для удаления  строк
    pub fn delete_rows(&mut self, idx: u32, amount: u32) -> Result<()> {
        // Remove cells in the specified rows
        self.cells
            .retain(|cell| cell.row < idx || cell.row >= idx + amount);

        // Update row numbers for remaining cells
        for cell in &mut self.cells {
            if cell.row > idx {
                cell.row -= amount;
                // Update the cell's coordinate
                let letter = column_number_to_letter(cell.column);
                cell.cell = format!("{}{}", letter, cell.row);
            }
        }

        // Update max_row if necessary
        self.max_row = self.max_row.saturating_sub(amount);

        // Sort cells to maintain order
        self.cells
            .sort_by(|a, b| a.row.cmp(&b.row).then_with(|| a.column.cmp(&b.column)));

        Ok(())
    }

    /// Метод для добавления данных по объединению ячеек.
    pub fn set_merged_cells(
        &mut self,
        start_row: u32,
        end_row: u32,
        start_column: u32,
        end_column: u32,
    ) -> Result<()> {
        // Iterate through all cells in the merge range
        for row in start_row..=end_row {
            for col in start_column..=end_column {
                if let Some(cell) = self
                    .cells
                    .iter_mut()
                    .find(|c| c.row == row && c.column == col)
                {
                    cell.is_merge = true;
                    cell.start_row = Some(start_row);
                    cell.end_row = Some(end_row);
                    cell.start_column = Some(start_column);
                    cell.end_column = Some(end_column);
                }
            }
        }

        Ok(())
    }

    /// Получить список всех ячеек в заданном диапазоне.
    pub fn iter_cells(
        &self,
        min_row: Option<u32>,
        max_row: Option<u32>,
        min_col: Option<u32>,
        max_col: Option<u32>,
    ) -> Result<Vec<XLSXSheetCell>> {
        // Получение значений, так как они необязательные.
        let min_row = min_row.unwrap_or(1);
        let max_row = max_row.unwrap_or(self.max_row);
        let min_col = min_col.unwrap_or(1);
        let max_col = max_col.unwrap_or(self.max_column);

        HelperSheetCell::iter_cells(min_row, max_row, min_col, max_col, &self.cells)
    }

    /// Поиск ячейки по шаблону
    pub fn find_cell_pattern_regex(&self, pattern: &str) -> Result<Option<XLSXSheetCell>> {
        HelperSheetCell::find_cell_pattern_regex(pattern, &self.cells)
    }

    // Поиск ячеек по шаблону
    pub fn find_cells_pattern_regex(&self, pattern: &str) -> Result<Vec<XLSXSheetCell>> {
        HelperSheetCell::find_cells_pattern_regex(pattern, &self.cells)
    }

    /// Поиск ячеек колонок для строк которые соответствуют патерну
    pub fn find_cells_for_rows_pattern_regex(
        &self,
        pattern: &str,
        col_stop: Option<u32>,
    ) -> Result<Vec<XLSXSheetCell>> {
        HelperSheetCell::find_cells_for_rows_pattern_regex(pattern, &self.cells, col_stop)
    }

    /// Поиск ячеек строк для колонок которые соответствуют патерну
    pub fn find_cells_for_cols_pattern_regex(
        &self,
        pattern: &str,
        row_stop: Option<u32>,
    ) -> Result<Vec<XLSXSheetCell>> {
        HelperSheetCell::find_cells_for_cols_pattern_regex(pattern, &self.cells, row_stop)
    }

    /// Поиск ячеек с помощью ИЛИ ячейки по патернам
    pub fn find_cells_multi_pattern_regex(
        &self,
        pattern_1: &str,
        pattern_2: &str,
    ) -> Result<Vec<XLSXSheetCell>> {
        HelperSheetCell::find_cells_multi_pattern_regex(pattern_1, pattern_2, &self.cells)
    }

    /// Поиск ячейки по буквенной координате A1 (cell)
    pub fn find_cell_by_cell(&self, cell: &str) -> Result<Option<XLSXSheetCell>> {
        HelperSheetCell::find_cell_by_cell(cell, &self.cells)
    }

    /// Поиск ячейки по координате
    pub fn find_cell_by_coordinate(&self, row: u32, col: u32) -> Result<Option<XLSXSheetCell>> {
        HelperSheetCell::find_cell_by_coordinate(row, col, &self.cells)
    }

    /// Поиск ячеек между шаьлонами
    pub fn find_cells_between_patterns(
        &self,
        pattern_after: &str,
        pattern_before: &str,
    ) -> Result<Vec<XLSXSheetCell>> {
        HelperSheetCell::find_cells_between_patterns(pattern_after, pattern_before, &self.cells)
    }

    /// Возвращаем все ячейки, которые находятся в диапазоне строк
    pub fn find_cells_by_range_rows(
        &self,
        start_row: u32,
        end_row: u32,
    ) -> Result<Vec<XLSXSheetCell>> {
        HelperSheetCell::find_cells_by_range_rows(start_row, end_row, &self.cells)
    }

    /// Возвращаем все ячейки, которые находятся в диапазоне колонок
    pub fn find_cells_by_range_cols(
        &self,
        start_col: u32,
        end_col: u32,
    ) -> Result<Vec<XLSXSheetCell>> {
        HelperSheetCell::find_cells_by_range_cols(start_col, end_col, &self.cells)
    }
}

#[derive(Clone, Debug, Serialize, Deserialize, Default)]
pub struct XLSXSheetCell {
    pub row: u32,
    pub column: u32,
    pub cell: String,
    pub value: CellValue,
    pub formula: Option<String>,
    pub data_type: String,
    pub number_format: String,
    pub cell_type: Option<String>,
    pub el_type: Option<String>,
    pub is_merge: bool,
    pub start_row: Option<u32>,
    pub end_row: Option<u32>,
    pub start_column: Option<u32>,
    pub end_column: Option<u32>,
    pub style_id: Option<String>,
    // Даннык поля только в движке пока что.
    pub hidden_value: Option<String>,
    pub comment: Option<String>,
}

impl XLSXSheetCell {
    pub fn new(row: u32, col: u32, value: Option<String>) -> Self {
        // Получение  letter (cell)
        let cell = column_number_to_letter(col);
        let cell = format!("{}{}", cell, row);

        // Обработка значения
        let mut raw_value = CellRawValue::Empty;
        if let Some(val) = value {
            raw_value = CellValue::quess_typed_value(&val)
        }

        let value = CellValue {
            raw_value: raw_value.clone(),
        };
        // Определение datetype
        let data_type = raw_value.get_date_type().to_string();
        // Определение number format
        let number_format = get_number_format_by_datatype(&data_type);

        Self {
            row,
            column: col,
            cell,
            value,
            data_type,
            number_format,
            ..Default::default()
        }
    }

    /// Метод для получения значения ячейки.
    pub fn set_value(&mut self, value: String) -> Result<()> {
        let cell_value = self.value.set_value(value);

        if self.formula.is_none() {
            let data_type = cell_value.get_data_type();

            // Обновим данные, так как это формула
            self.number_format = get_number_format_by_datatype(data_type);
            self.data_type = data_type.to_string();
        }

        Ok(())
    }

    /// Метод для получения значения ячейки Numbers.
    pub fn set_value_number(&mut self, value: f64) -> Result<()> {
        self.value.set_value_number(value);

        Ok(())
    }

    /// Метод для получения значения ячейки Bool.
    pub fn set_value_bool(&mut self, value: bool) -> Result<()> {
        self.value.set_value_bool(value);

        Ok(())
    }

    /// Метод для получения значения ячейки String.
    pub fn set_value_str(&mut self, value: String) -> Result<()> {
        self.value.set_value_str(value);

        Ok(())
    }

    /// Метод для получения значения ячейки Datetime.
    pub fn set_value_datetime(&mut self, value: NaiveDateTime) -> Result<()> {
        self.value.set_value_datatime(value);

        Ok(())
    }

    /// Метод для получения значения ячейки String.
    pub fn set_formula(&mut self, value: String) -> Result<()> {
        self.formula = Some(value);
        // если идет установка формулы, то и тип установим как формула
        self.data_type = "f".to_string();

        Ok(())
    }

    /// Метод для получения значения ячейки data_type.
    pub fn set_data_type(&mut self, value: String) -> Result<()> {
        if !DATA_TYPES.contains(&value.as_str()) {
            bail!(format!("value not in {:?}", DATA_TYPES))
        }

        self.data_type = value;

        Ok(())
    }

    /// Метод для получения значения ячейки number_format.
    pub fn set_number_format(&mut self, value: String) -> Result<()> {
        self.number_format = value;

        Ok(())
    }

    /// Метод для получения значения ячейки cell_type.
    pub fn set_cell_type(&mut self, value: String) -> Result<()> {
        self.cell_type = Some(value);

        Ok(())
    }

    /// Метод для получения значения ячейки el_type.
    pub fn set_el_type(&mut self, value: String) -> Result<()> {
        self.el_type = Some(value);

        Ok(())
    }

    /// Метод для получения флага, ячейка с формулой или нет.
    pub fn is_formula(&self) -> Result<bool> {
        Ok(self.formula.is_some() && self.data_type == *"f")
    }

    /// Проверить, является ли значение ячейки boolean
    pub fn is_value_bool(&self) -> Result<bool> {
        Ok(self.value.is_bool())
    }

    /// Проверить, является ли значение ячейки numeric
    pub fn is_value_numeric(&self) -> Result<bool> {
        Ok(self.value.is_numeric())
    }

    /// Проверить, является ли значение ячейки datetime
    pub fn is_value_datetime(&self) -> Result<bool> {
        Ok(self.value.is_datetime())
    }

    /// Проверить, является ли значение ячейки empty
    pub fn is_value_empty(&self) -> Result<bool> {
        Ok(self.value.is_empty())
    }

    /// Метод для добавления стиля к ячейки
    pub fn set_style_id(&mut self, value: String) -> Result<()> {
        self.style_id = Some(value);

        Ok(())
    }
}
