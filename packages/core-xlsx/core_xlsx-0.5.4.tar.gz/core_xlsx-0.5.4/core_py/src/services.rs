use pyo3::{exceptions::PyNotImplementedError, prelude::*, types::PyList};

use crate::types::WrapperXLSXSheet;

#[pyclass]
#[pyo3(module = "core_xlsx", frozen, subclass)]
#[derive(Debug, Clone)]
pub struct Service {
    uow: PyObject,
}

#[pymethods]
impl Service {
    #[new]
    fn new(uow: PyObject) -> PyResult<Self> {
        Python::with_gil(|_py| Ok(Self { uow }))
    }

    pub fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        Python::with_gil(|_py| {
            let class_name = slf.get_type().qualname()?;
            Ok(format!("{}", class_name))
        })
    }

    #[getter]
    pub fn uow(&self) -> PyResult<PyObject> {
        Python::with_gil(|_py| Ok(self.uow.clone()))
    }

    #[pyo3(text_signature = "($self, sheets, / **kwargs=None)")]
    pub fn summary_0(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<&Bound<'_, PyList>> {
        Python::with_gil(|_py| {
            Err(PyNotImplementedError::new_err(
                "Method 'summary_0' is not implemented",
            ))
        })
    }

    #[pyo3(text_signature = "($self, sheets, /, **kwargs=None)")]
    pub fn summary_1(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    #[pyo3(text_signature = "($self, sheets, /, **kwargs=None)")]
    pub fn summary_2(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Ok(vec![])
    }
    #[pyo3(text_signature = "($self, sheets, /, **kwargs=None)")]
    pub fn summary_3(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }
    #[pyo3(text_signature = "($self, sheets, /, **kwargs=None)")]
    pub fn summary_4(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    #[pyo3(text_signature = "($self, sheets, /, **kwargs=None)")]
    pub fn summary_5(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    #[pyo3(text_signature = "($self, sheets, /, **kwargs=None)")]
    pub fn summary_6(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    #[pyo3(text_signature = "($self, sheets, /, **kwargs=None)")]
    pub fn summary_7(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    #[pyo3(text_signature = "($self, sheets, /, **kwargs=None)")]
    pub fn summary_8(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    #[pyo3(text_signature = "($self, sheets, /, **kwargs=None)")]
    pub fn fmt_0(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| {
            Err(PyNotImplementedError::new_err(
                "Method 'fmt_0' is not implemented",
            ))
        })
    }

    pub fn fmt_1(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    pub fn fmt_2(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    pub fn fmt_3(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    pub fn fmt_4(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    pub fn fmt_5(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    pub fn fmt_6(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    pub fn fmt_7(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }

    pub fn fmt_8(
        &self,
        _sheets: &Bound<'_, PyList>,
        _kwargs: &Bound<'_, PyAny>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| Ok(vec![]))
    }
}
