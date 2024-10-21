#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
// Ref: https://github.com/colmap/colmap/blob/0ea2d5ceee1360bba427b2ef61f1351e59a46f91/src/colmap/util/types.h
use std::fmt;

use pyo3::prelude::*;


#[pyclass]
#[derive(Clone)]
pub struct Color {
    pub r: u8,
    pub g: u8,
    pub b: u8,
}

#[pymethods]
impl Color {
    #[getter]
    fn r(&self) -> u8 {
        self.r
    }

    #[getter]
    fn g(&self) -> u8 {
        self.g
    }

    #[getter]
    fn b(&self) -> u8 {
        self.b
    }
    fn __str__(&self) -> PyResult<String>   {
        Ok(format!("Color r: {}, b: {:?}, g: {:?}", self.r, self.b, self.g))
    }
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("Color r: {}, b: {:?}, g: {:?}", self.r, self.b, self.g))
    }
}

impl fmt::Display for Color {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "r: {}, b: {:?}, g: {:?}", self.r, self.b, self.g)
    }
}

pub type camera_t = u32;
// Unique identifier for images.
pub type image_t = u32;
// Each image pair gets a unique ID, see `Database::ImagePairToPairId`.
pub type image_pair_t = u64;

// Index per image, i.e. determines maximum number of 2D points per image.
pub type point2D_t = u32;


// Unique identifier per added 3D point. Since we add many 3D points,
// delete them, and possibly re-add them again, the maximum number of allowed
// unique indices should be large.
pub type point3D_t = u64;


// Let's hope these are the same as here:
// https://github.com/colmap/colmap/blob/0ea2d5ceee1360bba427b2ef61f1351e59a46f91/src/colmap/util/types.h#L101
pub const kInvalidPoint2DIdx: point2D_t = point2D_t::MAX;
pub const kInvalidPoint3DIdx: point3D_t = point3D_t::MAX;
