#![allow(non_camel_case_types)]
// See https://github.com/colmap/colmap/blob/main/src/colmap/sensor/models.h for reference
// I've simplified some stuff //Johan

use std::fmt;
use pyo3::prelude::*;
use pyo3::pyclass;

#[derive(Debug, Clone)]
pub enum CameraModelId {
    kInvalid = -1,
    kSimplePinhole = 0,
    kPinhole = 1,
    kSimpleRadial = 2,
    kRadial = 3,
    kOpenCV = 4,
    kOpenCVFisheye = 5,
    kFullOpenCV = 6,
    kFOV = 7,
    kSimpleRadialFisheye = 8,
    kRadialFisheye = 9,
    kThinPrismFisheye = 10,
}

impl From<i32> for CameraModelId {
    fn from(value: i32) -> Self {
        match value {
            -1 => CameraModelId::kInvalid, 
            0 => CameraModelId::kSimplePinhole,
            1 => CameraModelId::kPinhole,
            2 => CameraModelId::kSimpleRadial,
            3 => CameraModelId::kRadial,
            4 => CameraModelId::kOpenCV,
            5 => CameraModelId::kOpenCVFisheye,
            6 => CameraModelId::kFullOpenCV,
            7 => CameraModelId::kFOV,
            8 => CameraModelId::kSimpleRadialFisheye,
            9 => CameraModelId::kRadialFisheye,
            10 => CameraModelId::kThinPrismFisheye,
            _ => panic!("Invalid enum value"),
        }
    }
}

impl fmt::Display for CameraModelId {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let x = match self {
            CameraModelId::kInvalid => "Invalid".to_string(),
            CameraModelId::kSimplePinhole => "Simple Pinhole".to_string(),
            CameraModelId::kPinhole => "Pinhole".to_string(),
            CameraModelId::kSimpleRadial => "Simple Radial".to_string(),
            CameraModelId::kRadial => "Radial".to_string(),
            CameraModelId::kOpenCV => "OpenCV".to_string(),
            CameraModelId::kOpenCVFisheye => "OpenCV Fisheye".to_string(),
            CameraModelId::kFullOpenCV => "Full OpenCV".to_string(),
            CameraModelId::kFOV => "FOV".to_string(),
            CameraModelId::kSimpleRadialFisheye => "Simple Radial Fisheye".to_string(),
            CameraModelId::kRadialFisheye => "Radial Fisheye".to_string(),
            CameraModelId::kThinPrismFisheye => "Thin Prism Fisheye".to_string(),
        };
        write!(f, "{}", x)
    }

}


pub fn get_num_params(model_id: & CameraModelId) -> u64{
    let x: u64 = match model_id {
        CameraModelId::kSimplePinhole => 3,
        CameraModelId::kPinhole => 4,
        CameraModelId::kSimpleRadial => 4,
        CameraModelId::kRadial => 5,
        CameraModelId::kOpenCV => 8,
        CameraModelId::kOpenCVFisheye => 8 ,
        CameraModelId::kFullOpenCV => 12,
        CameraModelId::kFOV => 5,
        CameraModelId::kSimpleRadialFisheye => 4,
        CameraModelId::kRadialFisheye => 5,
        CameraModelId::kThinPrismFisheye => 12,
        CameraModelId::kInvalid => panic!("Cannot get params for invalid camera")
    };
    return x;   
}

#[pyclass]
pub struct Camera {
    #[pyo3(get)]
    pub camera_id:u32,
    pub model_id:CameraModelId,
    #[pyo3(get)]
    pub width: u64,
    #[pyo3(get)]
    pub height: u64,
    #[pyo3(get)]
    pub params: Vec<f64>,
}

#[pymethods]
impl Camera {
    #[getter]
    fn get_model_id(&self) -> PyResult<String> {
        return Ok(self.model_id.to_string());
    }
    fn K(&self) -> PyResult<[[f64; 3]; 3]> {
        match self.model_id {
            CameraModelId::kSimplePinhole => {
                let mut K = [[0.0; 3]; 3];
                K[0][0] = self.params[0];
                K[1][1] = self.params[0];
                K[0][2] = self.params[1];
                K[1][2] = self.params[2];
                K[2][2] = 1.0;
                return Ok(K);
            },
            CameraModelId::kPinhole => {
                let mut K = [[0.0; 3]; 3];
                K[0][0] = self.params[0];
                K[1][1] = self.params[1];
                K[0][2] = self.params[2];
                K[1][2] = self.params[3];
                K[2][2] = 1.0;
                return Ok(K);
            },
            _ => panic!("Not implemented"),
        }
    }
    fn __str__(&self) -> PyResult<String>   {
        Ok(format!("<Camera ID: {}, width: {}, height: {}, model: {}>", self.camera_id, self.width, self.height, self.model_id))
    }
    fn __repr__(&self) -> PyResult<String>{ Camera::__str__(self)}
}

impl fmt::Display for Camera {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Camera ID: {}, Model ID: {:?}\n Width: {} Height: {} \n Params: {:?}", self.camera_id, self.model_id, self.width, self.height, self.params)
    }
}