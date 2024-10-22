use crate::types::{point2D_t, image_t};

//pub struct TrackElement {
//    pub image_id: image_t,
//    // The point in the image that the track element is observed.
//    #[allow(non_snake_case)]
//    pub point2D_idx: point2D_t,
//}
pub type TrackElement = (image_t, point2D_t);
pub struct Track {
    pub elements_: Vec<TrackElement>,
}

impl Track{
    pub fn len(&self) -> usize{
        return self.elements_.len();
    }
    pub const fn elements(&self) -> &Vec<TrackElement>{
        return &self.elements_;
    }
}