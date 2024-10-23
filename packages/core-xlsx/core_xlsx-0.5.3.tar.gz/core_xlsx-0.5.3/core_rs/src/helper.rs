use anyhow::{bail, Result};
use rayon::iter::{IntoParallelRefIterator, ParallelIterator};
use regex::Regex;
use serde::{Deserialize, Serialize};

use crate::types::{XLSXSheet, XLSXSheetCell};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelperSheet {
    pub sheets: Vec<XLSXSheet>,
}

impl HelperSheet {
    pub fn new(sheets: Vec<XLSXSheet>) -> Self {
        Self { sheets }
    }

    /// Поиск листа по наименованию
    pub fn find_sheet_by_name(&self, name: &str) -> Result<Option<XLSXSheet>> {
        let sheet = self
            .sheets
            .par_iter()
            .find_first(|s| s.name == *name)
            .cloned();

        Ok(sheet)
    }

    /// Поиск листа по шаблону regex
    pub fn find_sheet_by_pattern(&self, pattern: &str) -> Result<Option<XLSXSheet>> {
        let re = Regex::new(pattern).unwrap();

        let cell = self
            .sheets
            .par_iter()
            .find_first(|s| re.is_match(&s.name))
            .cloned();

        Ok(cell)
    }

    /// Поиск листа по индексу
    pub fn find_sheet_by_index(&self, idx: i32) -> Result<Option<XLSXSheet>> {
        let cell = self
            .sheets
            .par_iter()
            .find_first(|s| s.index == idx)
            .cloned();

        Ok(cell)
    }

    /// Получение списка листов, исключая передаваесый список.
    pub fn get_sheets_without_names(&self, name_list: Vec<String>) -> Result<Vec<XLSXSheet>> {
        let cells = self
            .sheets
            .par_iter()
            .filter(|c| !name_list.contains(&c.name))
            .cloned()
            .collect();

        Ok(cells)
    }

