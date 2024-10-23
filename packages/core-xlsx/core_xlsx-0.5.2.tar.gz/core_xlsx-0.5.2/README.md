## Вспомогательная библиотека __core_xlsx__.

`core_xlsx` - это Python-библиотека для работы с данными в виде Excel (XLSX) для проекта, предоставляющая удобные инструменты для манипуляции данными в таблицах.

## Установка

```
poetry add core-xlsx
```

## Основные компоненты

- `XLSXSheet`: Представляет лист Excel.
- `XLSXSheetCell`: Представляет ячейку в листе Excel.
- `Service`: Базовый класс для создания сервисов обработки данных и создания отчетов.
- `HelperSheet`: Помощник для работы с несколькими листами и ячейками.
- `HelperSheetCell`: Помощник для работы с ячейками.
- `column_number_to_letter`: Функция для преобразования колонки с row в букву (1 -> A).
- `xlsxheets_to_json`: Функция для преобразования списка данных `Sequence[XLSXSheet]` в json
- `xlsxheets_to_dict`: Функция для преобразования списка данных `Sequence[XLSXSheet]` в dict

## Возможности

- Поиск листов по имени или шаблону
- Поиск ячеек по значению, регулярному выражению или адресу
- Манипуляция данными ячеек (установка значений, формул, форматов)
- Получение информации о ячейках (тип данных, числовой формат, стиль)
- Работа с датами и временем
- Создание пользовательских сервисов и форматтеров для создания отчетов xlsx.

## Пример использования

```python
from core_xlsx import XLSXSheet, Service, HelperSheet

class MyService(Service):
    def summary_0(self, sheets, /, **kwargs):
        """Данный метод предназначен для формирования отчета"""

        h = HelperSheet(sheets)
        sheet = h.find_sheet_by_pattern("Отчет")

        if sheet:
            cell = sheet.find_cell_pattern_regex("Итого:")
            if cell:
                total = float(cell.value)
                print(f"Итоговая сумма: {total}")

        # Вызовем метод форматирования
        sheets = self.fmt_0(sheets, year=2024)

        return sheets


    def fmt_0(self, sheets, /, **kwargs):
        """Данный метод предназначен для форматирования отчета"""
        return sheets

# Использование
service = MyService(uow="my_unit_of_work")
sheets = [...]  # Ваши данные листов

processed_sheets = service.summary_0(sheets)
```
