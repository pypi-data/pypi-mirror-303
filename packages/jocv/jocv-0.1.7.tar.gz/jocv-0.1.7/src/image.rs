use cgmath::{InnerSpace, Matrix, Zero};
use cgmath::{Vector2, Vector3, Quaternion, Matrix3};
use pyo3::pyclass;
use pyo3::prelude::*;
use crate::types::{image_t, camera_t, point3D_t, kInvalidPoint3DIdx};

#[pyclass]
pub struct Image {
    #[pyo3(get)]
    pub image_id: image_t,
    #[pyo3(get)]
    pub camera_id: camera_t,
    #[pyo3(get)]
    pub name: String,
    pub rot: Quaternion<f64>,
    pub trans: Vector3<f64>,
    #[allow(non_snake_case)]
    pub points2D: Vec<Vector2<f64>>,
    #[pyo3(get)]
    pub point3D_ids: Vec<point3D_t>,
}


#[pymethods]
impl Image {
    #[getter]
    fn get_rot(&self) -> PyResult<[[f64; 3]; 3]> {
        return Ok(Matrix3::from(self.rot).transpose().into());
    }
    #[getter]
    fn get_trans(&self) -> PyResult<[f64; 3]> {
        return Ok(self.trans.into());
    }
    #[getter]
    fn get_points2D(&self) -> PyResult<Vec<[f64; 2]>> {
        let mut points2D = Vec::new();
        for point in &self.points2D {
            points2D.push((*point).into());
        }
        return Ok(points2D);
    }
    #[getter]
    fn get_point3D_ids(&self) -> PyResult<Vec<point3D_t>> {
        return Ok(self.point3D_ids.clone());
    }
    fn get_tracked_point3D_ids(&self) -> PyResult<Vec<point3D_t>> {
        let mut tracked_point3D_ids: Vec<point3D_t> = Vec::new();
        for pt3D_id in &self.point3D_ids {
            if *pt3D_id != kInvalidPoint3DIdx {
                tracked_point3D_ids.push(*pt3D_id);
            }
        }
        return Ok(tracked_point3D_ids);
    }
    fn get_tracked_points2D(&self) -> PyResult<Vec<[f64; 2]>> {
        let mut tracked_points2D:  Vec<[f64; 2]> = Vec::new();
        for (pt2D, pt3D_id) in self.points2D.iter().zip(self.point3D_ids.iter()) {
            if *pt3D_id == kInvalidPoint3DIdx {
                continue;
            }
            tracked_points2D.push((*pt2D).into());
        }
        return Ok(tracked_points2D);
    }
    fn relative_pose_from(&self, other: &Image) -> PyResult<([[f64; 3];3], [f64;3])> {
        let rel_rot = self.rot * other.rot.conjugate();
        let rel_rot = rel_rot.normalize();
        let rel_trans = rel_rot * (-other.trans) + self.trans;
        
        return Ok((Matrix3::from(rel_rot).transpose().into(), rel_trans.into()));
    }
    fn relative_pose_to(&self, other: &Image) -> PyResult<([[f64; 3];3], [f64;3])> {
        return other.relative_pose_from(self);
    }
    fn __str__(&self) -> PyResult<String>   {
        Ok(format!("<Image ID: {}, name: {}, rot: {:?}, trans: {:?}>", self.camera_id, self.image_id, self.rot, self.trans))
    }
    fn __repr__(&self) -> PyResult<String>{ Image::__str__(self)}
}