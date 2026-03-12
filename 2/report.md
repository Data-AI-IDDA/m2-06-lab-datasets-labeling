# Lab Report: Dataset Creation and Labeling (Cat)
**Student ID:** 2
**Rank:** 2
**Class Size (N):** 33

## Dataset Summary
- **Requested Images (k):** 250
- **Successfully Verified:** 218
- **Failed Downloads:** 32 (Automatically removed to ensure dataset integrity)
- **Verification Status:** PASS (All images have matching YOLO labels and valid coordinates)

## Technical Process
1. **Partitioning:** Utilized a deterministic rank-based sampling ($ImageID[rank + iN]$) to ensure a non-overlapping slice of the Open Images V6 master list.
2. **Coordinate Transformation:** Converted Open Images normalized corner coordinates to YOLO center-width-height format.
3. **Quality Control:** - Ran `verify_yolo_dataset.py` to check for missing files and coordinate validity.
   - Synced `my_imageids.txt` with the local `images/` directory to ensure the "Master List" provided to the class is 100% accurate.

## Observations & Insights
- **Data Availability:** Approximately 12.8% of the source URLs from Open Images V6 were no longer accessible, requiring a larger initial sample (k=250) to reach the target volume.
- **Label Consistency:** All bounding boxes were verified to be for the "Cat" class (MID: /m/01yrx) and excluded "group-of" or "depiction" tags to maintain training quality.
- **ML Utility:** The high count of 218 images provides better statistical representation for the Data Science team's analysis regarding image resolution and box distribution.