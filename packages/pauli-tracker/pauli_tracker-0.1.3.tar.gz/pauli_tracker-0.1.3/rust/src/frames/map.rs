use std::{collections::HashMap, hash::BuildHasherDefault, mem};

use lib::{
    collection::{self, Init},
    pauli,
    tracker::{frames, Tracker},
};
use pyo3::{PyResult, Python};
use rustc_hash::FxHasher;

use crate::{impl_helper::links, pauli::PauliStack, BitVec, Module};

type Map<T> = collection::Map<T, BuildHasherDefault<FxHasher>>;

type Storage = Map<pauli::PauliStack<BitVec>>;
impl_frames!(
    Storage,
    concat!(
        "`Frames <",
        links::frames!(),
        ">`_\\<`Map <",
        links::map!(),
        ">`_\\<`PauliStack <",
        links::pauli_stack!(),
        ">`_\\<`BitVec <",
        links::bit_vec!(),
        ">`_\\>\\>\\>."
    )
);

#[pyo3::pymethods]
impl Frames {
    #[doc = crate::transform!()]
    ///
    /// Returns:
    ///     dict[int, PauliStack]:
    #[allow(clippy::wrong_self_convention)]
    fn into_py_dict(&self) -> HashMap<usize, PauliStack> {
        into_py_dict(self.0.clone())
    }

    #[doc = crate::take_transform!()]
    ///
    /// Returns:
    ///     dict[int, PauliStack]:
    fn take_into_py_dict(&mut self) -> HashMap<usize, PauliStack> {
        into_py_dict(mem::take(&mut self.0))
    }

    #[doc = crate::transform!()]
    ///
    /// Returns: cf. :obj:`~pauli_tracker.pauli.PauliStack`
    ///     dict[int, tuple[list[int], list[int]]]:
    #[allow(clippy::wrong_self_convention)]
    fn into_py_dict_recursive(&self) -> HashMap<usize, (Vec<u64>, Vec<u64>)> {
        into_py_dict_recursive(self.0.clone())
    }

    #[doc = crate::take_transform!()]
    ///
    /// Returns: cf. :obj:`~pauli_tracker.pauli.PauliStack`
    ///     dict[int, tuple[list[int], list[int]]]:
    fn take_into_py_dict_recursive(&mut self) -> HashMap<usize, (Vec<u64>, Vec<u64>)> {
        into_py_dict_recursive(mem::take(&mut self.0))
    }
}

fn into_py_dict(frames: frames::Frames<Storage>) -> HashMap<usize, PauliStack> {
    frames
        .into_storage()
        .into_iter()
        .map(|(b, p)| (b, PauliStack(p)))
        .collect()
}

fn into_py_dict_recursive(
    frames: frames::Frames<Storage>,
) -> HashMap<usize, (Vec<u64>, Vec<u64>)> {
    frames
        .into_storage()
        .into_iter()
        .map(|(b, p)| (b, (p.z.into_vec(), p.x.into_vec())))
        .collect()
}

pub fn add_module(py: Python<'_>, parent_module: &Module) -> PyResult<()> {
    let module = Module::new(py, "map", parent_module.path.clone())?;
    module.pymodule.add_class::<Frames>()?;
    parent_module.add_submodule(py, module)?;
    Ok(())
}
