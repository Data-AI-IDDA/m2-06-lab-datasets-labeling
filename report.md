student id: 19
class size: 33
11 image download failed, 89 succesful. output of test is below:
=== YOLO DATASET VERIFICATION ===
 ImageIDs checked:  100                          
 Missing images:    0          
 Missing labels:    0
 Bad label lines:   0
 
tricks images:

images\0cc955135a5cfaf3.jpg
cat's color is similar to the bed's color. it is hard to see cat.

images\0e5448942162349c.jpg
cat is in unusual position, its face 
is not visible

images\289834597d8e4c0b.jpg
photo itself is unusual, as it is in rectangle and unusual filter is applied to photo

images\14973f5c6cc5d658.jpg
very low resolution photo with unusual-beerdrinking cat

images\3995ea796e4acec7.jpg
cat is not visible because its color contrast with environment

images\2538e6f08b8bba0a.jpg
same as above

images\0734ee81e7fea860.jpg
cat is very small, almost not visible

images\0529acc72084c7fe.jpg
very close-up photo

images\271cc231a3ae6fd9.jpg
unusual position issue

images\0239b4f271cf6c07.jpg
cat is wearing glasses, so, its face is not visible

images\211f8f8ac4ef34e1.jpgphoto was taken while cat is in motion, so, its face is blurry


bias analysis:
light-colored(white and orange) 
are underpresented. Model can 
get wrong light-colored or baby 
cats. Because in our set, dark-
colored cats are dominant and 
because of environment factors, 
light-colored cats is hard to detect 
than dark-coloreds.mixed-colored cats dominates my 
image set.