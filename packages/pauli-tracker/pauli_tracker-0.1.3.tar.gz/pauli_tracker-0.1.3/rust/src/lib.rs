use bitvec::order::Lsb0;
use pyo3::{types::PyModule, PyResult, Python};

pub struct Module<'m> {
    pub pymodule: &'m PyModule,
    pub path: String,
}

impl<'m> Module<'m> {
    pub fn new(py: Python<'m>, name: &str, mut path: String) -> PyResult<Self> {
        path.push_str(format!(".{}", name).as_str());
        Ok(Self {
            pymodule: PyModule::new(py, name)?,
            path,
        })
    }

    pub fn add_submodule(&self, py: Python<'_>, submodule: Self) -> PyResult<()> {
        self.pymodule.add_submodule(submodule.pymodule)?;
        py.import("sys")?
            .getattr("modules")?
            .set_item(submodule.path, submodule.pymodule)?;
        Ok(())
    }
}

pub mod impl_helper;

pub mod frames;
mod live;
mod pauli;

// ensuring that we always use 64 bits per chunk (promised by the API docs and used
// internally, e.g., in the bitvector_to_boolvector function in __init__.py)
type BitVec = bitvec::vec::BitVec<u64, Lsb0>;

pub fn create_module(py: Python, module: &PyModule) -> PyResult<()> {
    let module = Module {
        pymodule: module,
        path: "pauli_tracker._lib".to_string(),
    };
    live::add_module(py, &module)?;
    frames::add_module(py, &module)?;
    pauli::add_module(py, &module)?;
    Ok(())
}
