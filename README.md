# Greek-CAPTCHA-Cracker
This is a system to crack Greek Captcha - CS771 (IITK)

## Project Overview

This project involves the extraction and recognition of characters from CAPTCHA images. The CAPTCHAs consist of three uppercase Greek characters, each image being 150 × 500 pixels. The characters in the images are rotated at angles of 0°, ±10°, ±20°, or ±30°, and there are obfuscating lines of varying shades in the background.

## Methodology

### 1. Preprocessing of Image (Data Cleaning)

To accurately identify and extract characters from the CAPTCHA images, several preprocessing steps were implemented to clean the images:

#### a. Background Removal

1. **Image Conversion**: Convert the image from BGR to HSV color space.
2. **Foreground Extraction**: Extract the 'S' (Saturation) channel from the HSV image and remove values less than half of the maximum saturation.
3. **Create Mask**: Use the foreground mask to isolate the main content of the image.
4. **Invert Mask**: Invert the foreground mask to get the background.
5. **Combine Foreground and Background**: Convert the background back to BGR color space and combine it with the original image to achieve a white background with clear characters.

#### b. Stray Line Removal

1. **Refinement of Mask**: Adjust the mask to effectively remove stray lines without altering the characters.
2. **Final Combination**: Combine the refined foreground mask with the original image to produce the final output, which is free from stray lines and obfuscating elements.

**References**: The above functions for background removal and stray line filtering were implemented based on methods detailed in the [FreedomVC blog](https://www.freedomvc.com/index.php/2022/01/17/basic-background-remover-with-opencv/).

## Algorithms Used

1. **Image Segmentation**: To isolate and process individual characters.
2. **Character Recognition**: For identifying characters after preprocessing.

## Hyperparameter Search Procedures

- **Foreground Mask Threshold**: Adjusted the threshold for the saturation channel to achieve optimal background removal.
- **Mask Refinement**: Tuned the parameters for mask refinement to effectively eliminate stray lines.

## Validation Procedure

- **Visual Inspection**: Manually inspected a subset of processed images to ensure the accuracy of background removal and line filtering.
- **Performance Metrics**: Evaluated the effectiveness of preprocessing by assessing the clarity of extracted characters and their suitability for recognition algorithms.

## Conclusion

The preprocessing techniques applied significantly improve the accuracy of character extraction from CAPTCHA images by effectively removing background noise and obfuscating lines. These cleaned images are then ready for further character recognition tasks.


