
use ahash::RandomState;
use std::collections::HashMap;
use std::collections::HashSet;
use crate::types::{image_t,point3D_t};
use crate::point3d::Point3D;

pub fn compute_overlaps(points3D: HashMap<point3D_t, Point3D, RandomState>) -> HashMap<image_t, HashMap<image_t, u32, RandomState>, RandomState>{
    println!("Computing overlaps...");
    let mut shared_points: HashMap<image_t, HashMap<image_t, u32, RandomState>, RandomState> = HashMap::default();
    for (_, point) in points3D {
        let unique_im_ids: Vec<u32> = point.track.iter().map(|&(x, _)| x).collect::<HashSet<_>>().into_iter().collect();
        for i in 0..unique_im_ids.len() {
            let im_i = unique_im_ids[i];
            *shared_points.entry(im_i).or_insert_with(HashMap::default).entry(im_i).or_insert(0) += 1;
            for j in 0..i {
                let im_j = unique_im_ids[j];
                    *shared_points.entry(im_i).or_insert_with(HashMap::default).entry(im_j).or_insert(0) +=1;
                    *shared_points.entry(im_j).or_insert_with(HashMap::default).entry(im_i).or_insert(0) +=1;
            }
        }
    }    println!("Done computing overlaps.");
    return shared_points;
}



pub fn compute_overlap_percentages(points3D: HashMap<point3D_t, Point3D, RandomState>) -> HashMap<image_t, HashMap<image_t, f32, RandomState>, RandomState> {
    let shared_points = compute_overlaps(points3D);
    
    println!("Computing percentages...");
    let mut overlap_percentages: HashMap<image_t, HashMap<image_t, f32, RandomState>, RandomState> = HashMap::default();
    
    for (img1, overlaps) in shared_points.iter() {
        let total_points_img1 = *overlaps.get(img1).unwrap_or(&1) as f32;  // Total points is the overlap with itself
        
        for (img2, count) in overlaps.iter() {
            if img1 != img2 {  // Skip the self-overlap
                let percentage = *count as f32 / total_points_img1;
                overlap_percentages
                    .entry(*img1)
                    .or_insert_with(HashMap::default)
                    .insert(*img2, percentage);
            }
        }
    }
    
    println!("Done computing percentages.");
    return overlap_percentages;
}