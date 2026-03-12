import os

images_dir = "images"
labels_dir = "labels"
imageids_file = "my_imageids.txt"

# Takes the names of image files
existing_images = {os.path.splitext(f)[0] for f in os.listdir(images_dir)}

# Read imageids.txt
with open(imageids_file) as f:
    ids = [line.strip() for line in f]

valid_ids = []

for img_id in ids:
    if img_id in existing_images:
        valid_ids.append(img_id)
    else:
        label_path = os.path.join(labels_dir, img_id + ".txt")
        if os.path.exists(label_path):
            os.remove(label_path)

# Write new imageids.txt
with open(imageids_file, "w") as f:
    for img_id in valid_ids:
        f.write(img_id + "\n")

print("Dataset fixed.")
print("Remaining images:", len(valid_ids))