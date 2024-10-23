pub mod datatype;
pub mod helper;
pub mod types;
pub mod utils;

/// Функция для получения версии.
pub fn version() -> &'static str {
    env!("CARGO_PKG_VERSION")
}
