# Greek-CAPTCHA-Cracker
This is a system to crack Greek Captcha - CS771 (IITK)


## Project Overview

This project involves extracting and recognizing characters from CAPTCHA images. Each CAPTCHA consists of three uppercase Greek characters within 150 × 500 pixel images, which may be rotated at angles of 0°, ±10°, ±20°, or ±30°. The images also feature obfuscating lines that complicate the extraction process.

## Methodology

### 1. Preprocessing of Image (Data Cleaning)

To ensure effective character recognition, several preprocessing steps were applied to clean the CAPTCHA images:

#### a. Background Removal

1. **Image Conversion**: Convert the image from BGR to HSV color space.
2. **Foreground Extraction**: Extract the 'S' (Saturation) channel and remove values below half of the maximum saturation.
3. **Create Mask**: Use the mask to isolate the main content of the image.
4. **Invert Mask**: Invert the mask to isolate the background.
5. **Combine Foreground and Background**: Merge the background with the original image to achieve a white background.

#### b. Stray Line Removal

1. **Refinement of Mask**: Adjust the mask to remove stray lines while preserving the characters.
2. **Final Combination**: Merge the refined mask with the original image to produce a clean result.

**References**: Background removal and stray line filtering techniques were adapted from [FreedomVC](https://www.freedomvc.com/index.php/2022/01/17/basic-background-remover-with-opencv/).

### 2. Character Recognition Models

Two different models were utilized for character recognition:

#### a. Convolutional Neural Network (CNN)

1. **Model Architecture**: A CNN model was used for its capability to extract and recognize features from images.
2. **Training Procedure**:
   - **Dataset**: Utilized the set of 2000 CAPTCHA images with three characters each.
   - **Augmentation**: Applied data augmentation techniques like rotation and scaling to improve model performance.
   - **Hyperparameter Tuning**: Optimized learning rate, batch size, and number of epochs through grid search or random search.
   - **Validation**: Used a validation set to tune hyperparameters and prevent overfitting.

3. **Validation**: Performance was assessed using accuracy, precision, recall, and F1-score on a test set.

#### b. Support Vector Machine (SVM)

1. **Feature Extraction**: Features were extracted from preprocessed images and fed into the SVM model.
2. **Training Procedure**:
   - **Kernel Selection**: Used kernels like linear, polynomial, or RBF to find the best fit.
   - **Hyperparameter Tuning**: Optimized parameters such as C (regularization parameter) and gamma (kernel coefficient).
   - **Validation**: Used cross-validation techniques to tune hyperparameters and evaluate model performance.

3. **Validation**: Performance was evaluated on a test set using metrics like accuracy, precision, recall, and F1-score.

## Conclusion

The preprocessing steps were crucial in preparing the CAPTCHA images for accurate character recognition. Both CNN and SVM models were employed to ensure robust character extraction. The CNN model leveraged its feature extraction capabilities, while the SVM model provided a different approach to classification, resulting in a comprehensive solution for CAPTCHA character recognition. CNN gave exceptional result of 100% accuracy but the model size was 136 MB so I used SVM later on which also gave 100% accuracy but the model size was 3.69 MB which is exceptionally lesser than the CNN model size.