    /// Получение списка листов, передаваемого списка листов .
    pub fn get_sheets_with_names(&self, name_list: Vec<String>) -> Result<Vec<XLSXSheet>> {
        let cells = self
            .sheets
            .par_iter()
            .filter(|c| name_list.contains(&c.name))
            .cloned()
            .collect();

        Ok(cells)
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelperSheetCell;

impl HelperSheetCell {
    /// Поиск ячейки по шаблону
    pub fn find_cell_pattern_regex(
        pattern: &str,
        cells: &Vec<XLSXSheetCell>,
    ) -> Result<Option<XLSXSheetCell>> {
        let re = Regex::new(pattern).unwrap();

        let cell = cells
            .par_iter()
            .find_first(|c| re.is_match(&c.value.get_value_str()))
            .cloned();

        Ok(cell)
    }

    // Поиск ячеек по шаблону
    pub fn find_cells_pattern_regex(
        pattern: &str,
        cells: &Vec<XLSXSheetCell>,
    ) -> Result<Vec<XLSXSheetCell>> {
        let re = Regex::new(pattern).unwrap();

        let cells = cells
            .par_iter()
            .filter(|c| re.is_match(&c.value.get_value_str()))
            .cloned()
            .collect();

        Ok(cells)
    }

    /// Поиск ячеек колонок для строк которые соответствуют патерну
    pub fn find_cells_for_rows_pattern_regex(
        pattern: &str,
        cells: &Vec<XLSXSheetCell>,
        col_stop: Option<u32>,
    ) -> Result<Vec<XLSXSheetCell>> {
        let re = Regex::new(pattern).unwrap();

        // Находим все строки, в которых есть ячейки, соответствующие шаблону
        let matching_rows: Vec<u32> = cells
            .par_iter()
            .filter(|c| re.is_match(&c.value.get_value_str()))
            .map(|c| c.row)
            .collect();

        // Возвращаем все ячейки, которые находятся в найденных строках
        let cells = cells
            .par_iter()
            .filter(|c| matching_rows.contains(&c.row) && col_stop.map_or(true, |s| c.column <= s))
            .cloned()
            .collect();

        Ok(cells)
    }

    /// Поиск ячеек строк для колонок которые соответствуют патерну
    pub fn find_cells_for_cols_pattern_regex(
        pattern: &str,
        cells: &Vec<XLSXSheetCell>,
        row_stop: Option<u32>,
    ) -> Result<Vec<XLSXSheetCell>> {
        let re = Regex::new(pattern).unwrap();

        // Находим все колонки, в которых есть ячейки, соответствующие шаблону
        let matching_cols: Vec<u32> = cells
            .par_iter()
            .filter(|c| re.is_match(&c.value.get_value_str()))
            .map(|c| c.column)
            .collect();

        // Возвращаем все ячейки, которые находятся в найденных колонках
        let cells = cells
            .par_iter()
            .filter(|c| matching_cols.contains(&c.column) && row_stop.map_or(true, |s| c.row <= s))
            .cloned()
            .collect();

        Ok(cells)
    }

    /// Поиск ячеек с помощью ИЛИ ячейки по патернам
    pub fn find_cells_multi_pattern_regex(
        pattern_1: &str,
        pattern_2: &str,
        cells: &Vec<XLSXSheetCell>,
    ) -> Result<Vec<XLSXSheetCell>> {
        let re1 = Regex::new(pattern_1).unwrap();
        let re2 = Regex::new(pattern_2).unwrap();

        let cells = cells
            .par_iter()
            .filter(|c| {
                let value_str = c.value.get_value_str();
                re1.is_match(&value_str) || re2.is_match(&value_str)
            })
            .cloned()
            .collect();

        Ok(cells)
    }

    /// Поиск ячейки по буквенной координате A1 (cell)
    pub fn find_cell_by_cell(
        cell: &str,
        cells: &Vec<XLSXSheetCell>,
    ) -> Result<Option<XLSXSheetCell>> {
        let cells = cells.par_iter().find_first(|c| c.cell == *cell).cloned();

        Ok(cells)
    }

    /// Поиск ячейки по координате
    pub fn find_cell_by_coordinate(
        row: u32,
        col: u32,
        cells: &Vec<XLSXSheetCell>,
    ) -> Result<Option<XLSXSheetCell>> {
        let cell = cells
            .par_iter()
            .find_first(|c| c.row == row && c.column == col)
            .cloned();

        Ok(cell)
    }

    /// Поиск ячеек между шаьлонами
    pub fn find_cells_between_patterns(
        pattern_after: &str,
        pattern_before: &str,
        cells: &Vec<XLSXSheetCell>,
    ) -> Result<Vec<XLSXSheetCell>> {
        let re1 = Regex::new(pattern_after).unwrap();
        let re2 = Regex::new(pattern_before).unwrap();

        let mut new_cells = Vec::new();
        let mut in_range = false;

        for cell in cells {
            let value_str = cell.value.get_value_str();

            if re1.is_match(&value_str) {
                in_range = true;
            } else if re2.is_match(&value_str) {
                in_range = false;
            }

            if in_range {
                new_cells.push(cell.clone());
            }
        }

        Ok(new_cells)
    }

    /// Получить список всех ячеек в заданном диапазоне.
    pub fn iter_cells(
        min_row: u32,
        max_row: u32,
        min_col: u32,
        max_col: u32,
        cells: &Vec<XLSXSheetCell>,
    ) -> Result<Vec<XLSXSheetCell>> {
        if min_row > max_row || min_col > max_col {
            bail!("The coordinates of the cells were incorrectly transmitted");
        }

        let filtered_cells = cells
            .par_iter()
            .filter(|c| {
                c.row >= min_row && c.row <= max_row && c.column >= min_col && c.column <= max_col
            })
            .cloned()
            .collect();

        Ok(filtered_cells)
    }

    /// Возвращаем все ячейки, которые находятся в диапазоне строк
    pub fn find_cells_by_range_rows(
        start_row: u32,
        end_row: u32,
        cells: &Vec<XLSXSheetCell>,
    ) -> Result<Vec<XLSXSheetCell>> {
        let cells = cells
            .par_iter()
            .filter(|c| c.row >= start_row && c.row <= end_row)
            .cloned()
            .collect();

        Ok(cells)
    }

    /// Возвращаем все ячейки, которые находятся в диапазоне колонок
    pub fn find_cells_by_range_cols(
        start_col: u32,
        end_col: u32,
        cells: &Vec<XLSXSheetCell>,
    ) -> Result<Vec<XLSXSheetCell>> {
        let cells = cells
            .par_iter()
            .filter(|c| c.column >= start_col && c.column <= end_col)
            .cloned()
            .collect();

        Ok(cells)
    }
}
